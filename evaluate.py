from sacrebleu.metrics import CHRF
import json
import glob
import argparse
from tqdm import tqdm

def read_jsonl(path):
    with open(path, "r") as f:
        return [json.loads(l) for l in f]

def write_jsonl(data, path):
    with open(path, "w") as f:
        for d in data:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")

parser = argparse.ArgumentParser()
parser.add_argument("--results_dir", type=str, required=True)
args = parser.parse_args()


chrf = CHRF(word_order=2)

paths = glob.glob(f"{args.results_dir}/*-to-eng_Latn.jsonl")
print(len(paths))
assert 203 <= len(paths) <= 204
results = []
for path in tqdm(paths):
    if "results" in path:
        continue
    data = read_jsonl(path)
    print(path, len((data)))
    assert len(data) >= 1010
    refs = [[d["ref_text"] for d in data]]
    hyps = [d["hyp_text"] for d in data]
    try:
        assert hyps
    except:
        print(path)
    score = chrf.corpus_score(hyps, refs)

    dic = {
        "src_lang": data[0]["src_lang"],
        "tgt_lang": data[0]["tgt_lang"],
        "model_id": data[0]["model_id"],
        "score": score.score,
        "signature": str(chrf.get_signature()),
    }
    results.append(dic)

write_jsonl(results, f"{args.results_dir}/results-to-eng_Latn.jsonl")