# params 
 {'predict_dates': [{'start': '2026-05-29', 'end': '2026-05-29'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260530_16 130420118034805664 (Recorders: 4/5)

	Recorder: 30dca948ebc94740b6333b13a7612f24

		Model: {'id': '30dca948ebc94740b6333b13a7612f24', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.012, 'Rank IC': 0.022, 'Rank ICIR': 0.15}, 'data_train_vec': ['2021-05-28', '2025-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.150', 'weight': '0.054'}

	Recorder: 25eea0794b5f43988774fd18e41dfd23

		Model: {'id': '25eea0794b5f43988774fd18e41dfd23', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.001, 'ICIR': 0.008, 'Rank IC': 0.019, 'Rank ICIR': 0.137}, 'data_train_vec': ['2022-05-30', '2025-05-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.137', 'weight': '0.049'}

	Recorder: 9e0a975e7dc84b3dbdb2f1ecac2eabe3

		Model: {'id': '9e0a975e7dc84b3dbdb2f1ecac2eabe3', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.31, 'Rank IC': 0.029, 'Rank ICIR': 0.196}, 'data_train_vec': ['2023-05-28', '2025-08-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.196', 'weight': '0.070'}

	Recorder: bf856eb36a7f43ab9dba8b36fc40d713

		Model: {'id': 'bf856eb36a7f43ab9dba8b36fc40d713', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.245, 'Rank IC': 0.012, 'Rank ICIR': 0.058}, 'data_train_vec': ['2025-05-28', '2026-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.058', 'weight': '0.021'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260530_16 697112318166872270 (Recorders: 3/5)

	Recorder: 8bc132087bda4d0b96b607fec759c4b9

		Model: {'id': '8bc132087bda4d0b96b607fec759c4b9', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.16, 'Rank IC': 0.027, 'Rank ICIR': 0.189}, 'data_train_vec': ['2023-05-28', '2025-08-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.189', 'weight': '0.068'}

	Recorder: 7b6f7feee5594495ad5b5f24301451e5

		Model: {'id': '7b6f7feee5594495ad5b5f24301451e5', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.081, 'Rank IC': 0.009, 'Rank ICIR': 0.083}, 'data_train_vec': ['2024-05-30', '2025-11-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.083', 'weight': '0.030'}

	Recorder: a634798e02474a0f94de193ccc69163b

		Model: {'id': 'a634798e02474a0f94de193ccc69163b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.076, 'ICIR': 0.34, 'Rank IC': 0.03, 'Rank ICIR': 0.135}, 'data_train_vec': ['2025-05-28', '2026-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.135', 'weight': '0.049'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260530_14 580028373558155694 (Recorders: 3/5)

	Recorder: 4767095153c74dbcb8c817e026a5e74e

		Model: {'id': '4767095153c74dbcb8c817e026a5e74e', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.057, 'Rank IC': 0.035, 'Rank ICIR': 0.231}, 'data_train_vec': ['2021-05-28', '2025-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.231', 'weight': '0.083'}

	Recorder: 5f615105bdc54608880568ca1850df14

		Model: {'id': '5f615105bdc54608880568ca1850df14', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.029, 'Rank IC': 0.039, 'Rank ICIR': 0.22}, 'data_train_vec': ['2022-05-30', '2025-05-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.220', 'weight': '0.079'}

	Recorder: e33ceb2eb38b41d1864d37e8cb440d0d

		Model: {'id': 'e33ceb2eb38b41d1864d37e8cb440d0d', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.206, 'Rank IC': 0.039, 'Rank ICIR': 0.264}, 'data_train_vec': ['2023-05-28', '2025-08-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.264', 'weight': '0.095'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260530_14 707845802814174961 (Recorders: 4/5)

	Recorder: 80d69dc0a6da4ba0babcdc2a007d308e

		Model: {'id': '80d69dc0a6da4ba0babcdc2a007d308e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.064, 'Rank IC': 0.035, 'Rank ICIR': 0.304}, 'data_train_vec': ['2021-05-28', '2025-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.304', 'weight': '0.109'}

	Recorder: 2f1b312a714b4aeb93c9ac461fd47615

		Model: {'id': '2f1b312a714b4aeb93c9ac461fd47615', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.097, 'Rank IC': 0.031, 'Rank ICIR': 0.281}, 'data_train_vec': ['2023-05-28', '2025-08-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.281', 'weight': '0.101'}

	Recorder: 5ab52e0fa78f44668d350b576f23b534

		Model: {'id': '5ab52e0fa78f44668d350b576f23b534', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.029, 'Rank IC': 0.011, 'Rank ICIR': 0.083}, 'data_train_vec': ['2024-05-30', '2025-11-29'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.083', 'weight': '0.030'}

	Recorder: 23d0e7bcf85f4b7a884884c55a596101

		Model: {'id': '23d0e7bcf85f4b7a884884c55a596101', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.051, 'ICIR': 0.242, 'Rank IC': 0.029, 'Rank ICIR': 0.124}, 'data_train_vec': ['2025-05-28', '2026-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.124', 'weight': '0.045'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260530_13 827090228650426005 (Recorders: 3/5)

	Recorder: 69cd53c25b1b4813910a3d1634ea7f1c

		Model: {'id': '69cd53c25b1b4813910a3d1634ea7f1c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.025, 'Rank IC': 0.02, 'Rank ICIR': 0.122}, 'data_train_vec': ['2021-05-28', '2025-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.122', 'weight': '0.044'}

	Recorder: 17a3ee5c410b46c8915522f319dab4f9

		Model: {'id': '17a3ee5c410b46c8915522f319dab4f9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.036, 'Rank IC': 0.026, 'Rank ICIR': 0.168}, 'data_train_vec': ['2023-05-28', '2025-08-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.168', 'weight': '0.060'}

	Recorder: 4b454b9430444dbd94a35b1b06ca1dbb

		Model: {'id': '4b454b9430444dbd94a35b1b06ca1dbb', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.086, 'Rank IC': 0.006, 'Rank ICIR': 0.037}, 'data_train_vec': ['2025-05-28', '2026-02-27'], 'train_time_vec': ['2026-05-30', '2026-05-30'], 'rank_icir': '0.037', 'weight': '0.013'}
