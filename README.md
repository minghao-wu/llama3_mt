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

**NOTE: We require the instruct models to generate translations using the JSON schema `{"translation": "string"}`. Pass@1 indicates the success rate of the model on its first attempt to generate the required JSON string.**

* [8B Model X-English](#8b-model-x-english)
* [8B Model English-X](#8b-model-english-x)
* [70B Model X-English](#70b-model-x-english)
* [70B Model English-X](#70b-model-english-x)
* [Selective Translation](#selective-translation)


### 8B Model X-English
|languages|0-shot Base|5-shot Base|0-shot Instruct|0-shot Pass@1|5-shot Instruct|5-shot Pass@1|
|---------|----------:|----------:|--------------:|------------:|--------------:|------------:|
|ace_Arab |      11.16|      20.78|          20.69|        95.65|          22.51|        97.04|
|ace_Latn |      24.22|      33.79|          31.25|        99.01|          34.52|        99.41|
|acm_Arab |      54.05|      54.57|          52.44|        98.91|          54.03|        99.51|
|acq_Arab |      55.52|      56.25|          54.29|        98.91|          55.88|        99.51|
|aeb_Arab |      48.31|      51.12|          48.52|        99.01|          49.93|        99.21|
|afr_Latn |      71.14|      73.14|          69.74|        99.01|          71.46|        99.31|
|ajp_Arab |      56.75|      59.44|          54.80|        99.21|          57.03|        99.41|
|aka_Latn |      19.32|      28.98|          27.19|        98.42|          29.05|        99.60|
|amh_Ethi |      22.14|      29.81|          23.51|        95.55|          24.77|        91.01|
|apc_Arab |      54.38|      56.81|          52.36|        99.51|          54.67|        99.60|
|arb_Arab |      59.41|      60.67|          57.76|        98.22|          59.24|        99.41|
|arb_Latn |      25.68|      33.25|          31.73|        99.41|          33.37|        99.41|
|ars_Arab |      58.34|      60.00|          56.82|        98.72|          58.45|        99.41|
|ary_Arab |      46.01|      48.94|          45.40|        99.31|          47.57|        99.41|
|arz_Arab |      51.66|      53.66|          50.31|        99.11|          52.23|        99.80|
|asm_Beng |      40.95|      45.35|          40.64|        99.80|          44.07|        98.72|
|ast_Latn |      59.61|      61.72|          59.35|        98.81|          61.11|        99.01|
|awa_Deva |      45.18|      53.26|          48.41|        99.90|          51.16|        99.60|
|ayr_Latn |      12.01|      20.06|          21.94|        96.34|          24.47|        98.81|
|azb_Arab |      25.52|      35.31|          33.22|        98.81|          35.92|        99.60|
|azj_Latn |      44.55|      47.37|          44.81|        99.01|          46.30|        99.51|
|bak_Cyrl |      43.66|      48.12|          43.66|        98.52|          46.60|        98.12|
|bam_Latn |      14.85|      21.95|          22.43|        97.33|          24.21|        98.02|
|ban_Latn |      41.55|      44.55|          40.57|        99.60|          43.70|        99.80|
|bel_Cyrl |      47.62|      49.93|          47.16|        99.11|          48.44|        99.21|
|bem_Latn |      15.15|      24.46|          26.26|        99.01|          28.03|        99.11|
|ben_Beng |      51.03|      52.60|          49.90|        99.80|          51.88|        99.51|
|bho_Deva |      41.93|      47.77|          43.35|        99.70|          45.94|        99.90|
|bjn_Arab |      10.98|      19.41|          19.71|        94.76|          22.61|        95.95|
|bjn_Latn |      43.24|      49.66|          42.79|        99.60|          47.89|        99.60|
|bod_Tibt |      15.78|      25.01|          22.45|        95.26|          23.54|        98.02|
|bos_Latn |      61.90|      63.77|          61.11|        99.11|          62.35|        98.72|
|bug_Latn |      20.86|      29.10|          27.85|        99.11|          31.11|        99.41|
|bul_Cyrl |      61.12|      62.92|          61.20|        98.42|          62.05|        99.11|
|cat_Latn |      64.65|      66.87|          65.29|        99.11|          66.17|        99.60|
|ceb_Latn |      51.68|      55.97|          51.01|        99.21|          53.97|        98.91|
|ces_Latn |      60.93|      61.64|          61.22|        98.81|          61.85|        99.01|
|cjk_Latn |      14.64|      21.06|          23.11|        97.13|          25.39|        98.91|
|ckb_Arab |      42.05|      44.20|          39.97|        99.41|          42.33|        99.41|
|crh_Latn |      37.88|      44.11|          39.90|        99.31|          43.05|        99.31|
|cym_Latn |      65.13|      67.27|          60.77|        99.60|          63.32|        99.51|
|dan_Latn |      66.81|      68.40|          66.57|        98.81|          67.32|        99.51|
|deu_Latn |      63.78|      65.23|          64.44|        99.21|          64.73|        99.11|
|dik_Latn |      15.03|      21.03|          21.67|        99.80|          25.32|        98.32|
|dyu_Latn |      12.52|      20.99|          22.22|        97.33|          24.15|        98.72|
|dzo_Tibt |      13.30|      21.85|          20.63|        93.77|          21.41|        94.66|
|ell_Grek |      57.56|      58.82|          57.35|        99.41|          58.10|        99.70|
|epo_Latn |      61.99|      64.99|          61.54|        98.72|          63.56|        99.11|
|est_Latn |      54.58|      56.21|          54.34|        98.52|          55.01|        99.21|
|eus_Latn |      48.90|      51.86|          47.18|        99.51|          49.64|        99.80|
|ewe_Latn |      14.60|      21.52|          21.89|        96.64|          24.27|        98.72|
|fao_Latn |      47.64|      52.02|          44.99|        98.91|          48.62|        98.91|
|fij_Latn |      19.28|      25.05|          25.34|        97.33|          26.86|        99.21|
|fin_Latn |      56.12|      57.01|          55.27|        99.51|          56.28|        99.70|
|fon_Latn |      11.46|      19.22|          21.44|        95.75|          23.28|        97.83|
|fra_Latn |      64.94|      66.30|          65.03|        98.22|          65.54|        99.21|
|fur_Latn |      53.08|      58.68|          50.97|        99.11|          56.25|        99.31|
|fuv_Latn |      14.42|      22.33|          22.01|        98.91|          24.70|        99.01|
|gla_Latn |      44.51|      46.69|          40.05|        99.51|          42.74|        98.72|
|gle_Latn |      52.28|      55.10|          48.56|        99.51|          50.97|        99.60|
|glg_Latn |      62.34|      63.70|          62.16|        99.41|          62.93|        99.21|
|grn_Latn |      22.68|      29.43|          29.02|        98.52|          31.82|        99.41|
|guj_Gujr |      47.04|      52.03|          47.48|        99.90|          49.55|        99.01|
|hat_Latn |      47.50|      51.11|          43.75|        99.21|          47.06|        99.11|
|hau_Latn |      38.64|      42.87|          37.01|        99.60|          40.23|        99.31|
|heb_Hebr |      59.29|      62.38|          58.68|        99.70|          60.19|        99.90|
|hin_Deva |      56.52|      58.89|          55.78|        99.80|          57.14|        99.41|
|hne_Deva |      44.25|      51.18|          45.94|        99.90|          49.26|        99.80|
|hrv_Latn |      58.91|      60.36|          58.67|        98.52|          59.35|        98.81|
|hun_Latn |      56.84|      58.32|          56.39|        99.11|          57.07|        99.60|
|hye_Armn |      55.69|      57.43|          54.81|        99.11|          55.72|        99.70|
|ibo_Latn |      32.16|      38.88|          31.21|        98.91|          35.69|        99.11|
|ilo_Latn |      38.89|      44.82|          40.18|        99.11|          44.02|        99.21|
|ind_Latn |      62.54|      64.30|          61.49|        99.51|          62.84|        98.91|
|isl_Latn |      50.27|      52.60|          48.11|        99.11|          49.84|        99.11|
|ita_Latn |      58.42|      59.33|          58.68|        98.81|          59.01|        99.70|
|jav_Latn |      49.18|      53.55|          46.38|        99.51|          50.19|        99.31|
|jpn_Jpan |      49.40|      52.45|          49.49|        99.51|          51.33|        99.70|
|kab_Latn |      13.31|      20.38|          20.67|        96.15|          23.13|        98.52|
|kac_Latn |      10.78|      22.04|          21.92|        95.36|          25.20|        98.32|
|kam_Latn |      16.52|      23.77|          24.18|        97.73|          25.90|        98.72|
|kan_Knda |      48.53|      49.99|          44.72|        99.90|          47.02|        99.80|
|kas_Arab |      21.17|      34.39|          29.80|        98.22|          34.48|        98.72|
|kas_Deva |      17.85|      30.07|          26.53|        98.22|          30.34|        99.31|
|kat_Geor |      47.16|      49.48|          46.46|        97.63|          47.59|        99.01|
|knc_Arab |       7.10|      14.98|          16.43|        95.36|          19.70|        97.43|
|knc_Latn |      11.50|      22.28|          23.30|        97.53|          26.04|        98.32|
|kaz_Cyrl |      44.42|      50.71|          45.70|        99.80|          48.41|        99.60|
|kbp_Latn |      13.97|      22.22|          22.24|        96.34|          24.04|        97.13|
|kea_Latn |      46.32|      55.53|          46.62|        99.01|          52.69|        99.01|
|khm_Khmr |      39.02|      44.93|          36.88|        98.72|          38.33|        98.81|
|kik_Latn |      18.62|      26.13|          25.87|        97.43|          27.65|        98.72|
|kin_Latn |      26.97|      31.56|          30.66|        99.51|          32.68|        99.01|
|kir_Cyrl |      37.49|      42.15|          39.22|        98.72|          41.73|        99.31|
|kmb_Latn |      12.37|      21.86|          23.05|        97.43|          25.28|        98.52|
|kmr_Latn |      35.47|      38.27|          35.16|        99.31|          38.22|        99.60|
|kon_Latn |      18.93|      26.27|          26.09|        97.83|          28.40|        98.62|
|kor_Hang |      50.98|      52.04|          49.73|        99.31|          51.27|        99.70|
|lao_Laoo |      27.79|      34.19|          27.64|        98.81|          28.31|        97.33|
|lij_Latn |      52.17|      58.37|          51.95|        98.81|          57.20|        99.11|
|lim_Latn |      54.54|      58.99|          52.92|        99.80|          56.87|        99.70|
|lin_Latn |      20.35|      28.12|          26.13|        98.81|          28.84|        99.31|
|lit_Latn |      52.52|      53.82|          51.63|        97.23|          52.75|        98.62|
|lmo_Latn |      50.81|      55.39|          49.92|        99.01|          54.15|        99.51|
|ltg_Latn |      30.52|      37.65|          33.08|        98.02|          36.66|        99.01|
|ltz_Latn |      57.11|      60.95|          55.35|        99.60|          57.51|        99.70|
|lua_Latn |      14.39|      23.74|          24.96|        98.42|          27.53|        98.81|
|lug_Latn |      19.58|      26.38|          25.08|        99.11|          27.76|        99.31|
|luo_Latn |      13.58|      22.60|          23.20|        97.43|          25.88|        99.11|
|lus_Latn |      26.23|      30.12|          29.59|        99.31|          31.95|        99.70|
|lvs_Latn |      53.46|      56.32|          53.45|        98.12|          54.62|        99.21|
|mag_Deva |      48.02|      55.90|          50.48|        99.90|          52.79|        99.80|
|mai_Deva |      44.36|      53.48|          45.81|        99.60|          50.06|        99.51|
|mal_Mlym |      47.07|      50.77|          46.43|        99.51|          48.48|        99.41|
|mar_Deva |      47.31|      51.91|          47.85|        99.90|          50.09|        99.60|
|min_Arab |      10.10|      17.11|          19.86|        95.95|          22.21|        96.94|
|min_Latn |      45.41|      51.28|          42.16|        99.70|          47.97|        99.41|
|mkd_Cyrl |      61.09|      63.29|          60.60|        97.63|          62.28|        98.32|
|plt_Latn |      25.40|      33.31|          30.51|        98.72|          32.93|        98.91|
|mlt_Latn |      63.52|      66.82|          60.13|        99.31|          62.71|        99.11|
|mni_Beng |       9.12|      21.58|          19.54|        87.65|          24.49|        96.74|
|khk_Cyrl |      33.33|      40.56|          35.35|        98.62|          39.06|        98.72|
|mos_Latn |      12.89|      21.01|          21.68|        97.83|          24.15|        98.81|
|mri_Latn |      32.92|      37.61|          33.24|        99.60|          35.73|        99.51|
|mya_Mymr |      32.92|      39.21|          31.79|        98.42|          34.29|        97.43|
|nld_Latn |      55.92|      56.94|          56.22|        99.70|          56.93|        99.21|
|nno_Latn |      63.69|      65.36|          63.31|        98.91|          64.37|        99.21|
|nob_Latn |      63.35|      64.40|          63.20|        99.41|          63.68|        99.51|
|npi_Deva |      48.71|      53.96|          47.87|        99.60|          51.38|        99.51|
|nso_Latn |      22.16|      28.51|          27.26|        98.81|          29.55|        99.31|
|nus_Latn |       9.51|      17.51|          19.54|        98.22|          22.14|        97.63|
|nya_Latn |      22.68|      28.86|          27.60|        99.31|          30.59|        99.01|
|oci_Latn |      68.46|      70.45|          67.11|        99.01|          68.97|        99.41|
|gaz_Latn |      13.20|      21.74|          20.77|        96.44|          23.27|        98.91|
|ory_Orya |      43.90|      47.63|          41.70|        99.70|          44.59|        99.31|
|pag_Latn |      32.71|      38.69|          36.08|        99.41|          38.61|        99.31|
|pan_Guru |      49.84|      52.31|          46.43|        99.60|          49.49|        99.11|
|pap_Latn |      53.97|      61.84|          52.94|        98.91|          59.07|        98.81|
|pes_Arab |      56.79|      58.37|          55.77|        99.70|          57.14|        99.90|
|pol_Latn |      53.18|      55.02|          53.69|        99.11|          54.40|        99.51|
|por_Latn |      68.23|      69.75|          68.44|        98.52|          68.78|        99.31|
|prs_Arab |      52.39|      57.38|          54.93|        99.51|          56.45|        99.51|
|pbt_Arab |      41.71|      46.89|          41.31|        99.41|          45.39|        99.41|
|quy_Latn |      16.42|      24.93|          24.98|        99.01|          27.55|        99.31|
|ron_Latn |      63.82|      64.97|          63.61|        98.91|          64.15|        99.51|
|run_Latn |      23.11|      27.69|          26.28|        98.52|          29.10|        99.21|
|rus_Cyrl |      57.60|      59.47|          58.49|        97.73|          58.83|        99.11|
|sag_Latn |      12.55|      21.10|          23.20|        96.25|          25.19|        99.41|
|san_Deva |      30.73|      39.53|          35.80|        99.41|          39.51|        99.70|
|sat_Olck |      15.56|      22.20|          20.49|        93.87|          21.19|        94.96|
|scn_Latn |      52.12|      55.73|          50.95|        98.72|          54.09|        99.31|
|shn_Mymr |      17.00|      29.78|          24.72|        94.76|          27.38|        60.67|
|sin_Sinh |      39.94|      44.21|          39.53|        99.51|          41.86|        99.21|
|slk_Latn |      58.24|      60.50|          59.13|        99.51|          60.00|        99.31|
|slv_Latn |      56.02|      57.69|          55.32|        99.11|          56.38|        99.31|
|smo_Latn |      27.05|      33.63|          29.96|        99.11|          32.13|        98.81|
|sna_Latn |      21.52|      28.18|          27.58|        98.91|          29.80|        99.41|
|snd_Arab |      39.94|      48.94|          39.85|        99.60|          45.01|        99.31|
|som_Latn |      21.51|      30.77|          28.63|        99.21|          30.23|        99.51|
|sot_Latn |      20.57|      27.62|          26.97|        98.91|          28.98|        98.81|
|spa_Latn |      56.16|      57.84|          56.33|        98.81|          57.49|        99.41|
|als_Latn |      58.56|      61.13|          57.68|        98.81|          59.14|        98.62|
|srd_Latn |      54.61|      57.75|          53.48|        98.72|          57.25|        99.11|
|srp_Cyrl |      62.57|      64.67|          62.09|        98.32|          63.22|        99.41|
|ssw_Latn |      20.09|      25.83|          25.67|        98.42|          28.43|        99.01|
|sun_Latn |      45.98|      50.55|          44.47|        99.70|          48.39|        99.51|
|swe_Latn |      66.44|      67.87|          66.62|        98.72|          67.11|        97.92|
|swh_Latn |      53.62|      56.70|          52.03|        99.80|          54.43|        99.41|
|szl_Latn |      51.47|      56.88|          50.54|        99.11|          53.72|        99.41|
|tam_Taml |      44.65|      48.96|          42.52|        99.70|          44.97|        99.51|
|tat_Cyrl |      42.75|      48.60|          43.78|        98.91|          47.53|        99.01|
|tel_Telu |      47.66|      53.62|          48.22|        99.60|          50.36|        99.21|
|tgk_Cyrl |      44.08|      48.17|          42.28|        97.92|          46.48|        98.81|
|tgl_Latn |      61.09|      62.82|          58.66|        99.11|          60.36|        99.51|
|tha_Thai |      51.71|      54.46|          51.21|        99.41|          53.04|        99.21|
|tir_Ethi |      12.34|      19.71|          19.47|        92.29|          21.00|        92.59|
|taq_Latn |      12.67|      21.38|          22.69|        97.23|          25.19|        98.91|
|taq_Tfng |       5.44|      16.28|          17.88|        88.24|          19.22|        94.76|
|tpi_Latn |      40.79|      44.81|          40.36|        99.31|          43.85|        99.41|
|tsn_Latn |      20.68|      26.94|          26.73|        99.01|          28.30|        99.51|
|tso_Latn |      19.68|      24.68|          25.02|        97.83|          27.09|        98.32|
|tuk_Latn |      33.08|      40.57|          36.60|        97.92|          39.64|        99.60|
|tum_Latn |      17.98|      26.20|          26.39|        98.12|          28.17|        99.31|
|tur_Latn |      56.37|      57.97|          56.28|        99.80|          57.17|        99.60|
|twi_Latn |      22.14|      28.58|          27.25|        99.01|          29.40|        99.60|
|tzm_Tfng |       6.99|      15.96|          17.36|        87.15|          19.20|        94.76|
|uig_Arab |      34.26|      39.57|          34.81|        99.70|          38.02|        99.21|
|ukr_Cyrl |      60.03|      61.79|          59.88|        98.81|          60.68|        99.21|
|umb_Latn |      12.83|      20.47|          21.91|        98.32|          24.35|        99.41|
|urd_Arab |      49.08|      53.16|          49.38|        99.80|          51.90|        99.70|
|uzn_Latn |      47.16|      50.46|          46.69|        98.52|          49.81|        99.70|
|vec_Latn |      58.10|      62.50|          57.06|        98.91|          60.46|        99.41|
|vie_Latn |      56.65|      57.69|          56.03|        99.31|          56.80|        99.51|
|war_Latn |      51.52|      57.14|          49.03|        99.51|          54.09|        99.51|
|wol_Latn |      16.34|      23.81|          24.09|        97.73|          26.62|        99.01|
|xho_Latn |      24.72|      31.60|          29.19|        98.91|          32.27|        98.42|
|ydd_Hebr |      54.31|      61.30|          51.86|        98.32|          56.74|        98.62|
|yor_Latn |      20.63|      27.40|          26.45|        99.21|          28.56|        99.31|
|yue_Hant |      51.95|      53.83|          51.39|        99.70|          52.99|        99.70|
|zho_Hans |      52.00|      53.60|          51.52|        99.41|          52.90|        99.70|
|zho_Hant |      50.76|      52.36|          50.10|        99.60|          51.48|        99.80|
|zsm_Latn |      61.81|      63.68|          60.43|        99.21|          62.11|        99.21|
|zul_Latn |      23.83|      29.61|          29.22|        99.11|          32.32|        99.01|

### 8B Model English-X


### 70B Model X-English


### 70B Model English-X


### Selective Translation