models=(    Llama-2-7b  Llama-2-13b  Llama-2-hf   ) 


if [ $1 == a100 ]
    then
    
            for model in "${models[@]}"
            do
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
            done
    
    # the output file is generated in reproduce_result/throughput 
    # if we run the scipt in h100, we should avoid overwrite the result
    rm -r reproduce_result/throughputa100
    mv reproduce_result/throughput  reproduce_result/throughputa100
    mkdir reproduce_result/throughput
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

    rm -r reproduce_result/throughputh100
    mv reproduce_result/throughput  reproduce_result/throughputh100
    mkdir reproduce_result/throughput

fi


