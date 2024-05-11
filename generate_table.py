from pytablewriter import MarkdownTableWriter
import json

def read_jsonl(path):
    with open(path, "r") as f:
        return [json.loads(l) for l in f]

zero_base = read_jsonl("/home/minghaow/llamamt-project/llama3_mt/translations/0-shot-base/Meta-Llama-3-8B/results-to-eng_Latn.jsonl")
five_base = read_jsonl("/home/minghaow/llamamt-project/llama3_mt/translations/5-shot-base/Meta-Llama-3-8B/results-to-eng_Latn.jsonl")
zero_instruct = read_jsonl("/home/minghaow/llamamt-project/llama3_mt/translations/0-shot-instruct/Meta-Llama-3-8B-Instruct/results-to-eng_Latn.jsonl")
five_instruct = read_jsonl("/home/minghaow/llamamt-project/llama3_mt/translations/5-shot-instruct/Meta-Llama-3-8B-Instruct/results-to-eng_Latn.jsonl")


lines = []
for z, f, zi, fi in zip(zero_base, five_base, zero_instruct, five_instruct):
    assert z["src_lang"] == f["src_lang"] == zi["src_lang"] == fi["src_lang"]
    assert z["tgt_lang"] == f["tgt_lang"] == zi["tgt_lang"] == fi["tgt_lang"]
    assert z["signature"] == f["signature"] == zi["signature"] == fi["signature"]
    lines.append([z["src_lang"], round(z["score"], 2), round(f["score"], 2), round(zi["score"], 2), round(fi["score"], 2)])
writer = MarkdownTableWriter(
    table_name="8B Model X-English",
    headers=["languages", "0-shot Base", "5-shot Base", "0-shot Instruct", "5-shot Instruct"],
    value_matrix=lines,
)

writer.write_table()