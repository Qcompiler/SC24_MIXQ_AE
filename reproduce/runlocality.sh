if [ $2 == a100 ]
    then
    CMD=" srun  -N 1 --pty --gres=gpu:a100:1 -p octave -A public python "
fi

if [ $2 == h100 ]
    then
    CMD="srun  -p twills -A h100 --gres=gpu:h100:1 --export=ALL python"
fi

set -x

quantpath=/home/dataset/quant/
modelpath=/home/dataset
dataset_path=/home/dataset/quant/checkpoint/dataset

model=$3
data_type=$4


for batch in    512 
    do
    for seq in   64  
        do


 

            if [ ${data_type} == mix8 ]
                then 
                    bit=8
                    echo  "---------use   mix 8  to bench --------"
     
                        echo ${model}          
                        rm -r ${quantpath}/quant${bit}/down_weight_only/${model}/model.safetensors     
                        CUDA_VISIBLE_DEVICES=$1    \
                        ${CMD} evallocality.py  --model_type ${data_type} --model_path  \
                        ${quantpath}/quant${bit}/down_weight_only/${model} \
                        --quant_file ${quantpath}/quant${bit}/down_weight_only/${model} \
                        --n_ctx ${batch}  --n_batch $batch  --dataset_path ${dataset_path} --eval_accuracy True
   
            
            fi
     
        done 
done
