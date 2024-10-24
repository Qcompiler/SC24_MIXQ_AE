import torch
import sys
sys.path.append('/home/chenyidong/anaconda3/envs/h100/lib/python3.11/site-packages')

token = 0
layer = 0
outfile_path = 'reproduce_result/'
args = sys.argv
if len(args) == 8:
    
    outfile_path += args[2]
    mod = args[3]
    projection = args[4]
    kernel = args[5]
    batch_size = args[6]
    layer = int(args[1])
    file = open(args[7])
    sparsity = float(file.readlines()[layer])
    print(sparsity)
    
else:
    print(
        "Usage: python benchbitsand.py layer path/to/profiling/results model_name Projection Kernel batch_size"
    )
    print(
        "       Please config your layer, model_name and projection for your model in above command."
    )
    print(
        "       We currently support FP16, EETQ, torch_int8, cublas, bitsandbytes, awq, quik_4, quik_8, cutlass, mixq_8, mixq_4 and fp8 kernels."
    )
    print("     We support batch size up to 512 and 2048 two mode, you can just input 512 or 2048 in the command/")
    exit(1)


if kernel != "fp8":
    from bitsandbytes.nn.modules import Linear8bitLt
    import bitsandbytes as bnb
    sys.path.append('/home/drc/mixq/src')
else:
    sys.path.append('/home/chenyidong/SC3/MixQ')

if batch_size == '512':
    test_batch_pool = [32, 64, 128, 256, 512]
elif batch_size == '2048':
    test_batch_pool = [32,64,128,256,512,1024,2048]
# file = "%d,%d,self_attn.q_proj"%(token,layer)
if projection == "up":
    file = "%d,%d,mlp.up_proj"%(token,layer)
elif projection == "down":
    file = "%d,%d,mlp.down_proj"%(token,layer)
else:
    file = "%d,%d,self_attn.q_proj"%(token,layer)

model = mod
if model == "LLama-2-13b":
    activation = torch.load('/home/chenyidong/activations/'+model+'/'+file,map_location=torch.device('cpu'))
elif model == "LLama-2-7b":
    activation = torch.load('/home/dataset/activation_tensor_llama-2-7b/'+file,map_location=torch.device('cpu'))
else:
    activation = torch.load('/home/dataset/'+model+'/'+file,map_location=torch.device('cpu'))

activation = torch.vstack((activation,activation))
activation = torch.vstack((activation,activation))
activation = torch.vstack((activation,activation))

# print(activation.shape)
# print(activation.abs().max())
def FindOutliers(activation, theta):
    tmp = torch.unique(torch.where((activation.abs() > theta))[1])
    return len(tmp)


if projection == "down":
    dic = {
        "LLama-2-13b": (8192, 13824),
        "LLama-2-7b": (4096, 11008),
        "LLama-2-70b": (4096, 8192)
    }
else:
    dic = {
        "LLama-2-13b": (12288, 5120),
        "LLama-2-7b": (12288, 4096),
        "LLama-2-70b": (10240, 8192)
    }


outfile = open(outfile_path, 'a')
print("running:", model+" "+ file + " with kernel: " + kernel)
print("layer: ", layer)
# print("layer: ", layer, file=outfile)

if kernel == 'FP16':
    # FP 16
    from torch.nn import functional as F
    for out_features, in_features in [dic[model]]:

        @torch.no_grad()
        def test_quant_linear_a16_w16(M, N, K) -> float:
            weight = torch.rand(N, K, dtype=torch.float16).cuda()
            x = torch.rand(M, K, dtype=torch.float16).cuda()
            elapsed_time_ms = 0
            iterations = 100
            for _ in range(10):
                y = F.linear(x, weight)

            for _ in range(iterations):
                start_event = torch.cuda.Event(enable_timing=True)
                end_event = torch.cuda.Event(enable_timing=True)
                torch.cuda.synchronize()
                start_event.record()
                y = F.linear(x, weight)
                end_event.record()
                torch.cuda.synchronize()
                elapsed_time_ms += start_event.elapsed_time(end_event)
            total_ops = M * N * K * 2 * iterations
            tflops = total_ops / elapsed_time_ms / 10**9
            return tflops, elapsed_time_ms

        print("0: linear FP16")
        print("FP16", end=",", file=outfile)
        a16w16_flops = []
        for m in test_batch_pool:
            tflops, elapsed_time_ms = test_quant_linear_a16_w16(
                m, out_features, in_features)
            a16w16_flops.append(tflops)
            print(tflops, end=",")
            print(tflops, end=",", file=outfile)
        print("\n")
        print("\n", file=outfile)
