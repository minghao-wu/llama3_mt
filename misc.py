import json
import glob

def read_jsonl(path):
    with open(path, "r") as f:
        return [json.loads(l) for l in f]

paths = glob.glob("/home/minghaow/llamamt-project/llama3_mt/translations/0-shot-instruct/Meta-Llama-3-70B-Instruct/*to-eng_Latn.jsonl")

good = 0
total = 0
for p in paths:
    print(p)
    if "results" in p:
        continue
    data = read_jsonl(p)
    good += len(data)
    total += 1012
print(good, total, good/total)