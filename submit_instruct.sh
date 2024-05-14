#!/bin/bash
#SBATCH --job-name=translate
#SBATCH --exclude=node[01-06]
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=290G
#SBATCH --gres=gpu:4
# SBATCH --partition=A100
#SBATCH --time=30-00:00:00
# SBATCH --mail-type=ALL
# SBATCH --mail-user=minghao.wu@monash.edu
#SBATCH --output=/home/minghaow/llamamt-project/logs/%j-%x.out
#SBATCH --error=/home/minghaow/llamamt-project/logs/%j-%x.err

export HF_HOME=/nfsdata/data/minghaow/llamamt-project/cache
module load cuda/12.1.0-gcc-8.5.0-5lkaqss


nshots=$1
model_id=$2
tgt_lang=$3

python run_instruct.py \
    --model_id $model_id \
    --dataset facebook/flores \
    --tgt_lang $tgt_lang \
    --results_dir /home/minghaow/llamamt-project/llama3_mt/translations/$nshots-shot-instruct \
    --nshots $nshots