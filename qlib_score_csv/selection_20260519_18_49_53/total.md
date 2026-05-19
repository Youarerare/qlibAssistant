# params 
 {'predict_dates': [{'start': '2026-05-19', 'end': '2026-05-19'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260519_18 124695478743980401 (Recorders: 4/5)

	Recorder: 442ee42ca3694ab18d0b91632b094481

		Model: {'id': '442ee42ca3694ab18d0b91632b094481', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.085, 'Rank IC': 0.022, 'Rank ICIR': 0.143}, 'data_train_vec': ['2022-05-19', '2025-05-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.143', 'weight': '0.042'}

	Recorder: 4c00f1e7f08f47a69ce88441e6802d41

		Model: {'id': '4c00f1e7f08f47a69ce88441e6802d41', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.029, 'Rank IC': 0.032, 'Rank ICIR': 0.196}, 'data_train_vec': ['2023-05-19', '2025-08-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.196', 'weight': '0.058'}

	Recorder: caad41f86fb94d6ebfe551e4463dff74

		Model: {'id': 'caad41f86fb94d6ebfe551e4463dff74', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.142, 'Rank IC': 0.01, 'Rank ICIR': 0.092}, 'data_train_vec': ['2024-05-19', '2025-11-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.092', 'weight': '0.027'}

	Recorder: c9675b7254e5451392fdf5711ca6b0be

		Model: {'id': 'c9675b7254e5451392fdf5711ca6b0be', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.04, 'ICIR': 0.258, 'Rank IC': 0.037, 'Rank ICIR': 0.227}, 'data_train_vec': ['2025-05-19', '2026-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.227', 'weight': '0.067'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260519_18 631410633890459750 (Recorders: 3/5)

	Recorder: 57947763fa4f4630aa7173e5aa4764b8

		Model: {'id': '57947763fa4f4630aa7173e5aa4764b8', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.164, 'Rank IC': 0.029, 'Rank ICIR': 0.243}, 'data_train_vec': ['2023-05-19', '2025-08-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.243', 'weight': '0.072'}

	Recorder: ef28a476ff2940dfbd0b5a76e2805756

		Model: {'id': 'ef28a476ff2940dfbd0b5a76e2805756', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.133, 'Rank IC': 0.005, 'Rank ICIR': 0.05}, 'data_train_vec': ['2024-05-19', '2025-11-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.050', 'weight': '0.015'}

	Recorder: 47543e680de4425d8cf3f50c0411ef1c

		Model: {'id': '47543e680de4425d8cf3f50c0411ef1c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.09, 'ICIR': 0.577, 'Rank IC': 0.043, 'Rank ICIR': 0.257}, 'data_train_vec': ['2025-05-19', '2026-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.257', 'weight': '0.076'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260519_15 799735325723501835 (Recorders: 4/5)

	Recorder: 0fbb3dcaf11c47e790c5ef4f5a91c4d5

		Model: {'id': '0fbb3dcaf11c47e790c5ef4f5a91c4d5', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.028, 'Rank IC': 0.028, 'Rank ICIR': 0.178}, 'data_train_vec': ['2021-05-19', '2025-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.178', 'weight': '0.053'}

	Recorder: b5d1963e34e4421d908b487a29a82ceb

		Model: {'id': 'b5d1963e34e4421d908b487a29a82ceb', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.015, 'Rank IC': 0.032, 'Rank ICIR': 0.173}, 'data_train_vec': ['2022-05-19', '2025-05-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.173', 'weight': '0.051'}

	Recorder: f1c7c99fc49c4bb79ecf6b4ecdfcee85

		Model: {'id': 'f1c7c99fc49c4bb79ecf6b4ecdfcee85', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.141, 'Rank IC': 0.039, 'Rank ICIR': 0.25}, 'data_train_vec': ['2023-05-19', '2025-08-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.250', 'weight': '0.074'}

	Recorder: a7488acd6afe4a06abcbe09cccfb7047

		Model: {'id': 'a7488acd6afe4a06abcbe09cccfb7047', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.069, 'ICIR': 0.411, 'Rank IC': 0.036, 'Rank ICIR': 0.205}, 'data_train_vec': ['2025-05-19', '2026-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.205', 'weight': '0.061'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260519_15 745264730398643698 (Recorders: 4/5)

	Recorder: f2040f41bd83450ab22a7dedcb6b550a

		Model: {'id': 'f2040f41bd83450ab22a7dedcb6b550a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.063, 'Rank IC': 0.031, 'Rank ICIR': 0.276}, 'data_train_vec': ['2021-05-19', '2025-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.276', 'weight': '0.082'}

	Recorder: fb2704f5b19e4093a7c4e07c8c9ea5b4

		Model: {'id': 'fb2704f5b19e4093a7c4e07c8c9ea5b4', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.091, 'Rank IC': 0.036, 'Rank ICIR': 0.325}, 'data_train_vec': ['2023-05-19', '2025-08-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.325', 'weight': '0.096'}

	Recorder: c1826f5102f543c4a0fdad7c14470fdb

		Model: {'id': 'c1826f5102f543c4a0fdad7c14470fdb', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.044, 'Rank IC': 0.014, 'Rank ICIR': 0.123}, 'data_train_vec': ['2024-05-19', '2025-11-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.123', 'weight': '0.036'}

	Recorder: 779c8763a8944b75a10b16600e3f708b

		Model: {'id': '779c8763a8944b75a10b16600e3f708b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.071, 'ICIR': 0.513, 'Rank IC': 0.048, 'Rank ICIR': 0.3}, 'data_train_vec': ['2025-05-19', '2026-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.300', 'weight': '0.089'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260519_15 536162122964853656 (Recorders: 2/5)

	Recorder: bf32f069d54647fc9e2a74d424281486

		Model: {'id': 'bf32f069d54647fc9e2a74d424281486', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.022, 'Rank IC': 0.024, 'Rank ICIR': 0.148}, 'data_train_vec': ['2023-05-19', '2025-08-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.148', 'weight': '0.044'}

	Recorder: 91676830807048d5967db682b8a330ce

		Model: {'id': '91676830807048d5967db682b8a330ce', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.235, 'Rank IC': 0.031, 'Rank ICIR': 0.193}, 'data_train_vec': ['2025-05-19', '2026-02-18'], 'train_time_vec': ['2026-05-19', '2026-05-19'], 'rank_icir': '0.193', 'weight': '0.057'}
