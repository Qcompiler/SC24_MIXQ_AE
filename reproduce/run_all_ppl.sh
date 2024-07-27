models=(   "Llama-2-7b"   "Llama-2-13b"  ) 
rm -r reproduce_result/ppl_summarise.out
for model in "${models[@]}"
do
    if [ $1 == a100 ]
        then
        
        bash runppl.sh  0 $1 ${model}   awq
        # mixq
        bash runppl.sh  0 $1 ${model}   mix4
        bash runppl.sh  0 $1 ${model}   mix8

        #  quik
        bash runppl.sh  0 $1 ${model}   quik

        #  bitsandbytes
        bash runppl.sh  0 $1 ${model}   bitsandbytes

        #  fp16
        bash runppl.sh  0 $1 ${model}   fp16

        

       
        
         
    
    fi

done