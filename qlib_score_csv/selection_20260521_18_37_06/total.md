# params 
 {'predict_dates': [{'start': '2026-05-21', 'end': '2026-05-21'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260521_18 131434498216793850 (Recorders: 3/5)

	Recorder: 288296c8d77948b1a0f5d0ba999c7e81

		Model: {'id': '288296c8d77948b1a0f5d0ba999c7e81', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.035, 'Rank IC': 0.018, 'Rank ICIR': 0.133}, 'data_train_vec': ['2022-05-21', '2025-05-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.133', 'weight': '0.050'}

	Recorder: f1bac8f3aa8c41d28bdb16d8db1a707b

		Model: {'id': 'f1bac8f3aa8c41d28bdb16d8db1a707b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.077, 'Rank IC': 0.024, 'Rank ICIR': 0.141}, 'data_train_vec': ['2023-05-21', '2025-08-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.141', 'weight': '0.053'}

	Recorder: d554aa29b180414aa711cb63b68fdc5b

		Model: {'id': 'd554aa29b180414aa711cb63b68fdc5b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.046, 'ICIR': 0.256, 'Rank IC': 0.014, 'Rank ICIR': 0.088}, 'data_train_vec': ['2025-05-21', '2026-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.088', 'weight': '0.033'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260521_18 131915387675051973 (Recorders: 3/5)

	Recorder: 01123d88254a474fbfe2962c0416e67d

		Model: {'id': '01123d88254a474fbfe2962c0416e67d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.081, 'Rank IC': 0.02, 'Rank ICIR': 0.156}, 'data_train_vec': ['2023-05-21', '2025-08-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.156', 'weight': '0.058'}

	Recorder: df58175a43224ec4a5009b0f1755f20b

		Model: {'id': 'df58175a43224ec4a5009b0f1755f20b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.194, 'Rank IC': 0.01, 'Rank ICIR': 0.097}, 'data_train_vec': ['2024-05-21', '2025-11-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.097', 'weight': '0.036'}

	Recorder: 031e52d5ff9e41cdb4c8eb226961d937

		Model: {'id': '031e52d5ff9e41cdb4c8eb226961d937', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.066, 'ICIR': 0.378, 'Rank IC': 0.022, 'Rank ICIR': 0.117}, 'data_train_vec': ['2025-05-21', '2026-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.117', 'weight': '0.044'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260521_15 821800818388276346 (Recorders: 4/5)

	Recorder: 8fcd998ad4154fc392c3e942da9aa45d

		Model: {'id': '8fcd998ad4154fc392c3e942da9aa45d', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.052, 'Rank IC': 0.032, 'Rank ICIR': 0.204}, 'data_train_vec': ['2021-05-21', '2025-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.204', 'weight': '0.076'}

	Recorder: 1cca7f4b5c6448db91e7f1405b8460f2

		Model: {'id': '1cca7f4b5c6448db91e7f1405b8460f2', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.028, 'Rank IC': 0.034, 'Rank ICIR': 0.191}, 'data_train_vec': ['2022-05-21', '2025-05-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.191', 'weight': '0.071'}

	Recorder: b365e8d9134b4124b108cff3e34b0c1b

		Model: {'id': 'b365e8d9134b4124b108cff3e34b0c1b', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.157, 'Rank IC': 0.04, 'Rank ICIR': 0.273}, 'data_train_vec': ['2023-05-21', '2025-08-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.273', 'weight': '0.102'}

	Recorder: 1ce20631a82d4094acbbb1888eac56fe

		Model: {'id': '1ce20631a82d4094acbbb1888eac56fe', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.045, 'ICIR': 0.283, 'Rank IC': 0.014, 'Rank ICIR': 0.08}, 'data_train_vec': ['2025-05-21', '2026-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.080', 'weight': '0.030'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260521_15 463324764898195037 (Recorders: 3/5)

	Recorder: 8f7fc384190241749f2105c00c2a2c3a

		Model: {'id': '8f7fc384190241749f2105c00c2a2c3a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.06, 'Rank IC': 0.029, 'Rank ICIR': 0.264}, 'data_train_vec': ['2021-05-21', '2025-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.264', 'weight': '0.099'}

	Recorder: 487f82c245034c59a1088225bae35c71

		Model: {'id': '487f82c245034c59a1088225bae35c71', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.074, 'Rank IC': 0.033, 'Rank ICIR': 0.314}, 'data_train_vec': ['2023-05-21', '2025-08-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.314', 'weight': '0.117'}

	Recorder: 4f31d7f2d88b419c88cefaba4e4bcb42

		Model: {'id': '4f31d7f2d88b419c88cefaba4e4bcb42', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.059, 'ICIR': 0.404, 'Rank IC': 0.033, 'Rank ICIR': 0.198}, 'data_train_vec': ['2025-05-21', '2026-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.198', 'weight': '0.074'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260521_15 714097645999101708 (Recorders: 2/5)

	Recorder: e847e9bbea8e44cb8aec2c1613dbd487

		Model: {'id': 'e847e9bbea8e44cb8aec2c1613dbd487', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.095, 'Rank IC': 0.032, 'Rank ICIR': 0.222}, 'data_train_vec': ['2023-05-21', '2025-08-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.222', 'weight': '0.083'}

	Recorder: 4b7dcc606ca84d8a88e9fdfd9f343391

		Model: {'id': '4b7dcc606ca84d8a88e9fdfd9f343391', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.307, 'Rank IC': 0.028, 'Rank ICIR': 0.201}, 'data_train_vec': ['2025-05-21', '2026-02-20'], 'train_time_vec': ['2026-05-21', '2026-05-21'], 'rank_icir': '0.201', 'weight': '0.075'}
