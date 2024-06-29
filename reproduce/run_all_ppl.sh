if [ $1 == a100 ]
    then
    

    # mixq
    bash runppl.sh  0 $1 Llama-2-7b   mix4
    # bash runppl.sh  0 $1 Llama-2-7b   mix8

    # #  quik
    # bash runppl.sh  0 $1 Llama-2-7b   quik

    # #  bitsandbytes
    # bash runppl.sh  0 $1 Llama-2-7b   bitsandbytes

    # #  fp16
    # bash runppl.sh  0 $1 Llama-2-7b   fp16

 
    # bash runppl.sh  0 $1 Llama-2-7b   awq
 
fi

if [ $1 == h100 ]
    then
    

    # mixq
    bash runppl.sh  0 $1 Llama-2-13b   mix8

    # # quik H100 do not have int4 tensorcode
    # bash runppl.sh  0 $1 Llama-2-7b   quik

    # # bitsandbytes
    bash runppl.sh  0 $1 Llama-2-7b   bitsandbytes

    # # fp16
    bash runppl.sh  0 $1 Llama-2-7b   fp16

 
    bash runppl.sh  0 $1 Llama-2-7b   awq
 
fi