elif kernel == 'EETQ':
    # EETQ
    from EETQ import quant_weights, w8_a16_gemm
    for out_features, in_features in [dic[model]]:

        @torch.no_grad()
        def test_quant_linear_a16_w8(M, N, K) -> float:
            weight = torch.randn((N, K), dtype=torch.float16, device='cuda')
            int8_weight_cpu = torch.t(weight).contiguous().cpu()
            int8_weight, scales = quant_weights(int8_weight_cpu, torch.int8,
                                                False)
            x = activation[0:M].cuda()
            qweight = int8_weight.to(weight.device)
            weight_scales = scales.half().to(weight.device)
            elapsed_time_ms = 0
            iterations = 100
            for _ in range(10):
                y = w8_a16_gemm(x, qweight, weight_scales)
            torch.cuda.synchronize()
            for _ in range(iterations):
                start_event = torch.cuda.Event(enable_timing=True)
                end_event = torch.cuda.Event(enable_timing=True)
                torch.cuda.synchronize()
                start_event.record()
                y = w8_a16_gemm(x, qweight, weight_scales)
                end_event.record()
                torch.cuda.synchronize()
                elapsed_time_ms += start_event.elapsed_time(end_event)
            total_ops = M * N * K * 2 * iterations
            tflops = total_ops / elapsed_time_ms / 10**9
            return tflops, elapsed_time_ms

        print("1: EETQ")
        print("EETQ", end=",", file=outfile)
        a16w16_flops = []
        for m in test_batch_pool:
            tflops, elapsed_time_ms = test_quant_linear_a16_w8(
                m, out_features, in_features)
            a16w16_flops.append(tflops)
            print(tflops, end=",")
            print(tflops, end=",", file=outfile)
        print("\n")
        print("\n", file=outfile)
elif kernel == 'torch_int8':
    # torch_int8
    from torch_int._CUDA import linear_a8_w8_b32_o32
    for out_features, in_features in [dic[model]]:

        @torch.no_grad()
        def test_quant_linear_a8_w8(M, N, K) -> float:
            x = activation[0:M].cuda()
            weight = torch.randint(-128, 127, (N, K), dtype=torch.int8).cuda()
            bias = torch.randint(torch.iinfo(torch.int32).min,
                                 torch.iinfo(torch.int32).max, (N, ),
                                 dtype=torch.int32).cuda()
            linear = torch.nn.Linear(K, N, bias=True)
            linear.weight.data = weight.float()
            linear.bias.data = bias.float()
            elapsed_time_ms = 0
            iterations = 100
            for _ in range(10):
                act = x.to(torch.int8)
                y = linear_a8_w8_b32_o32(act, weight, bias)
            torch.cuda.synchronize()
            for _ in range(iterations):
                start_event = torch.cuda.Event(enable_timing=True)
                end_event = torch.cuda.Event(enable_timing=True)
                torch.cuda.synchronize()
                start_event.record()
                act = x.to(torch.int8)
                y = linear_a8_w8_b32_o32(act, weight, bias)
                end_event.record()
                torch.cuda.synchronize()
                elapsed_time_ms += start_event.elapsed_time(end_event)
            total_ops = M * N * K * 2 * iterations
            tflops = total_ops / elapsed_time_ms / 10**9
            return tflops, elapsed_time_ms

        print("2: torch int8")
        print("torch_int8", end=",", file=outfile)
        a16w16_flops = []
        for m in test_batch_pool:
            tflops, elapsed_time_ms = test_quant_linear_a8_w8(
                m, out_features, in_features)
            a16w16_flops.append(tflops)
            print(tflops, end=",")
            print(tflops, end=",", file=outfile)
        print("\n")
        print("\n", file=outfile)
