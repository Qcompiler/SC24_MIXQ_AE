files="reproduce_result/ppl/ppl_"
types=["bitsandbytes","awq","mix8","mix4","fp16"]
models = ["Llama-2-7b"]

out = {}
for type in types:
    out[type] = {}
    for model in models:
        out[type][model] = {}


for type in types:
    out[type] = {}
    for model in models:
        out[type][model] = {}
        file = files + type + "_" + model + ".csv"
        a = open(file)
        f = a.readlines()
        f = float(f[-1].split(",")[-1])
        out[type][model] = f
        print(out)