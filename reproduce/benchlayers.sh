#!/bin/bash

rm -r reproduce_result/result/spasity
export PYTHONPATH=""
set -ex
srun -N 1 --pty --gres=gpu:a100:1 -p octave -A public python benchsparsity.py 0 result/spasity LLama-2-13b down mixq_8 2048
srun -N 1 --pty --gres=gpu:a100:1 -p octave -A public python benchsparsity.py 20 result/spasity LLama-2-13b down mixq_8 2048
srun -N 1 --pty --gres=gpu:a100:1 -p octave -A public python benchsparsity.py 39 result/spasity LLama-2-13b down mixq_8 2048

srun -N 1 --pty --gres=gpu:a100:1 -p octave -A public python benchsparsity.py 0 result/spasity LLama-2-13b down mixq_4 2048
srun -N 1 --pty --gres=gpu:a100:1 -p octave -A public python benchsparsity.py 20 result/spasity LLama-2-13b down mixq_4 2048
srun -N 1 --pty --gres=gpu:a100:1 -p octave -A public python benchsparsity.py 39 result/spasity LLama-2-13b down mixq_4 2048

python spasity.py