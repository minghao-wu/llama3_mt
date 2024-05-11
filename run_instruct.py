from datasets import load_dataset
from vllm import LLM, SamplingParams
import os
import uuid
import huggingface_hub
import json
import argparse

huggingface_hub.login(token="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")

text = """
Acehnese (Arabic script) | ace_Arab
Acehnese (Latin script) | ace_Latn
Mesopotamian Arabic | acm_Arab
Ta’izzi-Adeni Arabic | acq_Arab
Tunisian Arabic | aeb_Arab
Afrikaans | afr_Latn
South Levantine Arabic | ajp_Arab
Akan | aka_Latn
Amharic | amh_Ethi
North Levantine Arabic | apc_Arab
Modern Standard Arabic | arb_Arab
Modern Standard Arabic (Romanized) | arb_Latn
Najdi Arabic | ars_Arab
Moroccan Arabic | ary_Arab
Egyptian Arabic | arz_Arab
Assamese | asm_Beng
Asturian | ast_Latn
Awadhi | awa_Deva
Central Aymara | ayr_Latn
South Azerbaijani | azb_Arab
North Azerbaijani | azj_Latn
Bashkir | bak_Cyrl
Bambara | bam_Latn
Balinese | ban_Latn
Belarusian | bel_Cyrl
Bemba | bem_Latn
Bengali | ben_Beng
Bhojpuri | bho_Deva
Banjar (Arabic script) | bjn_Arab
Banjar (Latin script) | bjn_Latn
Standard Tibetan | bod_Tibt
Bosnian | bos_Latn
Buginese | bug_Latn
Bulgarian | bul_Cyrl
Catalan | cat_Latn
Cebuano | ceb_Latn
Czech | ces_Latn
Chokwe | cjk_Latn
Central Kurdish | ckb_Arab
Crimean Tatar | crh_Latn
Welsh | cym_Latn
Danish | dan_Latn
German | deu_Latn
Southwestern Dinka | dik_Latn
Dyula | dyu_Latn
Dzongkha | dzo_Tibt
Greek | ell_Grek
English | eng_Latn
Esperanto | epo_Latn
Estonian | est_Latn
Basque | eus_Latn
Ewe | ewe_Latn
Faroese | fao_Latn
Fijian | fij_Latn
Finnish | fin_Latn
Fon | fon_Latn
French | fra_Latn
Friulian | fur_Latn
Nigerian Fulfulde | fuv_Latn
Scottish Gaelic | gla_Latn
Irish | gle_Latn
Galician | glg_Latn
Guarani | grn_Latn
Gujarati | guj_Gujr
Haitian Creole | hat_Latn
Hausa | hau_Latn
Hebrew | heb_Hebr
Hindi | hin_Deva
Chhattisgarhi | hne_Deva
Croatian | hrv_Latn
Hungarian | hun_Latn
Armenian | hye_Armn
Igbo | ibo_Latn
Ilocano | ilo_Latn
Indonesian | ind_Latn
Icelandic | isl_Latn
Italian | ita_Latn
Javanese | jav_Latn
Japanese | jpn_Jpan
Kabyle | kab_Latn
Jingpho | kac_Latn
Kamba | kam_Latn
Kannada | kan_Knda
Kashmiri (Arabic script) | kas_Arab
Kashmiri (Devanagari script) | kas_Deva
Georgian | kat_Geor
Central Kanuri (Arabic script) | knc_Arab
Central Kanuri (Latin script) | knc_Latn
Kazakh | kaz_Cyrl
Kabiyè | kbp_Latn
Kabuverdianu | kea_Latn
Khmer | khm_Khmr
Kikuyu | kik_Latn
Kinyarwanda | kin_Latn
Kyrgyz | kir_Cyrl
Kimbundu | kmb_Latn
Northern Kurdish | kmr_Latn
Kikongo | kon_Latn
Korean | kor_Hang
Lao | lao_Laoo
Ligurian | lij_Latn
Limburgish | lim_Latn
Lingala | lin_Latn
Lithuanian | lit_Latn
Lombard | lmo_Latn
Latgalian | ltg_Latn
Luxembourgish | ltz_Latn
Luba-Kasai | lua_Latn
Ganda | lug_Latn
Luo | luo_Latn
Mizo | lus_Latn
Standard Latvian | lvs_Latn
Magahi | mag_Deva
Maithili | mai_Deva
Malayalam | mal_Mlym
Marathi | mar_Deva
Minangkabau (Arabic script) | min_Arab
Minangkabau (Latin script) | min_Latn
Macedonian | mkd_Cyrl
Plateau Malagasy | plt_Latn
Maltese | mlt_Latn
Meitei (Bengali script) | mni_Beng
Halh Mongolian | khk_Cyrl
Mossi | mos_Latn
Maori | mri_Latn
Burmese | mya_Mymr
Dutch | nld_Latn
Norwegian Nynorsk | nno_Latn
Norwegian Bokmål | nob_Latn
Nepali | npi_Deva
Northern Sotho | nso_Latn
Nuer | nus_Latn
Nyanja | nya_Latn
Occitan | oci_Latn
West Central Oromo | gaz_Latn
Odia | ory_Orya
Pangasinan | pag_Latn
Eastern Panjabi | pan_Guru
Papiamento | pap_Latn
Western Persian | pes_Arab
Polish | pol_Latn
Portuguese | por_Latn
Dari | prs_Arab
Southern Pashto | pbt_Arab
Ayacucho Quechua | quy_Latn
Romanian | ron_Latn
Rundi | run_Latn
Russian | rus_Cyrl
Sango | sag_Latn
Sanskrit | san_Deva
Santali | sat_Olck
Sicilian | scn_Latn
Shan | shn_Mymr
Sinhala | sin_Sinh
Slovak | slk_Latn
Slovenian | slv_Latn
Samoan | smo_Latn
Shona | sna_Latn
Sindhi | snd_Arab
Somali | som_Latn
Southern Sotho | sot_Latn
Spanish | spa_Latn
Tosk Albanian | als_Latn
Sardinian | srd_Latn
Serbian | srp_Cyrl
Swati | ssw_Latn
Sundanese | sun_Latn
Swedish | swe_Latn
Swahili | swh_Latn
Silesian | szl_Latn
Tamil | tam_Taml
Tatar | tat_Cyrl
Telugu | tel_Telu
Tajik | tgk_Cyrl
Tagalog | tgl_Latn
Thai | tha_Thai
Tigrinya | tir_Ethi
Tamasheq (Latin script) | taq_Latn
Tamasheq (Tifinagh script) | taq_Tfng
Tok Pisin | tpi_Latn
Tswana | tsn_Latn
Tsonga | tso_Latn
Turkmen | tuk_Latn
Tumbuka | tum_Latn
Turkish | tur_Latn
Twi | twi_Latn
Central Atlas Tamazight | tzm_Tfng
Uyghur | uig_Arab
Ukrainian | ukr_Cyrl
Umbundu | umb_Latn
Urdu | urd_Arab
Northern Uzbek | uzn_Latn
Venetian | vec_Latn
Vietnamese | vie_Latn
Waray | war_Latn
Wolof | wol_Latn
Xhosa | xho_Latn
Eastern Yiddish | ydd_Hebr
Yoruba | yor_Latn
Yue Chinese | yue_Hant
Chinese (Simplified) | zho_Hans
Chinese (Traditional) | zho_Hant
Standard Malay | zsm_Latn
Zulu | zul_Latn
"""
text = text.strip().split("\n")