elif kernel == 'cublas':
    # cublas int8
    from mixquant.Cache import MixLibCache, MLPCache
    from mixquant.modules.linear import MixLinear_GEMM
    import mixlib
    arch = torch.cuda.get_device_capability()[0]
    MixGemmcache = MixLibCache(4096)
    for out_features, in_features in [dic[model]]:

        @torch.no_grad()
        def test_gemm_int8(M, N, K):
            module = torch.nn.Linear(in_features, out_features).cuda()
            x = activation[0:M].cuda()
            q_linear = MixLinear_GEMM.from_linear(module,
                                                  bit=8,
                                                  weight_only=False,
                                                  init_only=False,
                                                  cache=MixGemmcache,
                                                  name="name")
            elapsed_time_ms = 0
            iterations = 100
            xi8 = q_linear.q_weight
            act = x.to(torch.int8)
            for i in range(10):
                mixlib.gemm(act, xi8, M, N, K)
            torch.cuda.synchronize()
            for _ in range(iterations):
                start_event = torch.cuda.Event(enable_timing=True)
                end_event = torch.cuda.Event(enable_timing=True)
                torch.cuda.synchronize()
                start_event.record()
                y = mixlib.gemm(act, xi8, M, N, K)
                end_event.record()
                torch.cuda.synchronize()
                elapsed_time_ms += start_event.elapsed_time(end_event)
            total_ops = M * N * K * 2 * iterations
            tflops = total_ops / elapsed_time_ms / 10**9
            return tflops, elapsed_time_ms

        print("3: cublas int8")
        print("cublas", end=",", file=outfile)
        w8a8o16_flops_quant = []
        for m in test_batch_pool:
            tflops, elapsed_time_ms = test_gemm_int8(m, out_features,
                                                     in_features)
            w8a8o16_flops_quant.append(tflops)
            print(tflops, end=",")
            print(tflops, end=",", file=outfile)
        print("\n")
        print("\n", file=outfile)
elif kernel == 'bitsandbytes':
    # bnb
    for out_features, in_features in [dic[model]]:

        @torch.no_grad()
        def test_quant_linear_w8_a8bnb(M, N, K) -> float:
            x = activation[0:M].cuda()
            linear_custom = Linear8bitLt(
                in_features,
                out_features,
                False,
                has_fp16_weights=False,
                threshold=6.0,
            )
            weight = torch.rand(N, K, dtype=torch.float16).cuda()
            linear_custom.weight = bnb.nn.Int8Params(
                weight, requires_grad=False,
                has_fp16_weights=False).to(torch.float16)
            linear_custom = linear_custom.cuda()
            elapsed_time_ms = 0
            iterations = 100
            for _ in range(10):
                y = linear_custom(x)
            torch.cuda.synchronize()
            for _ in range(iterations):
                start_event = torch.cuda.Event(enable_timing=True)
                end_event = torch.cuda.Event(enable_timing=True)
                torch.cuda.synchronize()
                start_event.record()
                y = linear_custom(x)
                end_event.record()
                torch.cuda.synchronize()
                elapsed_time_ms += start_event.elapsed_time(end_event)
                #l2Flusher.flush(cuda.Stream(0))
            total_ops = M * N * K * 2 * iterations
            tflops = total_ops / elapsed_time_ms / 10**9
            return tflops, elapsed_time_ms

        a8w8bnb_flops = []
        print("4: bnb")
        print("bnb", end=",", file=outfile)
        for m in test_batch_pool:
            tflops, elapsed_time_ms = test_quant_linear_w8_a8bnb(
                m, out_features, in_features)
            a8w8bnb_flops.append(tflops)
            print(tflops, end=",")
            print(tflops, end=",", file=outfile)
        print("\n")
        print("\n", file=outfile)
