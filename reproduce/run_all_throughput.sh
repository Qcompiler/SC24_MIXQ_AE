if [ $1 == a100 ]
    then
    

    # mixq
    bash runthroughput.sh  0 $1 Llama-2-7b   mix4
    bash runthroughput.sh  0 $1 Llama-2-7b   mix8

    # quik
    bash runthroughput.sh  0 $1 Llama-2-7b   quik

    # bitsandbytes
    bash runthroughput.sh  0 $1 Llama-2-7b   bitsandbytes

    # fp16
    bash runthroughput.sh  0 $1 Llama-2-7b   fp16

    # awq
    #pip install transformers==4.35
    bash runthroughput.sh  0 $1 Llama-2-7b   awq
    #pip install transformers==4.41.2

fi

if [ $1 == h100 ]
    then
    

    # mixq
    bash runthroughput.sh  0 $1 Llama-2-7b   mix8

    # # quik H100 do not have int4 tensorcode
    # bash runthroughput.sh  0 $1 Llama-2-7b   quik

    # # bitsandbytes
    # bash runthroughput.sh  0 $1 Llama-2-7b   bitsandbytes

    # # fp16
    # bash runthroughput.sh  0 $1 Llama-2-7b   fp16

    # # awq
    # #pip install transformers==4.35
    # bash runthroughput.sh  0 $1 Llama-2-7b   awq
    # #pip install transformers==4.41.2

fi



if [ $1 == h1002 ]
    then
    

    # mixq
    bash runthroughput.sh  0,1  $1 llama-2-hf   bitsandbytes

    # # quik H100 do not have int4 tensorcode
    # bash runthroughput.sh  0 $1 Llama-2-7b   quik

    # # bitsandbytes
    # bash runthroughput.sh  0 $1 Llama-2-7b   bitsandbytes

    # # fp16
    # bash runthroughput.sh  0 $1 Llama-2-7b   fp16

    # # awq
    # #pip install transformers==4.35
    # bash runthroughput.sh  0 $1 Llama-2-7b   awq
    # #pip install transformers==4.41.2

fi
