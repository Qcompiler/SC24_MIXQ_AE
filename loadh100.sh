conda activate h100
source /opt/spack/share/spack/setup-env.sh
spack load cuda@12.1.1 %gcc@12.2.0
spack load cudnn@8.9.7.29-12%gcc@11.3.0
spack load gcc@11.3.0
export PATH=$PATH:/sbin
Cur_Dir=$(pwd)
export PYTHONPATH=$PYTHONPATH:$Cur_Dir