# params 
 {'predict_dates': [{'start': '2026-05-27', 'end': '2026-05-27'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260527_18 130419723602618565 (Recorders: 3/5)

	Recorder: ab3153e215a14a07b05347d5579e2e83

		Model: {'id': 'ab3153e215a14a07b05347d5579e2e83', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.017, 'Rank IC': 0.021, 'Rank ICIR': 0.14}, 'data_train_vec': ['2022-05-27', '2025-05-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.140', 'weight': '0.043'}

	Recorder: 0689e501ff1b42db97edd5689a68f834

		Model: {'id': '0689e501ff1b42db97edd5689a68f834', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.018, 'Rank IC': 0.028, 'Rank ICIR': 0.16}, 'data_train_vec': ['2023-05-27', '2025-08-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.160', 'weight': '0.050'}

	Recorder: 5f1d5348a22944cdab1495c5846cb2c9

		Model: {'id': '5f1d5348a22944cdab1495c5846cb2c9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.061, 'ICIR': 0.259, 'Rank IC': 0.032, 'Rank ICIR': 0.154}, 'data_train_vec': ['2025-05-27', '2026-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.154', 'weight': '0.048'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260527_18 318880621064625923 (Recorders: 3/5)

	Recorder: ccf4f541fa42497d9aa126d8451f6f71

		Model: {'id': 'ccf4f541fa42497d9aa126d8451f6f71', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.184, 'Rank IC': 0.031, 'Rank ICIR': 0.236}, 'data_train_vec': ['2023-05-27', '2025-08-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.236', 'weight': '0.073'}

	Recorder: 9a31691e895d4aeab25f86eed49ed7e1

		Model: {'id': '9a31691e895d4aeab25f86eed49ed7e1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.11, 'Rank IC': 0.011, 'Rank ICIR': 0.107}, 'data_train_vec': ['2024-05-27', '2025-11-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.107', 'weight': '0.033'}

	Recorder: 1ba23db2d9a2454d93bbce603f81601c

		Model: {'id': '1ba23db2d9a2454d93bbce603f81601c', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.09, 'ICIR': 0.482, 'Rank IC': 0.047, 'Rank ICIR': 0.243}, 'data_train_vec': ['2025-05-27', '2026-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.243', 'weight': '0.075'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260527_16 319635658977033844 (Recorders: 4/5)

	Recorder: a8d64ba2833a482da6abcaf866d9128b

		Model: {'id': 'a8d64ba2833a482da6abcaf866d9128b', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.046, 'Rank IC': 0.031, 'Rank ICIR': 0.202}, 'data_train_vec': ['2021-05-27', '2025-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.202', 'weight': '0.063'}

	Recorder: 4d4a97d7f0504f478c0f4007862cbe56

		Model: {'id': '4d4a97d7f0504f478c0f4007862cbe56', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.076, 'Rank IC': 0.041, 'Rank ICIR': 0.227}, 'data_train_vec': ['2022-05-27', '2025-05-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.227', 'weight': '0.070'}

	Recorder: b10951e7d83b4635990722387643ff11

		Model: {'id': 'b10951e7d83b4635990722387643ff11', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.203, 'Rank IC': 0.044, 'Rank ICIR': 0.279}, 'data_train_vec': ['2023-05-27', '2025-08-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.279', 'weight': '0.086'}

	Recorder: 40b0aeb019404810aff546eaa570e6e7

		Model: {'id': '40b0aeb019404810aff546eaa570e6e7', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.053, 'ICIR': 0.295, 'Rank IC': 0.021, 'Rank ICIR': 0.111}, 'data_train_vec': ['2025-05-27', '2026-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.111', 'weight': '0.034'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260527_16 519060634921340831 (Recorders: 3/5)

	Recorder: 0f152ac73dd64040a5b9c72208e8292e

		Model: {'id': '0f152ac73dd64040a5b9c72208e8292e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.06, 'Rank IC': 0.034, 'Rank ICIR': 0.292}, 'data_train_vec': ['2021-05-27', '2025-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.292', 'weight': '0.091'}

	Recorder: dd1946a4d5e54778b0274c64a601f58b

		Model: {'id': 'dd1946a4d5e54778b0274c64a601f58b', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.118, 'Rank IC': 0.036, 'Rank ICIR': 0.326}, 'data_train_vec': ['2023-05-27', '2025-08-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.326', 'weight': '0.101'}

	Recorder: 5f2d68b7be554a6ba94a7e31f389a661

		Model: {'id': '5f2d68b7be554a6ba94a7e31f389a661', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.092, 'ICIR': 0.507, 'Rank IC': 0.067, 'Rank ICIR': 0.319}, 'data_train_vec': ['2025-05-27', '2026-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.319', 'weight': '0.099'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260527_16 243658502533888178 (Recorders: 2/5)

	Recorder: 015d643e43a6459e90e46695b6450777

		Model: {'id': '015d643e43a6459e90e46695b6450777', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.09, 'Rank IC': 0.028, 'Rank ICIR': 0.174}, 'data_train_vec': ['2023-05-27', '2025-08-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.174', 'weight': '0.054'}

	Recorder: 15ba3498f72e4684a3500332d6774c41

		Model: {'id': '15ba3498f72e4684a3500332d6774c41', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.314, 'Rank IC': 0.042, 'Rank ICIR': 0.256}, 'data_train_vec': ['2025-05-27', '2026-02-26'], 'train_time_vec': ['2026-05-27', '2026-05-27'], 'rank_icir': '0.256', 'weight': '0.079'}
