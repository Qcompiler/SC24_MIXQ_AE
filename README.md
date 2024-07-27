# AE of SC24 

For AE reviewers, we have prepared a server containing all the datasets and codes. Please contact chenyidong@mails.tsinghua.edu.cn to access the server.

## Hardware environments 

We run all the experiment in the two nodes: (1) 8 NVIDIA Ampere A100-PCIE-40GB GPUs with 2 AMD EPYC 7742 CPUs. (2) 2 NVIDIA Hopper H100-PCIE-80 GB with 2 AMD EPYC 7453 28-Core CPUs.


 We have provided a server for both environments. Please contact us for access to the server. Before installation and deployment, you need to log in to the server. This server has the same GPU and CPU configurations as we used in our paper.



## Operating System

Debian 6.1.27 or any Linux system that can support CUDA v12.1  and GCC v9.4 or above.


## Software environment

The compiler is CUDA 12.1.  The transformer version is 3.5 and the Pytorch version is 2.1.0.


## Installation and Compilation

For installation:

The installation process involves three libraries:  CUDA, CMake, and Pytorch. To optimize the time, you can use the module load on the provided cluster, which takes less than 10 seconds.

On our cluster, this could be done through those commands:

```
source load.sh
```





## Quantize Models. Please quantize the LLMs before inferencing and reproducing the result. We provide the script $quant.sh$ for quantizing

 the mixed-precision 4-bit and 8-bit model. Running the following command to quant a LlaMA-7B model (We have already did it for you in our server):

```  
bash   quant.sh  Llama-2-7b 
```


 ## Kernel performance evaluation. 
 
 For evaluating the kernel performance, the reader should download the activations (120GB) from the URL provided in activation tensor.txt. After downloading the tensor from the BaiduNetDisk. 

 
To reproduce  Fig.13 and Fig.14, the kernel performance of MixQ. The result could be reproduced by running:

``` 
 cd  SC24_MIXQ_AE/reproduce
 bash benchkernels.sh
```

The figures will be generated in  figure/tflops_int4_overall.pdf

  The kernel performance of MixQ should be faster than EETQ, AWQ, QUIK and Bitsandbytes   in A100 GPU. For LLama-2-70B mode, MixQ should reach about 443 TFLOPs for W8A8O16 quantizaiton and  724 TFLOPs for W4A4O16 quantizaiton.


To reproduce Fig.15, the layer performance of MixQ.     The result could be reproduced by running the following command :

``` 
bash benchlayers.sh 
```

The figures will be generated in  figure/donw_13B.pdf

   <!-- \item  reproduce Fig.16, the QAD is applied to achieve an average of $1.92\times$ performance enhancement.

The result could be reproduced by running:

\$ bash breakdown.sh (Time cost: 1 hour ) -->

 




## End-to-end throughput



<!-- To  reproduce Fig.17,   the order-reserved structure for outliers processing is much more costly-free than  order-permuted
% structure. The result could be reproduced by running:

% \$ cd  MixQ/reproduce

%  \$ bash overhead.sh (Time cost: 30 minutes ) -->


To  reproduce Fig.18, the result could be reproduced by running:

```
 bash run_all_throughput.sh a100 
```


To reproduce Fig.19. The result could be reproduced by running:

```
 bash run_all_throughput.sh h100 
```
(Time cost: 30 minutes )


To  reproduce Fig.20, the result could be reproduced by running:

```
bash run_all_latency.sh  a100 
```
 (Time cost: 4 hours )
 


## End-to-end Perplexity.




To  reproduce Table IV and Table V,  the perplexity of MixQ quantization method is lower than AWQ.
The result could be reproduced by running:

``` 
bash run_all_ppl.sh
python summarise_ppl.py >> reproduce_result/ppl_summarise.out
```
 
The summarise of the PPL is generated in   reproduce_result/ppl_summarise.out


<!-- # Locality and Sparsity of outliers.




To reproduce Fig.21 and Fig.22 ,  the locality and sparsity of outlier channels of different models. The result could be reproduced by running:

 \$ bash run\_all\_locality.sh  (Time cost: 4 hours )

 \end{itemize} -->



# Plotting

time: 10 minutes

The results that were used to create the figures in the submissions can be found in the reproduce/figure directory. 
Both Python scripts expect to be run from inside the plots directory.

To generate all the figures, please run

```
 bash plot_all.sh 
  ```
 
And we can get all the figures in the folder reproduce_result/figure.


 

 



