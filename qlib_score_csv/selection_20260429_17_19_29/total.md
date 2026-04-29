# params 
 {'predict_dates': [{'start': '2026-04-29', 'end': '2026-04-29'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260429_16 801016829791913220 (Recorders: 2/5)

	Recorder: e67ec670ade54781878920756638d200

		Model: {'id': 'e67ec670ade54781878920756638d200', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.06, 'Rank IC': 0.014, 'Rank ICIR': 0.142}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.142', 'weight': '0.087'}

	Recorder: d875ecb3f810452b8a47f919aface22b

		Model: {'id': 'd875ecb3f810452b8a47f919aface22b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.185, 'Rank IC': 0.009, 'Rank ICIR': 0.056}, 'data_train_vec': ['2025-04-29', '2026-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.056', 'weight': '0.034'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260429_16 467650333505409872 (Recorders: 2/5)

	Recorder: 47591c6daa1e49aaad3ee9ce7df86db0

		Model: {'id': '47591c6daa1e49aaad3ee9ce7df86db0', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.082, 'Rank IC': 0.012, 'Rank ICIR': 0.111}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.111', 'weight': '0.068'}

	Recorder: c8546c98d40d4fdb9c8c97fa21d3728e

		Model: {'id': 'c8546c98d40d4fdb9c8c97fa21d3728e', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.063, 'ICIR': 0.543, 'Rank IC': 0.031, 'Rank ICIR': 0.232}, 'data_train_vec': ['2025-04-29', '2026-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.232', 'weight': '0.142'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260429_14 696297494791611829 (Recorders: 3/5)

	Recorder: 1b0e1ba444874bfebde0184216a21cab

		Model: {'id': '1b0e1ba444874bfebde0184216a21cab', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.049, 'Rank IC': 0.039, 'Rank ICIR': 0.233}, 'data_train_vec': ['2023-04-29', '2025-07-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.233', 'weight': '0.143'}

	Recorder: 143c8f7689c547988d11078f7b2cb515

		Model: {'id': '143c8f7689c547988d11078f7b2cb515', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.093, 'Rank IC': 0.007, 'Rank ICIR': 0.063}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.063', 'weight': '0.039'}

	Recorder: e8acd61b750b410bb19391b197f304aa

		Model: {'id': 'e8acd61b750b410bb19391b197f304aa', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.029, 'ICIR': 0.202, 'Rank IC': 0.013, 'Rank ICIR': 0.081}, 'data_train_vec': ['2025-04-29', '2026-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.081', 'weight': '0.050'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260429_14 123895955150438208 (Recorders: 2/5)

	Recorder: 8647adef49c248cdb83a98fbc1d13d8d

		Model: {'id': '8647adef49c248cdb83a98fbc1d13d8d', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.031, 'Rank IC': 0.01, 'Rank ICIR': 0.084}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.084', 'weight': '0.051'}

	Recorder: 36858f1dc50d4ac4b9da24f03fe5fc62

		Model: {'id': '36858f1dc50d4ac4b9da24f03fe5fc62', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.068, 'ICIR': 0.626, 'Rank IC': 0.042, 'Rank ICIR': 0.342}, 'data_train_vec': ['2025-04-29', '2026-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.342', 'weight': '0.209'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260429_14 324903396235927429 (Recorders: 2/5)

	Recorder: 0d9ae27847f9492ebc46aae49a80b0f7

		Model: {'id': '0d9ae27847f9492ebc46aae49a80b0f7', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.06, 'Rank IC': 0.02, 'Rank ICIR': 0.177}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.177', 'weight': '0.108'}

	Recorder: 297a045d21894cc0b898ec67d6729657

		Model: {'id': '297a045d21894cc0b898ec67d6729657', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.188, 'Rank IC': 0.014, 'Rank ICIR': 0.113}, 'data_train_vec': ['2025-04-29', '2026-01-28'], 'train_time_vec': ['2026-04-29', '2026-04-29'], 'rank_icir': '0.113', 'weight': '0.069'}