language_map = {}
for line in text:
    lang, code = line.split(" | ")
    language_map[code] = lang

def format_base_model_sentence_pair(src_lang, tgt_lang, src_sent, tgt_sent=None):
    if tgt_sent:
        tgt_text = json.dumps({"translation": tgt_sent}, ensure_ascii=False)
        return f"[{src_lang}]: {src_sent}\n[{tgt_lang}]: {tgt_text}\n\n"
    else:
        return f"Translate the following sentence from {src_lang} to {tgt_lang}:\n[{src_lang}]: {src_sent}\n[{tgt_lang}]:"

def wrap_chat_template(llm, prompt):
    text = llm.llm_engine.tokenizer.tokenizer.apply_chat_template(
        [
            {"role": "system", "content": 'You are an accurate translator. You MUST answer with the following JSON scheme: {"translation": string}'},
            {"role": "user", "content": prompt}
        ], 
        tokenize=False, 
        add_generation_template=True
    )
    return text

def read_jsonl(path):
    with open(path, "r") as f:
        return [json.loads(l) for l in f]

def write_jsonl(lst, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    if os.path.exists(path):
        exist_data = read_jsonl(path)
        lst = exist_data + lst
    
    print(f"Writing {len(lst)} / 1012 examples to {path}")
    with open(path, "w") as f:
        for item in lst:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")



def sample_in_context_examples(nshots, data, src_lang, tgt_lang):
    data = data.shuffle(seed=42)
    data = data.select(range(nshots))

    src_sents = data[f"sentence_{src_lang}"][:nshots]
    tgt_sents = data[f"sentence_{tgt_lang}"][:nshots]
    prefix = ""
    for s, t in zip(src_sents, tgt_sents):
        prefix += format_base_model_sentence_pair(language_map[src_lang], language_map[tgt_lang], s, t)
    return prefix

parser = argparse.ArgumentParser()
parser.add_argument("--model_id", type=str, required=True)
parser.add_argument("--dataset", type=str, required=True)
parser.add_argument("--tgt_lang", type=str, required=True)
parser.add_argument("--results_dir", type=str, required=True)
parser.add_argument("--nshots", type=int, required=True)
args = parser.parse_args()
print(args)

results_dir = args.results_dir
model_id = args.model_id
results_dir = os.path.join(args.results_dir, os.path.basename(model_id))
sampling_params = SamplingParams(
    temperature=0.6, top_p=0.9, max_tokens=2048
)
llm = LLM(model=model_id, tensor_parallel_size=2, max_model_len=4096)
data = load_dataset(args.dataset, "all")

count = 0
for k, v in language_map.items():
    print("==============================")
    print(f"Translating {count} / 203")
    count += 1
    if args.tgt_lang == "all":
        src_lang = "eng_Latn"
        tgt_lang = k
    elif args.tgt_lang == "eng_Latn":
        src_lang = k
        tgt_lang = "eng_Latn"
    else:
        raise ValueError("tgt_lang must be 'all' or 'eng_Latn'")

    if src_lang == tgt_lang:
        continue

    output_path = os.path.join(results_dir, f"{src_lang}-to-{tgt_lang}.jsonl")

    if os.path.exists(output_path):
        exist_translation = read_jsonl(output_path)
        print(f"Existing translations: {len(exist_translation)} / 1012 examples for {src_lang} to {tgt_lang}")
        exist_src_sents = [d["src_text"] for d in exist_translation]
    
    src_sents = []
    tgt_sents = []
    for d in data["devtest"]:
        if d[f"sentence_{src_lang}"] not in exist_src_sents:
            src_sents.append(d[f"sentence_{src_lang}"])
            tgt_sents.append(d[f"sentence_{tgt_lang}"])
    if len(src_sents) == 0:
        print(f"No new examples for {src_lang} to {tgt_lang}")
        continue
    else:
        print(f"Translating {len(src_sents)} examples from {src_lang} to {tgt_lang}")

    if args.nshots == 0:
        prompts = [format_base_model_sentence_pair(language_map[src_lang], language_map[tgt_lang], src_sent, None) for src_sent, tgt_sent in zip(src_sents, tgt_sents)]
    else:
        prefix = sample_in_context_examples(args.nshots, data["dev"], src_lang, tgt_lang)
        prompts = [prefix+format_base_model_sentence_pair(language_map[src_lang], language_map[tgt_lang], src_sent, None) for src_sent, tgt_sent in zip(src_sents, tgt_sents)]
    prompts = [wrap_chat_template(llm, p) for p in prompts]

    outputs = llm.generate(prompts, sampling_params)
    results = []
    for src, ref, out, prompt in zip(src_sents, tgt_sents, outputs, prompts):
        generated_text = out.outputs[0].text
        translation_json = generated_text.replace("<|start_header_id|>assistant<|end_header_id|>", "").strip()
        try:
            dic = {
                "id": str(uuid.uuid4()),
                "model_id": model_id,
                "src_lang": src_lang,
                "tgt_lang": tgt_lang,
                "src_text": src,
                "ref_text": ref,
                "hyp_text": json.loads(translation_json)["translation"],
                "prompt": prompt,
                "generated_text": generated_text
            }
            results.append(dic)
        except:
            continue
    write_jsonl(results, output_path)