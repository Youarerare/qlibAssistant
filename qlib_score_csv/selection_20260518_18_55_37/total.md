# params 
 {'predict_dates': [{'start': '2026-05-18', 'end': '2026-05-18'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260518_18 578098294942873518 (Recorders: 4/5)

	Recorder: 83d4a21219474746a1e10a47f3dc9207

		Model: {'id': '83d4a21219474746a1e10a47f3dc9207', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.095, 'Rank IC': 0.016, 'Rank ICIR': 0.12}, 'data_train_vec': ['2021-05-18', '2025-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.120', 'weight': '0.041'}

	Recorder: 54c2e3f5f679401f9203740b8e724c89

		Model: {'id': '54c2e3f5f679401f9203740b8e724c89', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.059, 'Rank IC': 0.014, 'Rank ICIR': 0.09}, 'data_train_vec': ['2022-05-18', '2025-05-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.090', 'weight': '0.030'}

	Recorder: ab497d14492f4a9da53ab3de0245f06d

		Model: {'id': 'ab497d14492f4a9da53ab3de0245f06d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.092, 'Rank IC': 0.023, 'Rank ICIR': 0.147}, 'data_train_vec': ['2023-05-18', '2025-08-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.147', 'weight': '0.050'}

	Recorder: 5cc880e3ae5448a28821ea0e24c82c66

		Model: {'id': '5cc880e3ae5448a28821ea0e24c82c66', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.272, 'Rank IC': 0.039, 'Rank ICIR': 0.232}, 'data_train_vec': ['2025-05-18', '2026-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.232', 'weight': '0.078'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260518_18 429647563139463720 (Recorders: 3/5)

	Recorder: 75abd8cb1c914b2f838934be4a195070

		Model: {'id': '75abd8cb1c914b2f838934be4a195070', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.143, 'Rank IC': 0.026, 'Rank ICIR': 0.203}, 'data_train_vec': ['2023-05-18', '2025-08-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.203', 'weight': '0.069'}

	Recorder: 0b409c8efde8416d927ed527bce5e84a

		Model: {'id': '0b409c8efde8416d927ed527bce5e84a', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.114, 'Rank IC': 0.003, 'Rank ICIR': 0.034}, 'data_train_vec': ['2024-05-18', '2025-11-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.034', 'weight': '0.012'}

	Recorder: 6af2647a138b468ba6bdc31a614daf13

		Model: {'id': '6af2647a138b468ba6bdc31a614daf13', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.095, 'ICIR': 0.595, 'Rank IC': 0.048, 'Rank ICIR': 0.277}, 'data_train_vec': ['2025-05-18', '2026-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.277', 'weight': '0.094'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260518_16 946859380545706600 (Recorders: 3/5)

	Recorder: cd5187e8e95e480e9a310694efc596aa

		Model: {'id': 'cd5187e8e95e480e9a310694efc596aa', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.001, 'ICIR': 0.007, 'Rank IC': 0.028, 'Rank ICIR': 0.159}, 'data_train_vec': ['2022-05-18', '2025-05-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.159', 'weight': '0.054'}

	Recorder: aa6f741f6e2943f7a2defaecd24d2675

		Model: {'id': 'aa6f741f6e2943f7a2defaecd24d2675', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.092, 'Rank IC': 0.035, 'Rank ICIR': 0.225}, 'data_train_vec': ['2023-05-18', '2025-08-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.225', 'weight': '0.076'}

	Recorder: 5e8f1e5cb49d4aae9aca9c62058eba78

		Model: {'id': '5e8f1e5cb49d4aae9aca9c62058eba78', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.067, 'ICIR': 0.382, 'Rank IC': 0.032, 'Rank ICIR': 0.171}, 'data_train_vec': ['2025-05-18', '2026-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.171', 'weight': '0.058'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260518_15 104649162615313434 (Recorders: 4/5)

	Recorder: 322665ae0bca4def8ceed0b9c47ca2d8

		Model: {'id': '322665ae0bca4def8ceed0b9c47ca2d8', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.035, 'Rank IC': 0.027, 'Rank ICIR': 0.241}, 'data_train_vec': ['2021-05-18', '2025-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.241', 'weight': '0.082'}

	Recorder: b6b69a1648d74009a3b41fde46d9a583

		Model: {'id': 'b6b69a1648d74009a3b41fde46d9a583', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.071, 'Rank IC': 0.034, 'Rank ICIR': 0.304}, 'data_train_vec': ['2023-05-18', '2025-08-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.304', 'weight': '0.103'}

	Recorder: 9ded49f0d62b46308099ec3f5ba73c1a

		Model: {'id': '9ded49f0d62b46308099ec3f5ba73c1a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.04, 'Rank IC': 0.015, 'Rank ICIR': 0.132}, 'data_train_vec': ['2024-05-18', '2025-11-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.132', 'weight': '0.045'}

	Recorder: 17e7eee63d8d4833830f1efed91c002d

		Model: {'id': '17e7eee63d8d4833830f1efed91c002d', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.069, 'ICIR': 0.485, 'Rank IC': 0.043, 'Rank ICIR': 0.265}, 'data_train_vec': ['2025-05-18', '2026-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.265', 'weight': '0.090'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260518_15 447918028946122604 (Recorders: 2/5)

	Recorder: fd240e7508104b40887bab5022e24616

		Model: {'id': 'fd240e7508104b40887bab5022e24616', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.082, 'Rank IC': 0.027, 'Rank ICIR': 0.169}, 'data_train_vec': ['2023-05-18', '2025-08-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.169', 'weight': '0.057'}

	Recorder: 9d3929ad34a740699569cd620b526d44

		Model: {'id': '9d3929ad34a740699569cd620b526d44', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.034, 'ICIR': 0.217, 'Rank IC': 0.031, 'Rank ICIR': 0.187}, 'data_train_vec': ['2025-05-18', '2026-02-17'], 'train_time_vec': ['2026-05-18', '2026-05-18'], 'rank_icir': '0.187', 'weight': '0.063'}
