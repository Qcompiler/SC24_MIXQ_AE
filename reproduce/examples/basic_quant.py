
import os
import sys
sys.path.append('/home/chenyidong/AutoAWQ')
from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer

 
quant_config = { "zero_point": True, "q_group_size": 128, "w_bit": 4, "version": "GEMM" }


import argparse
parser = argparse.ArgumentParser(description="Calculate Perplexity for a model.")
parser.add_argument("--model_path", type=str,   help="Model path")
parser.add_argument("--quant_file", type=str,   help="quant_file Model path")
parser.add_argument("--w_bit", type=int, default=8,  help="weight bit")
args = parser.parse_args()

model_path = args.model_path
quant_path = args.quant_file

print(quant_path)
# Load model
# NOTE: pass safetensors=True to load safetensors
model = AutoAWQForCausalLM.from_pretrained(model_path,   **{"low_cpu_mem_usage": True},device_map='cpu')
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

# Quantize
model.quantize(tokenizer, quant_config=quant_config)

# Save quantized model
# NOTE: pass safetensors=True to save quantized model weights as safetensors
model.save_quantized(quant_path)
tokenizer.save_pretrained(quant_path)

print(f'Model is quantized and saved at "{quant_path}"')