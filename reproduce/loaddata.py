
from datasets import load_dataset


dataset = load_dataset("mit-han-lab/pile-val-backup", split="validation")
print(dataset)