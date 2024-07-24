models=(     "Llama-2-7b" "Llama-2-13b"  ) 
for model in "${models[@]}"
    do
        if [ $1 == a100 ]
            then
            

            # mixq
            bash runlatency.sh  0 $1 ${model}   mix4
            bash runlatency.sh  0 $1 ${model}   mix8

            # quik
            bash runlatency.sh  0 $1 ${model}   quik

            # bitsandbytes
            bash runlatency.sh  0 $1 ${model}   bitsandbytes

            # fp16
            bash runlatency.sh  0 $1 ${model}   fp16

            #awq
            pip install transformers==4.35
            bash runlatency.sh  0 $1 ${model}   awq
            pip install transformers==4.41.2



        fi

done


