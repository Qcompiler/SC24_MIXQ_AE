

if [ $1 == a100 ]
    then
    CMD=" srun  -N 1 --pty --gres=gpu:a100:1 -p octave -A public python "
    else
    CMD="srun  -p twills -A h100 --gres=gpu:h100:1 --export=ALL python"
fi
#CMD=" python" 
 
set -x



models=(  "Baichuan2-7b"  "Baichuan2-13b" "Aquila2-7b" "Llama-2-7b"  "Mistral-7b" )
models=(  "llama-2-hf"    )
models=(  "Llama-2-7b"   "Llama-2-13b" )
#models=(  "opt-6.7b"   )
quantpath=/home/dataset/quant/quant
modelpath=/home/dataset

for bit in  4   
  do 
    for model in "${models[@]}"
            do
            echo ${model}
            ${CMD} \
              examples/basic_quant_mix.py  \
            --model_path ${modelpath}/${model} \
            --quant_file ${quantpath}${bit}/down_weight_only/${model} --w_bit ${bit}
    done
done
 

# for bit in 4 
#   do 
#     for model in "${models[@]}"
#             do
#             echo ${model}
#             ${CMD} \
#               examples/basic_quant_quik.py  \
#             --model_path ${modelpath}/${model} \
#             --quant_file ${quantpath}quik${bit}/${model} --w_bit ${bit}
#     done
# done
 
