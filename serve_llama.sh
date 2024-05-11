
export HF_HOME=/nfsdata/data/minghaow/llamamt-project/cache

model_id=$1

python -m vllm.entrypoints.openai.api_server \
    --model $model_id \
    --dtype bfloat16 \
    --api-key any_key_you_want \
    --tensor-parallel-size 2 \
    --host 0.0.0.0 \
    --port 10086 \
    --max-model-len 8000 \
    --device auto \
