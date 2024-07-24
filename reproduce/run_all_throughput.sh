models=(    Llama-2-7b     ) 

for model in "${models[@]}"
    do
        if [ $1 == a100 ]
            then
            
            
                    # mixq
                    bash runthroughput.sh  0 $1  ${model}   mix4
                    bash runthroughput.sh  0 $1  ${model}   mix8

                    # quik
                    bash runthroughput.sh  0 $1  ${model}   quik

                    # bitsandbytes
                    bash runthroughput.sh  0 $1  ${model}   bitsandbytes

                    # fp16
                    bash runthroughput.sh  0 $1  ${model}   fp16

                    # awq
                    pip install transformers==4.35
                    bash runthroughput.sh  0 $1  ${model}   awq
                    pip install transformers==4.41.2

        

        fi

        if [ $1 == h100 ]
            then
            # use two H100 to run the Llama-70B models
            model=llama-2-hf
            # mixq
            bash runthroughput.sh  0 $1  ${model}   mix8

            # # bitsandbytes
            #bash runthroughput.sh  0 $1  ${model}   bitsandbytes

            # # fp16
            bash runthroughput.sh  0,1  h1002 ${model}   fp16




        fi


done 