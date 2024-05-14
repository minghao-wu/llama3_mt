from pytablewriter import MarkdownTableWriter
import json

chatgpt = {'ace_Arab': 3.35, 'ace_Latn': 10.12, 'acm_Arab': 27.78, 'acq_Arab': 29.45, 'aeb_Arab': 24.38, 'afr_Latn': 53.62, 'ajp_Arab': 33.45, 'aka_Latn': 7.87, 'als_Latn': 33.73, 'amh_Ethi': 4.1, 'apc_Arab': 29.7, 'arb_Arab': 33.3, 'ars_Arab': 32.31, 'ary_Arab': 21.67, 'arz_Arab': 25.54, 'asm_Beng': 12.09, 'ast_Latn': 36.22, 'awa_Deva': 19.51, 'ayr_Latn': 4.49, 'azb_Arab': 8.37, 'azj_Latn': 16.96, 'bak_Cyrl': 8.63, 'bam_Latn': 4.85, 'ban_Latn': 17.36, 'bel_Cyrl': 17.05, 'bem_Latn': 7.84, 'ben_Beng': 20.66, 'bho_Deva': 14.9, 'bjn_Arab': 4.12, 'bjn_Latn': 19.12, 'bod_Tibt': 2.22, 'bos_Latn': 38.22, 'bug_Latn': 7.43, 'bul_Cyrl': 35.84, 'cat_Latn': 42.42, 'ceb_Latn': 31.85, 'ces_Latn': 36.18, 'cjk_Latn': 4.81, 'ckb_Arab': 8.98, 'crh_Latn': 18.32, 'cym_Latn': 45.9, 'dan_Latn': 45.39, 'deu_Latn': 40.51, 'dik_Latn': 5.14, 'dyu_Latn': 3.93, 'dzo_Tibt': 1.79, 'ell_Grek': 30.53, 'epo_Latn': 37.6, 'est_Latn': 33.66, 'eus_Latn': 21.1, 'ewe_Latn': 4.64, 'fao_Latn': 29.33, 'fij_Latn': 9.21, 'fin_Latn': 31.07, 'fon_Latn': 3.59, 'fra_Latn': 42.02, 'fur_Latn': 29.28, 'fuv_Latn': 4.79, 'gaz_Latn': 4.54, 'gla_Latn': 21.09, 'gle_Latn': 28.53, 'glg_Latn': 37.42, 'grn_Latn': 7.43, 'guj_Gujr': 19.97, 'hat_Latn': 28.12, 'hau_Latn': 9.98, 'heb_Hebr': 34.75, 'hin_Deva': 27.76, 'hne_Deva': 18.31, 'hrv_Latn': 33.9, 'hun_Latn': 31.08, 'hye_Armn': 15.75, 'ibo_Latn': 6.98, 'ilo_Latn': 16.95, 'ind_Latn': 37.62, 'isl_Latn': 28.66, 'ita_Latn': 30.12, 'jav_Latn': 22.78, 'jpn_Jpan': 22.87, 'kab_Latn': 4.56, 'kac_Latn': 3.78, 'kam_Latn': 6.42, 'kan_Knda': 18.13, 'kas_Arab': 7.56, 'kas_Deva': 7.18, 'kat_Geor': 12.51, 'kaz_Cyrl': 15.35, 'kbp_Latn': 3.86, 'kea_Latn': 35.17, 'khk_Cyrl': 9.43, 'khm_Khmr': 10.09, 'kik_Latn': 6.66, 'kin_Latn': 12.5, 'kir_Cyrl': 9.53, 'kmb_Latn': 5.24, 'kmr_Latn': 14.87, 'knc_Arab': 2.54, 'knc_Latn': 5.04, 'kon_Latn': 5.82, 'kor_Hang': 23.65, 'lao_Laoo': 7.64, 'lij_Latn': 29.7, 'lim_Latn': 35.97, 'lin_Latn': 8.4, 'lit_Latn': 28.36, 'lmo_Latn': 28.16, 'ltg_Latn': 12.63, 'ltz_Latn': 35.99, 'lua_Latn': 6.45, 'lug_Latn': 7.92, 'luo_Latn': 4.66, 'lus_Latn': 7.74, 'lvs_Latn': 30.24, 'mag_Deva': 21.31, 'mai_Deva': 15.98, 'mal_Mlym': 16.31, 'mar_Deva': 18.5, 'min_Latn': 17.83, 'mkd_Cyrl': 35.93, 'mlt_Latn': 38.24, 'mni_Beng': 3.35, 'mos_Latn': 4.07, 'mri_Latn': 16.36, 'mya_Mymr': 3.52, 'nld_Latn': 28.29, 'nno_Latn': 42.43, 'nob_Latn': 39.44, 'npi_Deva': 20.99, 'nso_Latn': 10.61, 'nus_Latn': 3.61, 'nya_Latn': 11.86, 'oci_Latn': 45.6, 'ory_Orya': 14.19, 'pag_Latn': 14.93, 'pan_Guru': 21.52, 'pap_Latn': 39.13, 'pbt_Arab': 9.16, 'pes_Arab': 29.21, 'plt_Latn': 13.4, 'pol_Latn': 26.05, 'por_Latn': 45.32, 'prs_Arab': 29.57, 'quy_Latn': 5.16, 'ron_Latn': 38.9, 'run_Latn': 8.75, 'rus_Cyrl': 31.17, 'sag_Latn': 4.27, 'san_Deva': 10.26, 'scn_Latn': 29.03, 'shn_Mymr': 4.17, 'sin_Sinh': 4.48, 'slk_Latn': 34.61, 'slv_Latn': 31.91, 'smo_Latn': 12.9, 'sna_Latn': 10.22, 'snd_Arab': 11.4, 'som_Latn': 11.78, 'sot_Latn': 10.85, 'spa_Latn': 27.1, 'srd_Latn': 29.21, 'srp_Cyrl': 38.67, 'ssw_Latn': 9.08, 'sun_Latn': 20.81, 'swe_Latn': 44.43, 'swh_Latn': 36.36, 'szl_Latn': 30.86, 'tam_Taml': 12.73, 'taq_Latn': 5.11, 'taq_Tfng': 2.42, 'tat_Cyrl': 10.59, 'tel_Telu': 15.88, 'tgk_Cyrl': 14.1, 'tgl_Latn': 37.25, 'tha_Thai': 20.48, 'tir_Ethi': 2.58, 'tpi_Latn': 16.99, 'tsn_Latn': 9.52, 'tso_Latn': 10.03, 'tuk_Latn': 13.67, 'tum_Latn': 7.19, 'tur_Latn': 33.03, 'twi_Latn': 7.81, 'tzm_Tfng': 2.52, 'uig_Arab': 8.05, 'ukr_Cyrl': 33.9, 'umb_Latn': 4.78, 'urd_Arab': 22.6, 'uzn_Latn': 17.65, 'vec_Latn': 35.76, 'vie_Latn': 29.38, 'war_Latn': 31.18, 'wol_Latn': 6.09, 'xho_Latn': 14.82, 'ydd_Hebr': 20.34, 'yor_Latn': 7.98, 'yue_Hant': 24.66, 'zho_Hans': 23.8, 'zho_Hant': 22.75, 'zsm_Latn': 37.47, 'zul_Latn': 14.61}

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
    gpt_score = chatgpt[z["src_lang"]] if z["src_lang"] in chatgpt else "NA"
    lines.append([z["src_lang"], round(z["score"], 2), round(f["score"], 2), round(zi["score"], 2), round(fi["score"], 2), gpt_score])
writer = MarkdownTableWriter(
    table_name="8B Model X-English",
    headers=["languages", "0-shot Base", "5-shot Base", "0-shot Instruct", "5-shot Instruct", "0-shot gpt-3.5-turbo"],
    value_matrix=lines,
)

writer.write_table()