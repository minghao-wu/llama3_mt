# Evaluating the Machine Translation Capability of Llama-3 Models

In this project, we evaluate the machine translation capabilities of [Llama-3 models](https://huggingface.co/collections/meta-llama/meta-llama-3-66214712577ca38149ebb2b6) using the [facebook/flores](https://huggingface.co/datasets/facebook/flores) dataset. We assess these models on the X-English translations in zero-shot and five-shot settings. 

**NOTE: The Flores-200 dataset likely leaked into the training set of the Llama-3 models.**

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
    --model_id $model_id \
    --dataset facebook/flores \
    --tgt_lang $tgt_lang \ # either "eng_Latn" or "all"
    --results_dir <TRANSLATION_DIR> \
    --nshots $nshots
```
To translate with the instruct models, you can run
```
python run_instruct.py \
    --model_id $model_id \
    --dataset facebook/flores \
    --tgt_lang $tgt_lang \ # either "eng_Latn" or "all"
    --results_dir <TRANSLATION_DIR> \
    --nshots $nshots
```
You can also serve the models with the scripts of `serve_llama.sh` and `run_api.py`.

## Results
We run evaluations on [facebook/flores](https://huggingface.co/datasets/facebook/flores). The translations are evaluated using `chrF++` with the signature of `nrefs:1|case:mixed|eff:yes|nc:6|nw:2|space:no|version:2.4.2`. The raw translations can be found under the folder `translations`.

**NOTE: The results of `gpt-3.5-turbo` are adopted from [https://arxiv.org/abs/2305.06575](https://arxiv.org/abs/2305.06575).**

* [8B Model X-English](#8b-model-x-english)
* [70B Model X-English](#70b-model-x-english)

## Citation

```
@misc{llama3_mt,
  author = {Minghao Wu},
  title = {Evaluating the Machine Translation Capability of Llama-3 Models},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/minghao-wu/llama3_mt}},
}
```

### 8B Model X-English

|languages|0-shot Base|5-shot Base|0-shot Instruct|5-shot Instruct|0-shot gpt-3.5-turbo|
|---------|----------:|----------:|--------------:|--------------:|--------------------|
|ace_Arab |      11.16|      20.78|          20.60|          22.63|                3.35|
|ace_Latn |      24.22|      33.79|          31.23|          34.48|               10.12|
|acm_Arab |      54.05|      54.57|          52.43|          53.97|               27.78|
|acq_Arab |      55.52|      56.25|          54.25|          55.85|               29.45|
|aeb_Arab |      48.31|      51.12|          48.48|          49.94|               24.38|
|afr_Latn |      71.14|      73.14|          69.68|          71.48|               53.62|
|ajp_Arab |      56.75|      59.44|          54.88|          57.01|               33.45|
|aka_Latn |      19.32|      28.98|          27.07|          29.03|                7.87|
|amh_Ethi |      22.14|      29.81|          23.46|          24.82|                4.10|
|apc_Arab |      54.38|      56.81|          52.33|          54.60|               29.70|
|arb_Arab |      59.41|      60.67|          57.65|          59.24|               33.30|
|arb_Latn |      25.68|      33.25|          31.68|          33.43|NA                  |
|ars_Arab |      58.34|      60.00|          56.73|          58.43|               32.31|
|ary_Arab |      46.01|      48.94|          45.40|          47.55|               21.67|
|arz_Arab |      51.66|      53.66|          50.29|          52.24|               25.54|
|asm_Beng |      40.95|      45.35|          40.65|          44.10|               12.09|
|ast_Latn |      59.61|      61.72|          59.33|          61.06|               36.22|
|awa_Deva |      45.18|      53.26|          48.42|          51.12|               19.51|
|ayr_Latn |      12.01|      20.06|          21.90|          24.52|                4.49|
|azb_Arab |      25.52|      35.31|          33.15|          35.90|                8.37|
|azj_Latn |      44.55|      47.37|          44.78|          46.27|               16.96|
|bak_Cyrl |      43.66|      48.12|          43.61|          46.48|                8.63|
|bam_Latn |      14.85|      21.95|          22.41|          24.21|                4.85|
|ban_Latn |      41.55|      44.55|          40.52|          43.69|               17.36|
|bel_Cyrl |      47.62|      49.93|          47.17|          48.41|               17.05|
|bem_Latn |      15.15|      24.46|          26.17|          27.97|                7.84|
|ben_Beng |      51.03|      52.60|          49.88|          51.83|               20.66|
|bho_Deva |      41.93|      47.77|          43.43|          45.93|               14.90|
|bjn_Arab |      10.98|      19.41|          19.69|          22.64|                4.12|
|bjn_Latn |      43.24|      49.66|          42.78|          47.87|               19.12|
|bod_Tibt |      15.78|      25.01|          22.35|          23.52|                2.22|
|bos_Latn |      61.90|      63.77|          61.12|          62.36|               38.22|
|bug_Latn |      20.86|      29.10|          27.86|          31.10|                7.43|
|bul_Cyrl |      61.12|      62.92|          61.18|          62.02|               35.84|
|cat_Latn |      64.65|      66.87|          65.34|          66.14|               42.42|
|ceb_Latn |      51.68|      55.97|          50.93|          53.95|               31.85|
|ces_Latn |      60.93|      61.64|          61.22|          61.89|               36.18|
|cjk_Latn |      14.64|      21.06|          23.02|          25.37|                4.81|
|ckb_Arab |      42.05|      44.20|          39.93|          42.27|                8.98|
|crh_Latn |      37.88|      44.11|          39.91|          43.03|               18.32|
|cym_Latn |      65.13|      67.27|          60.76|          63.29|               45.90|
|dan_Latn |      66.81|      68.40|          66.58|          67.31|               45.39|
|deu_Latn |      63.78|      65.23|          64.45|          64.74|               40.51|
|dik_Latn |      15.03|      21.03|          21.69|          25.25|                5.14|
|dyu_Latn |      12.52|      20.99|          22.15|          24.13|                3.93|
|dzo_Tibt |      13.30|      21.85|          20.58|          21.46|                1.79|
|ell_Grek |      57.56|      58.82|          57.36|          58.10|               30.53|
|epo_Latn |      61.99|      64.99|          61.51|          63.50|               37.60|
|est_Latn |      54.58|      56.21|          54.39|          55.04|               33.66|
|eus_Latn |      48.90|      51.86|          47.15|          49.61|               21.10|
|ewe_Latn |      14.60|      21.52|          21.82|          24.25|                4.64|
|fao_Latn |      47.64|      52.02|          44.97|          48.60|               29.33|
|fij_Latn |      19.28|      25.05|          25.34|          26.87|                9.21|
|fin_Latn |      56.12|      57.01|          55.30|          56.29|               31.07|
|fon_Latn |      11.46|      19.22|          21.31|          23.23|                3.59|
|fra_Latn |      64.94|      66.30|          65.04|          65.53|               42.02|
|fur_Latn |      53.08|      58.68|          51.05|          56.20|               29.28|
|fuv_Latn |      14.42|      22.33|          22.01|          24.74|                4.79|
|gla_Latn |      44.51|      46.69|          40.01|          42.70|               21.09|
|gle_Latn |      52.28|      55.10|          48.54|          50.95|               28.53|
|glg_Latn |      62.34|      63.70|          62.15|          62.94|               37.42|
|grn_Latn |      22.68|      29.43|          28.89|          31.78|                7.43|
|guj_Gujr |      47.04|      52.03|          47.47|          49.48|               19.97|
|hat_Latn |      47.50|      51.11|          43.74|          47.05|               28.12|
|hau_Latn |      38.64|      42.87|          37.00|          40.25|                9.98|
|heb_Hebr |      59.29|      62.38|          58.65|          60.19|               34.75|
|hin_Deva |      56.52|      58.89|          55.79|          57.18|               27.76|
|hne_Deva |      44.25|      51.18|          45.92|          49.23|               18.31|
|hrv_Latn |      58.91|      60.36|          58.67|          59.43|               33.90|
|hun_Latn |      56.84|      58.32|          56.29|          57.09|               31.08|
|hye_Armn |      55.69|      57.43|          54.77|          55.72|               15.75|
|ibo_Latn |      32.16|      38.88|          31.18|          35.66|                6.98|
|ilo_Latn |      38.89|      44.82|          40.24|          44.02|               16.95|
|ind_Latn |      62.54|      64.30|          61.51|          62.93|               37.62|
|isl_Latn |      50.27|      52.60|          48.12|          49.88|               28.66|
|ita_Latn |      58.42|      59.33|          58.66|          58.98|               30.12|
|jav_Latn |      49.18|      53.55|          46.37|          50.21|               22.78|
|jpn_Jpan |      49.40|      52.45|          49.52|          51.34|               22.87|
|kab_Latn |      13.31|      20.38|          20.70|          23.17|                4.56|
|kac_Latn |      10.78|      22.04|          21.81|          25.12|                3.78|
|kam_Latn |      16.52|      23.77|          24.02|          25.93|                6.42|
|kan_Knda |      48.53|      49.99|          44.74|          47.03|               18.13|
|kas_Arab |      21.17|      34.39|          29.63|          34.48|                7.56|
|kas_Deva |      17.85|      30.07|          26.41|          30.31|                7.18|
|kat_Geor |      47.16|      49.48|          46.47|          47.59|               12.51|
|knc_Arab |       7.10|      14.98|          16.46|          19.68|                2.54|
|knc_Latn |      11.50|      22.28|          23.23|          25.96|                5.04|
|kaz_Cyrl |      44.42|      50.71|          45.69|          48.46|               15.35|
|kbp_Latn |      13.97|      22.22|          22.25|          23.92|                3.86|
|kea_Latn |      46.32|      55.53|          46.63|          52.61|               35.17|
|khm_Khmr |      39.02|      44.93|          36.82|          38.28|               10.09|
|kik_Latn |      18.62|      26.13|          25.72|          27.63|                6.66|
|kin_Latn |      26.97|      31.56|          30.64|          32.66|               12.50|
|kir_Cyrl |      37.49|      42.15|          39.23|          41.72|                9.53|
|kmb_Latn |      12.37|      21.86|          23.02|          25.31|                5.24|
|kmr_Latn |      35.47|      38.27|          35.21|          38.16|               14.87|
|kon_Latn |      18.93|      26.27|          25.95|          28.37|                5.82|
|kor_Hang |      50.98|      52.04|          49.68|          51.26|               23.65|
|lao_Laoo |      27.79|      34.19|          27.64|          28.25|                7.64|
|lij_Latn |      52.17|      58.37|          51.96|          57.18|               29.70|
|lim_Latn |      54.54|      58.99|          52.91|          56.91|               35.97|
|lin_Latn |      20.35|      28.12|          26.12|          28.81|                8.40|
|lit_Latn |      52.52|      53.82|          51.55|          52.78|               28.36|
|lmo_Latn |      50.81|      55.39|          49.93|          54.15|               28.16|
|ltg_Latn |      30.52|      37.65|          33.11|          36.72|               12.63|
|ltz_Latn |      57.11|      60.95|          55.39|          57.52|               35.99|
|lua_Latn |      14.39|      23.74|          24.91|          27.49|                6.45|
|lug_Latn |      19.58|      26.38|          25.08|          27.77|                7.92|
|luo_Latn |      13.58|      22.60|          23.14|          25.83|                4.66|
|lus_Latn |      26.23|      30.12|          29.52|          31.98|                7.74|
|lvs_Latn |      53.46|      56.32|          53.39|          54.67|               30.24|
|mag_Deva |      48.02|      55.90|          50.48|          52.77|               21.31|
|mai_Deva |      44.36|      53.48|          45.82|          50.12|               15.98|
|mal_Mlym |      47.07|      50.77|          46.44|          48.49|               16.31|
|mar_Deva |      47.31|      51.91|          47.85|          50.09|               18.50|
|min_Arab |      10.10|      17.11|          19.87|          22.19|NA                  |
|min_Latn |      45.41|      51.28|          42.12|          47.98|               17.83|
|mkd_Cyrl |      61.09|      63.29|          60.54|          62.26|               35.93|
|plt_Latn |      25.40|      33.31|          30.57|          32.95|               13.40|
|mlt_Latn |      63.52|      66.82|          60.08|          62.67|               38.24|
|mni_Beng |       9.12|      21.58|          19.37|          24.40|                3.35|
|khk_Cyrl |      33.33|      40.56|          35.33|          38.99|                9.43|
|mos_Latn |      12.89|      21.01|          21.65|          24.15|                4.07|
|mri_Latn |      32.92|      37.61|          33.29|          35.73|               16.36|
|mya_Mymr |      32.92|      39.21|          31.75|          34.17|                3.52|
|nld_Latn |      55.92|      56.94|          56.25|          56.94|               28.29|
|nno_Latn |      63.69|      65.36|          63.32|          64.40|               42.43|
|nob_Latn |      63.35|      64.40|          63.20|          63.70|               39.44|
|npi_Deva |      48.71|      53.96|          47.87|          51.39|               20.99|
|nso_Latn |      22.16|      28.51|          27.18|          29.51|               10.61|
|nus_Latn |       9.51|      17.51|          19.55|          22.12|                3.61|
|nya_Latn |      22.68|      28.86|          27.56|          30.58|               11.86|
|oci_Latn |      68.46|      70.45|          67.07|          68.94|               45.60|
|gaz_Latn |      13.20|      21.74|          20.75|          23.29|                4.54|
|ory_Orya |      43.90|      47.63|          41.72|          44.61|               14.19|
|pag_Latn |      32.71|      38.69|          36.10|          38.56|               14.93|
|pan_Guru |      49.84|      52.31|          46.49|          49.48|               21.52|
|pap_Latn |      53.97|      61.84|          52.95|          59.07|               39.13|
|pes_Arab |      56.79|      58.37|          55.79|          57.12|               29.21|
|pol_Latn |      53.18|      55.02|          53.72|          54.40|               26.05|
|por_Latn |      68.23|      69.75|          68.38|          68.77|               45.32|
|prs_Arab |      52.39|      57.38|          55.02|          56.47|               29.57|
|pbt_Arab |      41.71|      46.89|          41.28|          45.38|                9.16|
|quy_Latn |      16.42|      24.93|          24.95|          27.53|                5.16|
|ron_Latn |      63.82|      64.97|          63.63|          64.16|               38.90|
|run_Latn |      23.11|      27.69|          26.28|          29.07|                8.75|
|rus_Cyrl |      57.60|      59.47|          58.38|          58.79|               31.17|
|sag_Latn |      12.55|      21.10|          23.11|          25.20|                4.27|
|san_Deva |      30.73|      39.53|          35.77|          39.48|               10.26|
|sat_Olck |      15.56|      22.20|          20.40|          21.13|NA                  |
|scn_Latn |      52.12|      55.73|          50.89|          54.10|               29.03|
|shn_Mymr |      17.00|      29.78|          24.49|          25.59|                4.17|
|sin_Sinh |      39.94|      44.21|          39.45|          41.80|                4.48|
|slk_Latn |      58.24|      60.50|          59.10|          59.96|               34.61|
|slv_Latn |      56.02|      57.69|          55.28|          56.38|               31.91|
|smo_Latn |      27.05|      33.63|          29.94|          32.08|               12.90|
|sna_Latn |      21.52|      28.18|          27.49|          29.82|               10.22|
|snd_Arab |      39.94|      48.94|          39.80|          45.03|               11.40|
|som_Latn |      21.51|      30.77|          28.64|          30.23|               11.78|
|sot_Latn |      20.57|      27.62|          26.88|          28.95|               10.85|
|spa_Latn |      56.16|      57.84|          56.35|          57.51|               27.10|
|als_Latn |      58.56|      61.13|          57.65|          59.20|               33.73|
|srd_Latn |      54.61|      57.75|          53.50|          57.24|               29.21|
|srp_Cyrl |      62.57|      64.67|          62.00|          63.21|               38.67|
|ssw_Latn |      20.09|      25.83|          25.58|          28.39|                9.08|
|sun_Latn |      45.98|      50.55|          44.48|          48.36|               20.81|
|swe_Latn |      66.44|      67.87|          66.61|          67.11|               44.43|
|swh_Latn |      53.62|      56.70|          52.00|          54.43|               36.36|
|szl_Latn |      51.47|      56.88|          50.57|          53.75|               30.86|
|tam_Taml |      44.65|      48.96|          42.50|          44.91|               12.73|
|tat_Cyrl |      42.75|      48.60|          43.79|          47.55|               10.59|
|tel_Telu |      47.66|      53.62|          48.18|          50.39|               15.88|
|tgk_Cyrl |      44.08|      48.17|          42.28|          46.55|               14.10|
|tgl_Latn |      61.09|      62.82|          58.65|          60.37|               37.25|
|tha_Thai |      51.71|      54.46|          51.17|          52.99|               20.48|
|tir_Ethi |      12.34|      19.71|          19.45|          20.90|                2.58|
|taq_Latn |      12.67|      21.38|          22.56|          25.18|                5.11|
|taq_Tfng |       5.44|      16.28|          17.91|          19.22|                2.42|
|tpi_Latn |      40.79|      44.81|          40.36|          43.87|               16.99|
|tsn_Latn |      20.68|      26.94|          26.68|          28.32|                9.52|
|tso_Latn |      19.68|      24.68|          24.96|          27.15|               10.03|
|tuk_Latn |      33.08|      40.57|          36.55|          39.64|               13.67|
|tum_Latn |      17.98|      26.20|          26.33|          28.13|                7.19|
|tur_Latn |      56.37|      57.97|          56.26|          57.13|               33.03|
|twi_Latn |      22.14|      28.58|          27.17|          29.38|                7.81|
|tzm_Tfng |       6.99|      15.96|          17.24|          19.12|                2.52|
|uig_Arab |      34.26|      39.57|          34.82|          37.95|                8.05|
|ukr_Cyrl |      60.03|      61.79|          59.90|          60.71|               33.90|
|umb_Latn |      12.83|      20.47|          21.87|          24.39|                4.78|
|urd_Arab |      49.08|      53.16|          49.38|          51.90|               22.60|
|uzn_Latn |      47.16|      50.46|          46.65|          49.79|               17.65|
|vec_Latn |      58.10|      62.50|          57.07|          60.45|               35.76|
|vie_Latn |      56.65|      57.69|          56.00|          56.77|               29.38|
|war_Latn |      51.52|      57.14|          49.03|          54.06|               31.18|
|wol_Latn |      16.34|      23.81|          23.99|          26.53|                6.09|
|xho_Latn |      24.72|      31.60|          29.18|          32.18|               14.82|
|ydd_Hebr |      54.31|      61.30|          51.79|          56.64|               20.34|
|yor_Latn |      20.63|      27.40|          26.41|          28.58|                7.98|
|yue_Hant |      51.95|      53.83|          51.37|          52.99|               24.66|
|zho_Hans |      52.00|      53.60|          51.48|          52.90|               23.80|
|zho_Hant |      50.76|      52.36|          50.08|          51.48|               22.75|
|zsm_Latn |      61.81|      63.68|          60.45|          62.13|               37.47|
|zul_Latn |      23.83|      29.61|          29.18|          32.31|               14.61|


### 70B Model X-English