elif kernel == 'awq':
    # AWQ
    from awq_inference_engine import gemm_forward_cuda
    for out_features, in_features in [dic[model]]:

        @torch.no_grad()
        def test_quant_linear_a16_w4_gemv(M, N, K):
            groupSize = 128
            x = torch.rand(M, K, dtype=torch.float16, device='cuda')
            weight = torch.randint(0,
                                   128, (N, K // 32 * 4),
                                   dtype=torch.int32,
                                   device='cuda')
            scailing = torch.rand(
                K // groupSize, N, dtype=torch.float16, device='cuda') + 1
            zeros = torch.randint(0,
                                  128, (N, K // 32 * 4),
                                  dtype=torch.int32,
                                  device='cuda')
            elapsed_time_ms = 0
            iterations = 30
            for i in range(20):
                y = gemm_forward_cuda(x, weight, scailing, zeros, 8)
            for _ in range(iterations):
                start_event = torch.cuda.Event(enable_timing=True)
                end_event = torch.cuda.Event(enable_timing=True)
                torch.cuda.synchronize()
                start_event.record()
                y = gemm_forward_cuda(x, weight, scailing, zeros, 8)
                end_event.record()
                torch.cuda.synchronize()
                elapsed_time_ms += start_event.elapsed_time(end_event)
            total_ops = M * N * K * 2 * iterations
            tflops = total_ops / elapsed_time_ms / 10**9
            return tflops, elapsed_time_ms

        print("5: awq")
        print("awq", end=",", file=outfile)
        a16w4_flops = []
        for m in test_batch_pool:
            tflops, elapsed_time_ms = test_quant_linear_a16_w4_gemv(
                m, out_features, in_features)
            a16w4_flops.append(tflops)
            print(tflops, end=",")
            print(tflops, end=",", file=outfile)
        print("\n")
        print("\n", file=outfile)
elif kernel == 'quik_4':
    # QUIK int4
    sys.path.append('/home/drc/mixq/QUIK/experiments')
    from qlinear import MixedQLinear
    for out_features, in_features in [dic[model]]:

        @torch.no_grad()
        def test_quant_linear_a4_w4(M, N, K) -> float:
            x = activation[0:M].cuda()
            baseline_mod = torch.nn.Linear(in_features,
                                           out_features,
                                           bias=False).cuda().to(torch.float16)
            baseline_mod.weight.data = torch.randint_like(
                baseline_mod.weight.data, low=-8, high=7).to(torch.float16)
            fp_indices = torch.randperm(in_features)[:256]
            s_w = torch.ones((out_features, 1),
                             dtype=torch.float16,
                             device='cuda')
            int4_mod = MixedQLinear.from_float(baseline_mod,
                                               baseline_mod.weight.data,
                                               s_w,
                                               shared_input=None,
                                               fp_indices=fp_indices,
                                               bits=4).cuda()
            elapsed_time_ms = 0
            iterations = 100
            for _ in range(10):
                y = int4_mod(x)
            torch.cuda.synchronize()
            for _ in range(iterations):
                start_event = torch.cuda.Event(enable_timing=True)
                end_event = torch.cuda.Event(enable_timing=True)
                torch.cuda.synchronize()
                start_event.record()
                y = int4_mod(x)
                end_event.record()
                torch.cuda.synchronize()
                elapsed_time_ms += start_event.elapsed_time(end_event)
            total_ops = M * N * K * 2 * iterations
            tflops = total_ops / elapsed_time_ms / 10**9
            return tflops, elapsed_time_ms

        print("6: QUIK int4")
        print("QUIK int4", end=",", file=outfile)
        a16w16_flops = []
        for m in test_batch_pool:
            tflops, elapsed_time_ms = test_quant_linear_a4_w4(
                m, out_features, in_features)
            a16w16_flops.append(tflops)
            print(tflops, end=",")
            print(tflops, end=",", file=outfile)
        print("\n")
        print("\n", file=outfile)
elif kernel == 'cutlass':
    # int4Matmul
    import quik
    for out_features, in_features in [dic[model]]:

        @torch.no_grad()
        def test_int4(M, N, K) -> float:
            x = activation[0:M].cuda().to(torch.float16)
            int_weight = torch.randint(1,
                                       7, (out_features, in_features // 2),
                                       dtype=torch.uint8,
                                       requires_grad=False).cuda()
            reshaped_x = x.reshape((-1, x.shape[-1]))
            qscale_x = (
                torch.max(torch.abs(reshaped_x), dim=1)[0].unsqueeze(1) /
                (1 << (4 - 1) - 1)).to(torch.float16).cuda()
            qint_x = quik.symmetric.quantize(x, qscale_x, 4)
            y = quik.matmul.int4Matmul(qint_x, int_weight)
            elapsed_time_ms = 0
            iterations = 100
            for _ in range(10):
                quik.matmul.int4Matmul(qint_x, int_weight)
            torch.cuda.synchronize()
            for _ in range(iterations):
                start_event = torch.cuda.Event(enable_timing=True)
                end_event = torch.cuda.Event(enable_timing=True)
                torch.cuda.synchronize()
                start_event.record()
                quik.matmul.int4Matmul(qint_x, int_weight)
                end_event.record()
                torch.cuda.synchronize()
                elapsed_time_ms += start_event.elapsed_time(end_event)
            total_ops = M * N * K * 2 * iterations
            tflops = total_ops / elapsed_time_ms / 10**9
            return tflops, elapsed_time_ms

        print("7: int4")
        print("int4", end=",", file=outfile)
        a16w16_flops = []
        for m in test_batch_pool:
            tflops, elapsed_time_ms = test_int4(m, out_features, in_features)
            a16w16_flops.append(tflops)
            print(tflops, end=",")
            print(tflops, end=",", file=outfile)
        print("\n")
        print("\n", file=outfile)
elif kernel == 'mixq_8':
    # mixq int8
    from mixquant.Cache import MixLibCache, MLPCache
    from mixquant.modules.linear import MixLinear_GEMM
    import mixlib
    arch = torch.cuda.get_device_capability()[0]
    MixGemmcache = MixLibCache(4096)
    for out_features, in_features in [dic[model]]:

        int8_fp_features_num = int( in_features * sparsity)

        @torch.no_grad()
        def test_quant_linear_Mixq_gemm(M, N, K):
            module = torch.nn.Linear(in_features, out_features).cuda()
            x = activation[0:M].cuda()
            q_linear = MixLinear_GEMM.from_linear(module,
                                                  bit=8,
                                                  weight_only=False,
                                                  init_only=False,
                                                  cache=MixGemmcache,
                                                  name="name")
            q_linear.fp_indices = torch.as_tensor(range(0,int8_fp_features_num),dtype=torch.int32,device='cuda')
            q_linear.outliers = x[:, q_linear.fp_indices]
            q_linear.fp_weight = q_linear.q_weight[:,q_linear.fp_indices].to(torch.float16) 
            q_linear.fp_weight *=  q_linear.scale_col.T
            q_linear.add_outliers = False
            elapsed_time_ms = 0
            iterations = 300
            MixGemmcache.q_xcache = mixlib.FindRowScale(
                x, MixGemmcache.x_scale, M, in_features, 8)
            for i in range(50):
                q_linear(x, cache=MixGemmcache, bench_gemm=True)
            torch.cuda.synchronize()
            for _ in range(iterations):
                x = activation[0:M].cuda()
                start_event = torch.cuda.Event(enable_timing=True)
                end_event = torch.cuda.Event(enable_timing=True)
                torch.cuda.synchronize()
                start_event.record()
                y = q_linear(x, cache=MixGemmcache, bench_gemm=True)
                end_event.record()
                torch.cuda.synchronize()
                elapsed_time_ms += start_event.elapsed_time(end_event)
            total_ops = M * N * K * 2 * iterations
            tflops = total_ops / elapsed_time_ms / 10**9
            return tflops, elapsed_time_ms

        print("8: mixq int8")
        print("mixq_int8", end=",", file=outfile)
        w8a8o16_flops_quant = []
        for m in test_batch_pool:
            tflops, elapsed_time_ms = test_quant_linear_Mixq_gemm(
                m, out_features, in_features)
            w8a8o16_flops_quant.append(tflops)
            print(tflops, end=",")
            print(tflops, end=",", file=outfile)
        print("\n")
        print("\n", file=outfile)
elif kernel == 'mixq_4':
    # mixq int4
    from mixquant.Cache import MixLibCache, MLPCache
    from mixquant.modules.linear import MixLinear_GEMM
    import mixlib
    arch = torch.cuda.get_device_capability()[0]
    MixGemmcache = MixLibCache(4096)
    for out_features, in_features in [dic[model]]:
        if arch == 9:
            break

        @torch.no_grad()
        def test_quant_linear_Mixq_gemm(M, N, K):
            
            int4_fp_features_num = int( in_features * sparsity)  + 64
            module = torch.nn.Linear(in_features, out_features).cuda()
            x = activation[0:M].cuda()
            layer_scales = torch.max(module.weight.data.abs(), dim=0)[0]
            q_linear = MixLinear_GEMM.from_linear(
                module,
                bit=4,
                weight_only=False,
                init_only=False,
                cache=MixGemmcache,
                int4_fp_features_num=int4_fp_features_num,
                layer_scales=layer_scales,
                name="name")
            elapsed_time_ms = 0
            iterations = 300

            #sparsity *= 0
             
            MixGemmcache.q_xcache = mixlib.FindRowScale(
                x, MixGemmcache.x_scale, M, in_features, 4)
            

            
            q_linear.add_outliers = False
            for i in range(50):
                q_linear(x)
            torch.cuda.synchronize()
            for _ in range(iterations):
                x = activation[0:M].cuda()
                start_event = torch.cuda.Event(enable_timing=True)
                end_event = torch.cuda.Event(enable_timing=True)
                torch.cuda.synchronize()
                start_event.record()
                y = q_linear(x, cache=MixGemmcache, bench_gemm=True)
                end_event.record()
                torch.cuda.synchronize()
                elapsed_time_ms += start_event.elapsed_time(end_event)
            total_ops = M * N * K * 2 * iterations
            tflops = total_ops / elapsed_time_ms / 10**9
            return tflops, elapsed_time_ms

        print("9: mixq int4")
        print("mixq_int4", end=",", file=outfile)
        w8a8o16_flops_quant = []
        for m in test_batch_pool:
            tflops, elapsed_time_ms = test_quant_linear_Mixq_gemm(
                m, out_features, in_features)
            w8a8o16_flops_quant.append(tflops)
            print(tflops, end=",")
            print(tflops, end=",", file=outfile)
        print("\n")
        print("\n", file=outfile)
elif kernel == 'quik_8':
    # QUIK int8
    sys.path.append('/home/drc/mixq/QUIK/experiments')
    from qlinear import MixedQLinear
    for out_features, in_features in [dic[model]]:

        @torch.no_grad()
        def test_quant_linear_a8_w8(M, N, K) -> float:
            x = activation[0:M].cuda()
            baseline_mod = torch.nn.Linear(in_features,
                                           out_features,
                                           bias=False).cuda().to(torch.float16)
            baseline_mod.weight.data = torch.randint_like(
                baseline_mod.weight.data, low=-8, high=7).to(torch.float16)
            fp_indices = torch.randperm(in_features)[:256]
            s_w = torch.ones((out_features, 1),
                             dtype=torch.float16,
                             device='cuda')
            int8_mod = MixedQLinear.from_float(baseline_mod,
                                               baseline_mod.weight.data,
                                               s_w,
                                               shared_input=None,
                                               fp_indices=fp_indices,
                                               bits=8).cuda()
            elapsed_time_ms = 0
            iterations = 100
            for _ in range(10):
                y = int8_mod(x)
            torch.cuda.synchronize()
            for _ in range(iterations):
                start_event = torch.cuda.Event(enable_timing=True)
                end_event = torch.cuda.Event(enable_timing=True)
                torch.cuda.synchronize()
                start_event.record()
                y = int8_mod(x)
                end_event.record()
                torch.cuda.synchronize()
                elapsed_time_ms += start_event.elapsed_time(end_event)
            total_ops = M * N * K * 2 * iterations
            tflops = total_ops / elapsed_time_ms / 10**9
            return tflops, elapsed_time_ms

        print("9: QUIK int8")
        print("QUIK_8", end=",", file=outfile)
        a16w16_flops = []
        for m in test_batch_pool:
            tflops, elapsed_time_ms = test_quant_linear_a8_w8(
                m, out_features, in_features)
            a16w16_flops.append(tflops)
            print(tflops, end=",")
            print(tflops, end=",", file=outfile)
        print("\n")
        print("\n", file=outfile)
elif kernel == 'fp8':
    # FP8
    from typing import Any, Dict, List, Optional, Tuple, Union
    from vllm import _custom_ops as ops
    import torch

    def per_tensor_dequantize(
            tensor: torch.Tensor,
            inv_scale: Union[float, torch.Tensor]) -> torch.Tensor:
        fake_qweight = tensor.to(torch.float16)
        dq_weight = fake_qweight * inv_scale
        return dq_weight

    def per_tensor_quantize(
            tensor: torch.Tensor,
            inv_scale: Union[float, torch.Tensor]) -> torch.Tensor:
        finfo = torch.finfo(torch.float8_e4m3fn)
        qweight = (tensor / inv_scale).clamp(min=finfo.min, max=finfo.max)
        return qweight.to(torch.float8_e4m3fn)

    def apply(layer: torch.nn.Module,
              x: torch.Tensor,
              bias: Optional[torch.Tensor] = None) -> torch.Tensor:

        if False:
            qinput, x_scale = ops.scaled_fp8_quant(x, layer.input_scale)

            # Fused GEMM_DQ
            output = ops.cutlass_scaled_mm(
                qinput,
                layer.weight,
                out_dtype=x.dtype,
                scale_a=x_scale,
                scale_b=layer.weight_scale,
            )
        else:
            qinput, x_scale = ops.scaled_fp8_quant(x,
                                                   layer.input_scale,
                                                   batch_dim_padding=17)
            output, _ = torch._scaled_mm(
                qinput,
                layer.weight,
                out_dtype=x.dtype,
                scale_a=x_scale,
                scale_b=layer.weight_scale,
                bias=bias,
            )

        return torch.narrow(output, 0, 0, x.shape[0])

    for out_features, in_features in [dic[model]]:

        @torch.no_grad()
        def test_quant_linear_fp8(M, N, K) -> float:

            x = activation[0:M].cuda()

            elapsed_time_ms = 0
            iterations = 100
            layer = torch.nn.Linear(K, N, device='cuda')

            input_scale = None
            qweight, weight_scale = ops.scaled_fp8_quant(layer.weight,
                                                         scale=None)

            class Layer:

                def __init__(self) -> None:
                    pass

            fp8layer = Layer()
            fp8layer.weight_scale = weight_scale
            fp8layer.weight = qweight.t()
            fp8layer.input_scale = input_scale

            for _ in range(50):
                y = apply(fp8layer, x)
            torch.cuda.synchronize()
            for _ in range(iterations):
                start_event = torch.cuda.Event(enable_timing=True)
                end_event = torch.cuda.Event(enable_timing=True)
                torch.cuda.synchronize()
                start_event.record()
                y = apply(fp8layer, x)
                end_event.record()
                torch.cuda.synchronize()
                elapsed_time_ms += start_event.elapsed_time(end_event)

            total_ops = M * N * K * 2 * iterations
            tflops = total_ops / elapsed_time_ms / 10**9
            return tflops, elapsed_time_ms

        print("10: FP8")
        print("FP8", end=",", file=outfile)
        a16w16_flops = []
        for m in test_batch_pool:
            tflops, elapsed_time_ms = test_quant_linear_fp8(
                m, out_features, in_features)
            a16w16_flops.append(tflops)
            print(tflops, end=",")
            print(tflops, end=",", file=outfile)
        print("\n")
        print("\n", file=outfile)
else:
    print("Error: Unknown kernel!")
    print(
        "       We currently support FP16, EETQ, torch_int8, cublas, bitsandbytes, awq, quik_4, quik_8, cutlass, mixq_8, mixq_4 and fp8 kernels."
    )
    exit(1)
