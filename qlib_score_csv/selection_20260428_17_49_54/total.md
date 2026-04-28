# params 
 {'predict_dates': [{'start': '2026-04-28', 'end': '2026-04-28'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260428_17 258319408884176666 (Recorders: 3/5)

	Recorder: 4255b005b55a4e6782b4a24080e5f014

		Model: {'id': '4255b005b55a4e6782b4a24080e5f014', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.075, 'Rank IC': 0.027, 'Rank ICIR': 0.191}, 'data_train_vec': ['2023-04-28', '2025-07-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.191', 'weight': '0.068'}

	Recorder: 95bdf97a93b8485f900a0046f62d3de0

		Model: {'id': '95bdf97a93b8485f900a0046f62d3de0', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.082, 'Rank IC': 0.017, 'Rank ICIR': 0.169}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.169', 'weight': '0.060'}

	Recorder: 4e4e1b8c928a4c1cbb26a5ce84b71e42

		Model: {'id': '4e4e1b8c928a4c1cbb26a5ce84b71e42', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.033, 'ICIR': 0.288, 'Rank IC': 0.036, 'Rank ICIR': 0.269}, 'data_train_vec': ['2025-04-28', '2026-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.269', 'weight': '0.096'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260428_17 463354941055057560 (Recorders: 3/5)

	Recorder: 1505d0a8da8943aaa409ba0ad5fbb6ea

		Model: {'id': '1505d0a8da8943aaa409ba0ad5fbb6ea', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.085, 'Rank IC': 0.032, 'Rank ICIR': 0.208}, 'data_train_vec': ['2023-04-28', '2025-07-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.208', 'weight': '0.074'}

	Recorder: ecd37ecfe0e144b9b8f9e2dfc5f8401f

		Model: {'id': 'ecd37ecfe0e144b9b8f9e2dfc5f8401f', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.086, 'Rank IC': 0.013, 'Rank ICIR': 0.118}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.118', 'weight': '0.042'}

	Recorder: 56135da8687a492a935f5a5328f383e1

		Model: {'id': '56135da8687a492a935f5a5328f383e1', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.424, 'Rank IC': 0.03, 'Rank ICIR': 0.214}, 'data_train_vec': ['2025-04-28', '2026-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.214', 'weight': '0.076'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260428_14 630630220853057218 (Recorders: 3/5)

	Recorder: eb4397be7eb1479c831090b7e6651285

		Model: {'id': 'eb4397be7eb1479c831090b7e6651285', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.086, 'Rank IC': 0.044, 'Rank ICIR': 0.268}, 'data_train_vec': ['2023-04-28', '2025-07-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.268', 'weight': '0.096'}

	Recorder: e97be3fadf514b148522ba49c69bf6b3

		Model: {'id': 'e97be3fadf514b148522ba49c69bf6b3', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.149, 'Rank IC': 0.014, 'Rank ICIR': 0.13}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.130', 'weight': '0.046'}

	Recorder: 4a9c15c8706c4499988f2d4300d31787

		Model: {'id': '4a9c15c8706c4499988f2d4300d31787', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.03, 'ICIR': 0.184, 'Rank IC': 0.009, 'Rank ICIR': 0.049}, 'data_train_vec': ['2025-04-28', '2026-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.049', 'weight': '0.018'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260428_14 426981851033935386 (Recorders: 3/5)

	Recorder: 4269443c36314597aa202c3217e595a7

		Model: {'id': '4269443c36314597aa202c3217e595a7', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.03, 'Rank IC': 0.029, 'Rank ICIR': 0.246}, 'data_train_vec': ['2023-04-28', '2025-07-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.246', 'weight': '0.088'}

	Recorder: 12d5b48019554e79991f63303bd0fc8f

		Model: {'id': '12d5b48019554e79991f63303bd0fc8f', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.013, 'Rank IC': 0.009, 'Rank ICIR': 0.075}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.075', 'weight': '0.027'}

	Recorder: 8ee9222bc17c4296b990231fa5f2470a

		Model: {'id': '8ee9222bc17c4296b990231fa5f2470a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.066, 'ICIR': 0.579, 'Rank IC': 0.043, 'Rank ICIR': 0.328}, 'data_train_vec': ['2025-04-28', '2026-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.328', 'weight': '0.117'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260428_14 299366799993149234 (Recorders: 3/5)

	Recorder: 07f90b6bd7464fa9b4515bb11d2988b4

		Model: {'id': '07f90b6bd7464fa9b4515bb11d2988b4', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.001, 'ICIR': 0.009, 'Rank IC': 0.018, 'Rank ICIR': 0.102}, 'data_train_vec': ['2021-04-28', '2025-01-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.102', 'weight': '0.036'}

	Recorder: 386e640e74b441748b29cbcea0e33331

		Model: {'id': '386e640e74b441748b29cbcea0e33331', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.074, 'Rank IC': 0.037, 'Rank ICIR': 0.224}, 'data_train_vec': ['2023-04-28', '2025-07-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.224', 'weight': '0.080'}

	Recorder: 304e772b0e55478780a59fc2809b8f37

		Model: {'id': '304e772b0e55478780a59fc2809b8f37', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.075, 'Rank IC': 0.024, 'Rank ICIR': 0.207}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-28', '2026-04-28'], 'rank_icir': '0.207', 'weight': '0.074'}
