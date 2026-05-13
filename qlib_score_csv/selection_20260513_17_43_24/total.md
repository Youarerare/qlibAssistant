# params 
 {'predict_dates': [{'start': '2026-05-13', 'end': '2026-05-13'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260513_17 878168104177806619 (Recorders: 2/5)

	Recorder: 63a26fd519b44bab8e21836321c780f4

		Model: {'id': '63a26fd519b44bab8e21836321c780f4', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.02, 'Rank IC': 0.004, 'Rank ICIR': 0.032}, 'data_train_vec': ['2024-05-13', '2025-11-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.032', 'weight': '0.013'}

	Recorder: f629678ca23d4b35addf9123f0c31872

		Model: {'id': 'f629678ca23d4b35addf9123f0c31872', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.085, 'ICIR': 0.779, 'Rank IC': 0.047, 'Rank ICIR': 0.425}, 'data_train_vec': ['2025-05-13', '2026-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.425', 'weight': '0.169'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260513_17 941854002428210503 (Recorders: 3/5)

	Recorder: 398a7049a4584a219db99bfab37ded23

		Model: {'id': '398a7049a4584a219db99bfab37ded23', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.017, 'ICIR': 0.179, 'Rank IC': 0.024, 'Rank ICIR': 0.206}, 'data_train_vec': ['2023-05-13', '2025-08-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.206', 'weight': '0.082'}

	Recorder: a10fca719405436a8d04ede683a0957d

		Model: {'id': 'a10fca719405436a8d04ede683a0957d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.197, 'Rank IC': 0.003, 'Rank ICIR': 0.025}, 'data_train_vec': ['2024-05-13', '2025-11-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.025', 'weight': '0.010'}

	Recorder: 0cc1e711b97548a58f11e38c41fe1b10

		Model: {'id': '0cc1e711b97548a58f11e38c41fe1b10', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.097, 'ICIR': 0.678, 'Rank IC': 0.045, 'Rank ICIR': 0.325}, 'data_train_vec': ['2025-05-13', '2026-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.325', 'weight': '0.129'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260513_15 928773009440902926 (Recorders: 2/5)

	Recorder: 203bc8ab94e1447fbe7de353b93083bf

		Model: {'id': '203bc8ab94e1447fbe7de353b93083bf', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.082, 'Rank IC': 0.029, 'Rank ICIR': 0.181}, 'data_train_vec': ['2023-05-13', '2025-08-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.181', 'weight': '0.072'}

	Recorder: e45961a8ae64459f8c20016bcaca7262

		Model: {'id': 'e45961a8ae64459f8c20016bcaca7262', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.073, 'ICIR': 0.598, 'Rank IC': 0.035, 'Rank ICIR': 0.286}, 'data_train_vec': ['2025-05-13', '2026-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.286', 'weight': '0.113'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260513_14 605972475556646483 (Recorders: 3/5)

	Recorder: d93f009695a44ac691f17216c38c8e99

		Model: {'id': 'd93f009695a44ac691f17216c38c8e99', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.017, 'Rank IC': 0.026, 'Rank ICIR': 0.234}, 'data_train_vec': ['2023-05-13', '2025-08-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.234', 'weight': '0.093'}

	Recorder: 3b612d4a5e724708a89932788f20f664

		Model: {'id': '3b612d4a5e724708a89932788f20f664', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.124, 'Rank IC': 0.024, 'Rank ICIR': 0.21}, 'data_train_vec': ['2024-05-13', '2025-11-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.210', 'weight': '0.083'}

	Recorder: 5aae075ac3c94a52b112510d790f3f9c

		Model: {'id': '5aae075ac3c94a52b112510d790f3f9c', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.074, 'ICIR': 0.631, 'Rank IC': 0.047, 'Rank ICIR': 0.387}, 'data_train_vec': ['2025-05-13', '2026-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.387', 'weight': '0.154'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260513_14 428636587889287483 (Recorders: 1/5)

	Recorder: ea9748af82fa42079a3729ff48801e1d

		Model: {'id': 'ea9748af82fa42079a3729ff48801e1d', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.048, 'ICIR': 0.407, 'Rank IC': 0.022, 'Rank ICIR': 0.209}, 'data_train_vec': ['2025-05-13', '2026-02-12'], 'train_time_vec': ['2026-05-13', '2026-05-13'], 'rank_icir': '0.209', 'weight': '0.083'}
