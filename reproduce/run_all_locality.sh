models=(     "Llama-2-13b"  ) 
for model in "${models[@]}"
do
    if [ $1 == h100 ]
        then
        

        # mixq
        bash runlocality.sh  0 $1  ${model}  mix8


    
    fi
done

