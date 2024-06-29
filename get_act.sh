
CMD=" srun  -N 1 --pty --gres=gpu:a100:6 -A h100 -p a100  python "
#CMD="srun  -p twills -A h100 --gres=gpu:h100:2 --export=ALL python"
set -x

model=( llama-2-hf )
# model=( Aquila2-7b )
# model=( Baichuan2-7b )
$CMD examples/smooth_quant_get_act.py  --model-name /home/dataset/${model}  \
        --output-path /home/chenyidong/SC3/MixQ/src/act_scales/${model}.pt  --dataset-path /home/chenyidong/val.jsonl.zst 

