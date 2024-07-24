

if [ $2 == a100 ]
    then
    CMD=" srun  -N 1 --pty --gres=gpu:a100:1 -p octave -A public python "
fi

if [ $2 == h100 ]
    then
    CMD="  srun  -p twills -A h100 --gres=gpu:h100:1 --export=ALL python"
fi

if [ $2 == h1002 ]
    then
    CMD="  srun  -p twills -A h100 --gres=gpu:h100:2 --export=ALL python"
fi
# fp16 = [324.7421773966231, 600.0817201560811, 1019.1094069141465, 1508.5728672586265, 1650.8977361964487]
set -x

quantpath=/home/dataset/quant/
modelpath=/home/dataset
dataset_path=/home/dataset/quant/checkpoint/dataset

model_type=$3
data_type=$4

for batch in    32 64 128 256 512      
#for batch in  1  

    do
    for seq in   128  
        do

            if [ ${data_type} == mix4 ]
                then 
                    bit=4
                    echo  "---------run mix 4--------"
                
                    model=${model_type}
                    echo ${model}   
                    rm -r ${quantpath}/quant${bit}/${model}/model.safetensors     
                    CUDA_VISIBLE_DEVICES=$1    ${CMD}  benchflops.py  --model_type ${data_type} --model_path  \
                    ${quantpath}/quant${bit}/${model} \
                    --quant_file ${quantpath}/quant${bit}/${model} \
                    --batch_size ${batch} --bit ${bit} --dataset_path ${dataset_path}  
                 
            fi
            
            if [ ${data_type} == mix8 ]
                then 
                    bit=8
                    echo  "---------run mix 8--------"
                 
                    model=${model_type}
                    echo ${model}   
                    rm -r ${quantpath}/quant${bit}/${model}/model.safetensors     
                    CUDA_VISIBLE_DEVICES=$1    ${CMD}  benchflops.py  --model_type ${data_type} --model_path  \
                    ${quantpath}/quant${bit}/${model} \
                    --quant_file ${quantpath}/quant${bit}/${model} \
                    --batch_size ${batch} --bit ${bit} --dataset_path ${dataset_path}  
          
            fi       

            if [ ${data_type} == quik ]
                then     
               bit=4
            echo  "---------run QUIK 4--------"
 
               
                model=${model_type}
                echo ${model}          
                CUDA_VISIBLE_DEVICES=$1  ${CMD}  benchflops.py  --model_type ${data_type} --model_path  \
                ${quantpath}/quantquik${bit}/${model} \
                --quant_file ${quantpath}/quantquik${bit}/${model} \
                --batch_size ${batch} --bit ${bit} --dataset_path  ${dataset_path}  
                
            fi

            if [ ${data_type} == fp16 ]
                then
            
                model=${model_type}
                     
                echo ${model}          
                CUDA_VISIBLE_DEVICES=$1 ${CMD} benchflops.py  --model_type ${data_type} --model_path  \
                ${modelpath}/${model} \
                --quant_file ${modelpath}/${model} --batch_size ${batch} --dataset_path ${dataset_path}   

            fi

            if [ ${data_type} == bitsandbytes ]
                then
            
                model=${model_type}
                     
                echo ${model}          
                CUDA_VISIBLE_DEVICES=$1 ${CMD} benchflops.py  --model_type ${data_type} --model_path  \
                ${modelpath}/${model} \
                --quant_file ${modelpath}/${model} --batch_size ${batch} --dataset_path ${dataset_path}  

            fi


            if [ ${data_type} == awq ]
                then
            
                model=${model_type}
                    echo ${model}
                    CUDA_VISIBLE_DEVICES=$1    ${CMD} benchflops.py  --model_type ${data_type} --model_path  \
                    ${quantpath}/awqquant/${model} \
                    --quant_file ${quantpath}/awqquant/${model} --batch_size ${batch} --dataset_path ${dataset_path}  
                 
            fi


         
        done 
done
