#!/bin/bash
#SBATCH --job-name=translate
#SBATCH --exclude=node[01-04]
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=200G
#SBATCH --gres=gpu:1
#SBATCH --partition=A100
#SBATCH --time=30-00:00:00
# SBATCH --mail-type=ALL
# SBATCH --mail-user=minghao.wu@monash.edu
#SBATCH --output=/home/minghaow/llamamt-project/logs/%j-%x.out
#SBATCH --error=/home/minghaow/llamamt-project/logs/%j-%x.err

export HF_HOME=/nfsdata/data/minghaow/llamamt-project/cache
module load cuda/12.1.0-gcc-8.5.0-5lkaqss

# for model in meta-llama/Meta-Llama-3-8B ; do
#     for nshots in 0 5 ; do
#         for tgt_lang in all ; do 
#             echo "sbatch -J translate-base-$nshots-$(basename $model)-$tgt_lang /home/minghaow/llamamt-project/llama3_mt/submit_base.sh $nshots $model $tgt_lang"
#             sbatch -J translate-base-$nshots-$(basename $model)-$tgt_lang /home/minghaow/llamamt-project/llama3_mt/submit_base.sh $nshots $model $tgt_lang
#         done
#     done
# done


# for model in meta-llama/Meta-Llama-3-8B-Instruct ; do
#     for nshots in 0 5 ; do
#         for tgt_lang in all ; do 
#             echo "sbatch -J translate-instruct-$nshots-$(basename $model)-$tgt_lang /home/minghaow/llamamt-project/llama3_mt/submit_instruct.sh $nshots $model $tgt_lang"
#             sbatch -J translate-instruct-$nshots-$(basename $model)-$tgt_lang /home/minghaow/llamamt-project/llama3_mt/submit_instruct.sh $nshots $model $tgt_lang
#             # bash /home/minghaow/llamamt-project/llama3_mt/submit_instruct.sh $nshots $model $tgt_lang
#         done
#     done
# done

nshots=5
model_id=meta-llama/Meta-Llama-3-8B-Instruct
tgt_lang=eng_Latn

python run_api.py \
    --model_id $model_id \
    --dataset facebook/flores \
    --tgt_lang $tgt_lang \
    --results_dir /home/minghaow/llamamt-project/llama3_mt/translations/$nshots-shot-instruct/Meta-Llama-3-8B-Instruct \
    --nshots $nshots