
import os

os.environ["WORLD_SIZE"] = "1"
import sys
sys.path.append('/home/chenyidong/quant/AutoAWQ')
from mixquant import AutoForCausalLM
from transformers import AutoTokenizer

import argparse
parser = argparse.ArgumentParser(description="Calculate Perplexity for a model.")
parser.add_argument("--model_path", type=str,   help="Model path")
parser.add_argument("--quant_file", type=str,   help="quant_file Model path")
parser.add_argument("--w_bit", type=int, default=8,  help="weight bit")
parser.add_argument("--weight_only_map", type=str, default="",  help="weight only linear layer map")
args = parser.parse_args()

model_path = args.model_path
quant_path = args.quant_file
weight_only_map = args.weight_only_map

if len(weight_only_map) == 0:
    weight_only_map = None
quant_config = { "w_bit": args.w_bit, "version": "MIX" }
print(quant_path)
# Load model
# NOTE: pass safetensors=True to load safetensors
model = AutoForCausalLM.from_pretrained(model_path, mix = True, **{"low_cpu_mem_usage": True},device_map='cpu')
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

print(model)
# Quantize
model.quantize_mix(tokenizer, quant_config=quant_config, weight_only_map_str = weight_only_map )

# Save quantized model
# NOTE: pass safetensors=True to save quantized model weights as safetensors
model.save_quantized(quant_path)
tokenizer.save_pretrained(quant_path)

print(f'Mix Model is quantized and saved at "{quant_path}"')