# params 
 {'predict_dates': [{'start': '2026-05-25', 'end': '2026-05-25'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260525_17 131367843448656645 (Recorders: 3/5)

	Recorder: ea3544559a7746a8afafcb12c5e0a34d

		Model: {'id': 'ea3544559a7746a8afafcb12c5e0a34d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.076, 'Rank IC': 0.031, 'Rank ICIR': 0.22}, 'data_train_vec': ['2021-05-25', '2025-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.220', 'weight': '0.057'}

	Recorder: 8588ef4a59634435a860063eb610fbdf

		Model: {'id': '8588ef4a59634435a860063eb610fbdf', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.237, 'Rank IC': 0.034, 'Rank ICIR': 0.24}, 'data_train_vec': ['2023-05-25', '2025-08-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.240', 'weight': '0.063'}

	Recorder: 6a999d3f0ea345419ff6f8ef33d9a089

		Model: {'id': '6a999d3f0ea345419ff6f8ef33d9a089', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.071, 'ICIR': 0.363, 'Rank IC': 0.05, 'Rank ICIR': 0.29}, 'data_train_vec': ['2025-05-25', '2026-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.290', 'weight': '0.076'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260525_17 443725994244444697 (Recorders: 3/5)

	Recorder: dc0ceca46d374e8da8ccbc03f393ab5b

		Model: {'id': 'dc0ceca46d374e8da8ccbc03f393ab5b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.082, 'Rank IC': 0.022, 'Rank ICIR': 0.17}, 'data_train_vec': ['2023-05-25', '2025-08-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.170', 'weight': '0.044'}

	Recorder: d6bc9c00f6ea4a40aa161b414862cc3c

		Model: {'id': 'd6bc9c00f6ea4a40aa161b414862cc3c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.173, 'Rank IC': 0.005, 'Rank ICIR': 0.041}, 'data_train_vec': ['2024-05-25', '2025-11-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.041', 'weight': '0.011'}

	Recorder: e8e79ab9c7584c7b831ad0817a8a8056

		Model: {'id': 'e8e79ab9c7584c7b831ad0817a8a8056', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.095, 'ICIR': 0.536, 'Rank IC': 0.052, 'Rank ICIR': 0.273}, 'data_train_vec': ['2025-05-25', '2026-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.273', 'weight': '0.071'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260525_15 573230976786950259 (Recorders: 4/5)

	Recorder: 03c8da9dc0a74659a4d292ce3afafa9b

		Model: {'id': '03c8da9dc0a74659a4d292ce3afafa9b', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.07, 'Rank IC': 0.034, 'Rank ICIR': 0.232}, 'data_train_vec': ['2021-05-25', '2025-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.232', 'weight': '0.060'}

	Recorder: 3e7c45dc86ef4177912edaa8e338ced4

		Model: {'id': '3e7c45dc86ef4177912edaa8e338ced4', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.034, 'Rank IC': 0.037, 'Rank ICIR': 0.207}, 'data_train_vec': ['2022-05-25', '2025-05-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.207', 'weight': '0.054'}

	Recorder: acbaa08612304c79ac368ca7252f9d2e

		Model: {'id': 'acbaa08612304c79ac368ca7252f9d2e', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.191, 'Rank IC': 0.039, 'Rank ICIR': 0.267}, 'data_train_vec': ['2023-05-25', '2025-08-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.267', 'weight': '0.070'}

	Recorder: 01c2fcb5845345449f72861c4890636e

		Model: {'id': '01c2fcb5845345449f72861c4890636e', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.074, 'ICIR': 0.387, 'Rank IC': 0.049, 'Rank ICIR': 0.253}, 'data_train_vec': ['2025-05-25', '2026-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.253', 'weight': '0.066'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260525_15 439953432222685548 (Recorders: 4/5)

	Recorder: b451694a0ecd4aed8b941d18ed523bb4

		Model: {'id': 'b451694a0ecd4aed8b941d18ed523bb4', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.063, 'Rank IC': 0.031, 'Rank ICIR': 0.277}, 'data_train_vec': ['2021-05-25', '2025-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.277', 'weight': '0.072'}

	Recorder: 289bcbd97cea4d669cfdcc988d26a69b

		Model: {'id': '289bcbd97cea4d669cfdcc988d26a69b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.094, 'Rank IC': 0.036, 'Rank ICIR': 0.329}, 'data_train_vec': ['2023-05-25', '2025-08-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.329', 'weight': '0.086'}

	Recorder: 86fde0fb68e649fdb6455916300e06c7

		Model: {'id': '86fde0fb68e649fdb6455916300e06c7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.015, 'Rank IC': 0.01, 'Rank ICIR': 0.079}, 'data_train_vec': ['2024-05-25', '2025-11-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.079', 'weight': '0.021'}

	Recorder: 7db699cafc274c01ab2bb5d0ad9d594b

		Model: {'id': '7db699cafc274c01ab2bb5d0ad9d594b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.11, 'ICIR': 0.624, 'Rank IC': 0.089, 'Rank ICIR': 0.45}, 'data_train_vec': ['2025-05-25', '2026-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.450', 'weight': '0.117'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260525_15 756034339088639119 (Recorders: 2/5)

	Recorder: ad136cc8152c4294abe4dc0d76dc677b

		Model: {'id': 'ad136cc8152c4294abe4dc0d76dc677b', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.13, 'Rank IC': 0.034, 'Rank ICIR': 0.215}, 'data_train_vec': ['2023-05-25', '2025-08-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.215', 'weight': '0.056'}

	Recorder: 799e90b5cd7c4e60b230c0684ba94c42

		Model: {'id': '799e90b5cd7c4e60b230c0684ba94c42', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.059, 'ICIR': 0.32, 'Rank IC': 0.042, 'Rank ICIR': 0.295}, 'data_train_vec': ['2025-05-25', '2026-02-24'], 'train_time_vec': ['2026-05-25', '2026-05-25'], 'rank_icir': '0.295', 'weight': '0.077'}
