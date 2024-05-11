# Evaluating the Machine Translation Capability of Llama-3 Models

In this project, we evaluate the machine translation capabilities of [Llama-3 models](https://huggingface.co/collections/meta-llama/meta-llama-3-66214712577ca38149ebb2b6) using the [facebook/flores](https://huggingface.co/datasets/facebook/flores) dataset. We assess these models in zero-shot and five-shot settings. Additionally, we evaluate the models in a selective translation setting, where the model is required to translate only part of the source text.

**NOTE: The results might not be valid because the Flores-200 dataset likely leaked into the training set of the Llama-3 models.**

## Setup
```
datasets==2.19.1
flash-attn==2.5.8
transformers==4.40.2
vllm==0.4.1
sacrebleu==2.4.2
torch==2.2.1
pytablewriter==1.2.0
```
## Generate Your Own Translations
To translate with the base models, you can run
```
python run_base.py \
    --model_id meta-llama/Meta-Llama-3-70B \
    --results_dir <YOU_OUTPUT_DIR> \
    --nshots <NUM_SHOTS>
```
To translate with the instruct models, you can run
```
python run_instruct.py \
    --model_id meta-llama/Meta-Llama-3-8B-Instruct \
    --results_dir <YOU_OUTPUT_DIR> \
    --nshots <NUM_SHOTS>
```
**NOTE: The source and target languages are hard-coded in the program. You need to modify them yourself.**

## Results
We run evaluations on [facebook/flores](https://huggingface.co/datasets/facebook/flores). The translations are evaluated using `chrF++` with the signature of `nrefs:1|case:mixed|eff:yes|nc:6|nw:2|space:no|version:2.4.2`. The raw translations can be found under the folder `translations`.

**NOTE: We require the instruct models to generate translations using the JSON schema `{"translation": "string"}`. Pass@1 indicates the success rate of the instruct model on its first attempt to generate the required JSON string.**

* [8B Model X-English](#8b-model-x-english)
* [8B Model English-X](#8b-model-english-x)
* [70B Model X-English](#70b-model-x-english)
* [70B Model English-X](#70b-model-english-x)


### 8B Model X-English

|languages|0-shot Base|5-shot Base|0-shot Instruct|5-shot Instruct|
|---------|----------:|----------:|--------------:|--------------:|
|ace_Arab |      11.16|      20.78|          20.69|          22.51|
|ace_Latn |      24.22|      33.79|          31.25|          34.52|
|acm_Arab |      54.05|      54.57|          52.44|          54.03|
|acq_Arab |      55.52|      56.25|          54.29|          55.88|
|aeb_Arab |      48.31|      51.12|          48.52|          49.93|
|afr_Latn |      71.14|      73.14|          69.74|          71.46|
|ajp_Arab |      56.75|      59.44|          54.80|          57.03|
|aka_Latn |      19.32|      28.98|          27.19|          29.05|
|amh_Ethi |      22.14|      29.81|          23.51|          24.77|
|apc_Arab |      54.38|      56.81|          52.36|          54.67|
|arb_Arab |      59.41|      60.67|          57.76|          59.24|
|arb_Latn |      25.68|      33.25|          31.73|          33.37|
|ars_Arab |      58.34|      60.00|          56.82|          58.45|
|ary_Arab |      46.01|      48.94|          45.40|          47.57|
|arz_Arab |      51.66|      53.66|          50.31|          52.23|
|asm_Beng |      40.95|      45.35|          40.64|          44.07|
|ast_Latn |      59.61|      61.72|          59.35|          61.11|
|awa_Deva |      45.18|      53.26|          48.41|          51.16|
|ayr_Latn |      12.01|      20.06|          21.94|          24.47|
|azb_Arab |      25.52|      35.31|          33.22|          35.92|
|azj_Latn |      44.55|      47.37|          44.81|          46.30|
|bak_Cyrl |      43.66|      48.12|          43.66|          46.60|
|bam_Latn |      14.85|      21.95|          22.43|          24.21|
|ban_Latn |      41.55|      44.55|          40.57|          43.70|
|bel_Cyrl |      47.62|      49.93|          47.16|          48.44|
|bem_Latn |      15.15|      24.46|          26.26|          28.03|
|ben_Beng |      51.03|      52.60|          49.90|          51.88|
|bho_Deva |      41.93|      47.77|          43.35|          45.94|
|bjn_Arab |      10.98|      19.41|          19.71|          22.61|
|bjn_Latn |      43.24|      49.66|          42.79|          47.89|
|bod_Tibt |      15.78|      25.01|          22.45|          23.54|
|bos_Latn |      61.90|      63.77|          61.11|          62.35|
|bug_Latn |      20.86|      29.10|          27.85|          31.11|
|bul_Cyrl |      61.12|      62.92|          61.20|          62.05|
|cat_Latn |      64.65|      66.87|          65.29|          66.17|
|ceb_Latn |      51.68|      55.97|          51.01|          53.97|
|ces_Latn |      60.93|      61.64|          61.22|          61.85|
|cjk_Latn |      14.64|      21.06|          23.11|          25.39|
|ckb_Arab |      42.05|      44.20|          39.97|          42.33|
|crh_Latn |      37.88|      44.11|          39.90|          43.05|
|cym_Latn |      65.13|      67.27|          60.77|          63.32|
|dan_Latn |      66.81|      68.40|          66.57|          67.32|
|deu_Latn |      63.78|      65.23|          64.44|          64.73|
|dik_Latn |      15.03|      21.03|          21.67|          25.32|
|dyu_Latn |      12.52|      20.99|          22.22|          24.15|
|dzo_Tibt |      13.30|      21.85|          20.63|          21.41|
|ell_Grek |      57.56|      58.82|          57.35|          58.10|
|epo_Latn |      61.99|      64.99|          61.54|          63.56|
|est_Latn |      54.58|      56.21|          54.34|          55.01|
|eus_Latn |      48.90|      51.86|          47.18|          49.64|
|ewe_Latn |      14.60|      21.52|          21.89|          24.27|
|fao_Latn |      47.64|      52.02|          44.99|          48.62|
|fij_Latn |      19.28|      25.05|          25.34|          26.86|
|fin_Latn |      56.12|      57.01|          55.27|          56.28|
|fon_Latn |      11.46|      19.22|          21.44|          23.28|
|fra_Latn |      64.94|      66.30|          65.03|          65.54|
|fur_Latn |      53.08|      58.68|          50.97|          56.25|
|fuv_Latn |      14.42|      22.33|          22.01|          24.70|
|gla_Latn |      44.51|      46.69|          40.05|          42.74|
|gle_Latn |      52.28|      55.10|          48.56|          50.97|
|glg_Latn |      62.34|      63.70|          62.16|          62.93|
|grn_Latn |      22.68|      29.43|          29.02|          31.82|
|guj_Gujr |      47.04|      52.03|          47.48|          49.55|
|hat_Latn |      47.50|      51.11|          43.75|          47.06|
|hau_Latn |      38.64|      42.87|          37.01|          40.23|
|heb_Hebr |      59.29|      62.38|          58.68|          60.19|
|hin_Deva |      56.52|      58.89|          55.78|          57.14|
|hne_Deva |      44.25|      51.18|          45.94|          49.26|
|hrv_Latn |      58.91|      60.36|          58.67|          59.35|
|hun_Latn |      56.84|      58.32|          56.39|          57.07|
|hye_Armn |      55.69|      57.43|          54.81|          55.72|
|ibo_Latn |      32.16|      38.88|          31.21|          35.69|
|ilo_Latn |      38.89|      44.82|          40.18|          44.02|
|ind_Latn |      62.54|      64.30|          61.49|          62.84|
|isl_Latn |      50.27|      52.60|          48.11|          49.84|
|ita_Latn |      58.42|      59.33|          58.68|          59.01|
|jav_Latn |      49.18|      53.55|          46.38|          50.19|
|jpn_Jpan |      49.40|      52.45|          49.49|          51.33|
|kab_Latn |      13.31|      20.38|          20.67|          23.13|
|kac_Latn |      10.78|      22.04|          21.92|          25.20|
|kam_Latn |      16.52|      23.77|          24.18|          25.90|
|kan_Knda |      48.53|      49.99|          44.72|          47.02|
|kas_Arab |      21.17|      34.39|          29.80|          34.48|
|kas_Deva |      17.85|      30.07|          26.53|          30.34|
|kat_Geor |      47.16|      49.48|          46.46|          47.59|
|knc_Arab |       7.10|      14.98|          16.43|          19.70|
|knc_Latn |      11.50|      22.28|          23.30|          26.04|
|kaz_Cyrl |      44.42|      50.71|          45.70|          48.41|
|kbp_Latn |      13.97|      22.22|          22.24|          24.04|
|kea_Latn |      46.32|      55.53|          46.62|          52.69|
|khm_Khmr |      39.02|      44.93|          36.88|          38.33|
|kik_Latn |      18.62|      26.13|          25.87|          27.65|
|kin_Latn |      26.97|      31.56|          30.66|          32.68|
|kir_Cyrl |      37.49|      42.15|          39.22|          41.73|
|kmb_Latn |      12.37|      21.86|          23.05|          25.28|
|kmr_Latn |      35.47|      38.27|          35.16|          38.22|
|kon_Latn |      18.93|      26.27|          26.09|          28.40|
|kor_Hang |      50.98|      52.04|          49.73|          51.27|
|lao_Laoo |      27.79|      34.19|          27.64|          28.31|
|lij_Latn |      52.17|      58.37|          51.95|          57.20|
|lim_Latn |      54.54|      58.99|          52.92|          56.87|
|lin_Latn |      20.35|      28.12|          26.13|          28.84|
|lit_Latn |      52.52|      53.82|          51.63|          52.75|
|lmo_Latn |      50.81|      55.39|          49.92|          54.15|
|ltg_Latn |      30.52|      37.65|          33.08|          36.66|
|ltz_Latn |      57.11|      60.95|          55.35|          57.51|
|lua_Latn |      14.39|      23.74|          24.96|          27.53|
|lug_Latn |      19.58|      26.38|          25.08|          27.76|
|luo_Latn |      13.58|      22.60|          23.20|          25.88|
|lus_Latn |      26.23|      30.12|          29.59|          31.95|
|lvs_Latn |      53.46|      56.32|          53.45|          54.62|
|mag_Deva |      48.02|      55.90|          50.48|          52.79|
|mai_Deva |      44.36|      53.48|          45.81|          50.06|
|mal_Mlym |      47.07|      50.77|          46.43|          48.48|
|mar_Deva |      47.31|      51.91|          47.85|          50.09|
|min_Arab |      10.10|      17.11|          19.86|          22.21|
|min_Latn |      45.41|      51.28|          42.16|          47.97|
|mkd_Cyrl |      61.09|      63.29|          60.60|          62.28|
|plt_Latn |      25.40|      33.31|          30.51|          32.93|
|mlt_Latn |      63.52|      66.82|          60.13|          62.71|
|mni_Beng |       9.12|      21.58|          19.54|          24.49|
|khk_Cyrl |      33.33|      40.56|          35.35|          39.06|
|mos_Latn |      12.89|      21.01|          21.68|          24.15|
|mri_Latn |      32.92|      37.61|          33.24|          35.73|
|mya_Mymr |      32.92|      39.21|          31.79|          34.29|
|nld_Latn |      55.92|      56.94|          56.22|          56.93|
|nno_Latn |      63.69|      65.36|          63.31|          64.37|
|nob_Latn |      63.35|      64.40|          63.20|          63.68|
|npi_Deva |      48.71|      53.96|          47.87|          51.38|
|nso_Latn |      22.16|      28.51|          27.26|          29.55|
|nus_Latn |       9.51|      17.51|          19.54|          22.14|
|nya_Latn |      22.68|      28.86|          27.60|          30.59|
|oci_Latn |      68.46|      70.45|          67.11|          68.97|
|gaz_Latn |      13.20|      21.74|          20.77|          23.27|
|ory_Orya |      43.90|      47.63|          41.70|          44.59|
|pag_Latn |      32.71|      38.69|          36.08|          38.61|
|pan_Guru |      49.84|      52.31|          46.43|          49.49|
|pap_Latn |      53.97|      61.84|          52.94|          59.07|
|pes_Arab |      56.79|      58.37|          55.77|          57.14|
|pol_Latn |      53.18|      55.02|          53.69|          54.40|
|por_Latn |      68.23|      69.75|          68.44|          68.78|
|prs_Arab |      52.39|      57.38|          54.93|          56.45|
|pbt_Arab |      41.71|      46.89|          41.31|          45.39|
|quy_Latn |      16.42|      24.93|          24.98|          27.55|
|ron_Latn |      63.82|      64.97|          63.61|          64.15|
|run_Latn |      23.11|      27.69|          26.28|          29.10|
|rus_Cyrl |      57.60|      59.47|          58.49|          58.83|
|sag_Latn |      12.55|      21.10|          23.20|          25.19|
|san_Deva |      30.73|      39.53|          35.80|          39.51|
|sat_Olck |      15.56|      22.20|          20.49|          21.19|
|scn_Latn |      52.12|      55.73|          50.95|          54.09|
|shn_Mymr |      17.00|      29.78|          24.72|          27.38|
|sin_Sinh |      39.94|      44.21|          39.53|          41.86|
|slk_Latn |      58.24|      60.50|          59.13|          60.00|
|slv_Latn |      56.02|      57.69|          55.32|          56.38|
|smo_Latn |      27.05|      33.63|          29.96|          32.13|
|sna_Latn |      21.52|      28.18|          27.58|          29.80|
|snd_Arab |      39.94|      48.94|          39.85|          45.01|
|som_Latn |      21.51|      30.77|          28.63|          30.23|
|sot_Latn |      20.57|      27.62|          26.97|          28.98|
|spa_Latn |      56.16|      57.84|          56.33|          57.49|
|als_Latn |      58.56|      61.13|          57.68|          59.14|
|srd_Latn |      54.61|      57.75|          53.48|          57.25|
|srp_Cyrl |      62.57|      64.67|          62.09|          63.22|
|ssw_Latn |      20.09|      25.83|          25.67|          28.43|
|sun_Latn |      45.98|      50.55|          44.47|          48.39|
|swe_Latn |      66.44|      67.87|          66.62|          67.11|
|swh_Latn |      53.62|      56.70|          52.03|          54.43|
|szl_Latn |      51.47|      56.88|          50.54|          53.72|
|tam_Taml |      44.65|      48.96|          42.52|          44.97|
|tat_Cyrl |      42.75|      48.60|          43.78|          47.53|
|tel_Telu |      47.66|      53.62|          48.22|          50.36|
|tgk_Cyrl |      44.08|      48.17|          42.28|          46.48|
|tgl_Latn |      61.09|      62.82|          58.66|          60.36|
|tha_Thai |      51.71|      54.46|          51.21|          53.04|
|tir_Ethi |      12.34|      19.71|          19.47|          21.00|
|taq_Latn |      12.67|      21.38|          22.69|          25.19|
|taq_Tfng |       5.44|      16.28|          17.88|          19.22|
|tpi_Latn |      40.79|      44.81|          40.36|          43.85|
|tsn_Latn |      20.68|      26.94|          26.73|          28.30|
|tso_Latn |      19.68|      24.68|          25.02|          27.09|
|tuk_Latn |      33.08|      40.57|          36.60|          39.64|
|tum_Latn |      17.98|      26.20|          26.39|          28.17|
|tur_Latn |      56.37|      57.97|          56.28|          57.17|
|twi_Latn |      22.14|      28.58|          27.25|          29.40|
|tzm_Tfng |       6.99|      15.96|          17.36|          19.20|
|uig_Arab |      34.26|      39.57|          34.81|          38.02|
|ukr_Cyrl |      60.03|      61.79|          59.88|          60.68|
|umb_Latn |      12.83|      20.47|          21.91|          24.35|
|urd_Arab |      49.08|      53.16|          49.38|          51.90|
|uzn_Latn |      47.16|      50.46|          46.69|          49.81|
|vec_Latn |      58.10|      62.50|          57.06|          60.46|
|vie_Latn |      56.65|      57.69|          56.03|          56.80|
|war_Latn |      51.52|      57.14|          49.03|          54.09|
|wol_Latn |      16.34|      23.81|          24.09|          26.62|
|xho_Latn |      24.72|      31.60|          29.19|          32.27|
|ydd_Hebr |      54.31|      61.30|          51.86|          56.74|
|yor_Latn |      20.63|      27.40|          26.45|          28.56|
|yue_Hant |      51.95|      53.83|          51.39|          52.99|
|zho_Hans |      52.00|      53.60|          51.52|          52.90|
|zho_Hant |      50.76|      52.36|          50.10|          51.48|
|zsm_Latn |      61.81|      63.68|          60.43|          62.11|
|zul_Latn |      23.83|      29.61|          29.22|          32.32|

### 8B Model English-X


### 70B Model X-English


### 70B Model English-X

