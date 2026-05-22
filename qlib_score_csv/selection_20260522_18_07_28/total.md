# params 
 {'predict_dates': [{'start': '2026-05-22', 'end': '2026-05-22'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260522_17 746690066981106950 (Recorders: 3/5)

	Recorder: 00b1e87892fd4dbabb1c571f0d8d3c00

		Model: {'id': '00b1e87892fd4dbabb1c571f0d8d3c00', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.03, 'Rank IC': 0.027, 'Rank ICIR': 0.189}, 'data_train_vec': ['2022-05-22', '2025-05-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.189', 'weight': '0.055'}

	Recorder: 7193063294bb4791a81ae513428ce8cc

		Model: {'id': '7193063294bb4791a81ae513428ce8cc', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.119, 'Rank IC': 0.037, 'Rank ICIR': 0.254}, 'data_train_vec': ['2023-05-22', '2025-08-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.254', 'weight': '0.074'}

	Recorder: a5e8bcde94cc4dfc8175e33e5848b864

		Model: {'id': 'a5e8bcde94cc4dfc8175e33e5848b864', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.069, 'ICIR': 0.48, 'Rank IC': 0.03, 'Rank ICIR': 0.182}, 'data_train_vec': ['2025-05-22', '2026-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.182', 'weight': '0.053'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260522_17 134158103464148849 (Recorders: 3/5)

	Recorder: 74ba18d5220b4985a409f8b55e3cd59f

		Model: {'id': '74ba18d5220b4985a409f8b55e3cd59f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.182, 'Rank IC': 0.027, 'Rank ICIR': 0.219}, 'data_train_vec': ['2023-05-22', '2025-08-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.219', 'weight': '0.064'}

	Recorder: fe890005ac3b46de8b0bc1bc6ed8406e

		Model: {'id': 'fe890005ac3b46de8b0bc1bc6ed8406e', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.228, 'Rank IC': 0.007, 'Rank ICIR': 0.07}, 'data_train_vec': ['2024-05-22', '2025-11-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.070', 'weight': '0.020'}

	Recorder: 34a3794a232743edb4f5723f9e6a6cb1

		Model: {'id': '34a3794a232743edb4f5723f9e6a6cb1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.096, 'ICIR': 0.536, 'Rank IC': 0.047, 'Rank ICIR': 0.252}, 'data_train_vec': ['2025-05-22', '2026-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.252', 'weight': '0.074'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260522_15 562628085803222400 (Recorders: 4/5)

	Recorder: 3b4ac9b894724163b476909b9f3fbdbf

		Model: {'id': '3b4ac9b894724163b476909b9f3fbdbf', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.039, 'Rank IC': 0.031, 'Rank ICIR': 0.205}, 'data_train_vec': ['2021-05-22', '2025-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.205', 'weight': '0.060'}

	Recorder: 401bf1c326f447568e7ab36e32f16c3a

		Model: {'id': '401bf1c326f447568e7ab36e32f16c3a', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.022, 'Rank IC': 0.036, 'Rank ICIR': 0.205}, 'data_train_vec': ['2022-05-22', '2025-05-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.205', 'weight': '0.060'}

	Recorder: 83323fe03988403bbaa4451cd2004acc

		Model: {'id': '83323fe03988403bbaa4451cd2004acc', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.174, 'Rank IC': 0.039, 'Rank ICIR': 0.263}, 'data_train_vec': ['2023-05-22', '2025-08-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.263', 'weight': '0.077'}

	Recorder: 10afcdd6563f42768ec84a05526f2e7a

		Model: {'id': '10afcdd6563f42768ec84a05526f2e7a', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.077, 'ICIR': 0.459, 'Rank IC': 0.036, 'Rank ICIR': 0.2}, 'data_train_vec': ['2025-05-22', '2026-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.200', 'weight': '0.058'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260522_15 194177767852456482 (Recorders: 4/5)

	Recorder: e3f672cbebae40da8987b69164506760

		Model: {'id': 'e3f672cbebae40da8987b69164506760', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.065, 'Rank IC': 0.031, 'Rank ICIR': 0.28}, 'data_train_vec': ['2021-05-22', '2025-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.280', 'weight': '0.082'}

	Recorder: 39fe32eddd224b6caf4f1821ca9910e9

		Model: {'id': '39fe32eddd224b6caf4f1821ca9910e9', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.108, 'Rank IC': 0.036, 'Rank ICIR': 0.337}, 'data_train_vec': ['2023-05-22', '2025-08-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.337', 'weight': '0.098'}

	Recorder: 970139c4f93d4d91b81d651a740410a4

		Model: {'id': '970139c4f93d4d91b81d651a740410a4', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.001, 'ICIR': 0.008, 'Rank IC': 0.012, 'Rank ICIR': 0.091}, 'data_train_vec': ['2024-05-22', '2025-11-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.091', 'weight': '0.027'}

	Recorder: 7ec140d648f84c09a0ffd66d78c862c6

		Model: {'id': '7ec140d648f84c09a0ffd66d78c862c6', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.081, 'ICIR': 0.486, 'Rank IC': 0.059, 'Rank ICIR': 0.311}, 'data_train_vec': ['2025-05-22', '2026-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.311', 'weight': '0.091'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260522_14 717008191799711943 (Recorders: 2/5)

	Recorder: 65ef4a4f2cc8401a9648f3e8fd15def7

		Model: {'id': '65ef4a4f2cc8401a9648f3e8fd15def7', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.075, 'Rank IC': 0.032, 'Rank ICIR': 0.233}, 'data_train_vec': ['2023-05-22', '2025-08-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.233', 'weight': '0.068'}

	Recorder: 32dc289772f14fa7b0d8ded1aa6cbcdf

		Model: {'id': '32dc289772f14fa7b0d8ded1aa6cbcdf', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.349, 'Rank IC': 0.021, 'Rank ICIR': 0.135}, 'data_train_vec': ['2025-05-22', '2026-02-21'], 'train_time_vec': ['2026-05-22', '2026-05-22'], 'rank_icir': '0.135', 'weight': '0.039'}
