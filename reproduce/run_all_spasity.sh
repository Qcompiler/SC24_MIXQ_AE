

CMD="srun -N 1 --pty --gres=gpu:a100:4 -p octave -A public python"
#CMD="python "
 
export PYTHONPATH=""
set -ex


model=LLama-2-7b



file=result/spasity${model}i4
#rm -r  reproduce_result/${file}
for i in {0..31..1}
do
   
   
    CUDA_VISIBLE_DEVICES=3 ${CMD}  benchsparsity_by_csv.py $i ${file} ${model} down mixq_4 2048 ${model}_down_sparsity.csv

done


# file=result/spasity${model}i8  
# #rm -r  reproduce_result/${file}
# for i in {0..31..1}
# do
   
   
#     CUDA_VISIBLE_DEVICES=2 ${CMD}  benchsparsity_by_csv.py $i ${file} ${model} down mixq_8 2048 ${model}_down_sparsity.csv

# done



# model=LLama-2-7b
# for i in {0..31..1}
# do
#     CUDA_VISIBLE_DEVICES=4 ${CMD}  benchsparsity_by_csv.py $i result/spasity ${model} down mixq_8 2048 ${model}_down_sparsity.csv

# done

# model=LLama-2-13b
# file=result/spasity${model}i4  
# #rm -r  reproduce_result/${file}
# for i in {0..39..1}
# do
   
   
#     CUDA_VISIBLE_DEVICES=3 ${CMD}  benchsparsity_by_csv.py $i ${file} ${model} down mixq_4 2048 ${model}_down_sparsity.csv

# done
#srun -N 1 --pty --gres=gpu:a100:1 -p octave -A public python benchsparsity.py LLama-2-13b_down_sparsity.csv result/spasity LLama-2-13b down mixq_8 2048


#srun -N 1 --pty --gres=gpu:a100:1 -p octave -A public python benchsparsity.py 0 result/spasity LLama-2-7b down mixq_8 2048

