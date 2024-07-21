#!/bin/bash

# for i in {0..31}; do
#     # echo "evaluate ${file}" >> eval_out
#     srun -N 1 --pty --gres=gpu:a100:1 -p octave -A public python benchbitsand.py $i result/llama70b-up.csv LLama-2-70b up
# done
rm -r result/kernel_8
rm -r result/kernel_4

export PYTHONPATH=""
kernels_8=("FP16" "EETQ" "torch_int8" "bitsandbytes" "mixq_8")
kernels_4=("FP16" "awq" "quik_4" "cutlass" "mixq_4")
for kernel in "${kernels_8[@]}"; do
  echo ${kernel}
  srun -N 1 --pty --gres=gpu:a100:1 -p octave -A public python benchbitsand.py 0 result/kernel_8 LLama-2-7b q $kernel 2048
done

for kernel in "${kernels_8[@]}"; do
  echo ${kernel}
  srun -N 1 --pty --gres=gpu:a100:1 -p octave -A public python benchbitsand.py 0 result/kernel_8 LLama-2-13b q $kernel 2048
done
for kernel in "${kernels_8[@]}"; do
  echo ${kernel}
  srun -N 1 --pty --gres=gpu:a100:1 -p octave -A public python benchbitsand.py 0 result/kernel_8 LLama-2-70b q $kernel 2048
done

for kernel in "${kernels_4[@]}"; do
  echo ${kernel}
  srun -N 1 --pty --gres=gpu:a100:1 -p octave -A public python benchbitsand.py 0 result/kernel_4 LLama-2-7b q $kernel 2048
done

for kernel in "${kernels_4[@]}"; do
  echo ${kernel}
  srun -N 1 --pty --gres=gpu:a100:1 -p octave -A public python benchbitsand.py 0 result/kernel_4 LLama-2-13b q $kernel 2048
done

for kernel in "${kernels_4[@]}"; do
  echo ${kernel}
  srun -N 1 --pty --gres=gpu:a100:1 -p octave -A public python benchbitsand.py 0 result/kernel_4 LLama-2-70b q $kernel 2048
done

python kernel.py