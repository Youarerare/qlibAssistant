# params 
 {'predict_dates': [{'start': '2026-05-08', 'end': '2026-05-08'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260508_16 126255021661170698 (Recorders: 2/5)

	Recorder: 126d1349a11948439ec17b95b94f9f10

		Model: {'id': '126d1349a11948439ec17b95b94f9f10', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.131, 'Rank IC': 0.039, 'Rank ICIR': 0.239}, 'data_train_vec': ['2023-05-08', '2025-08-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.239', 'weight': '0.094'}

	Recorder: 1a9c76462cd743b3b9cc07534cd8d7a1

		Model: {'id': '1a9c76462cd743b3b9cc07534cd8d7a1', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.235, 'Rank IC': 0.02, 'Rank ICIR': 0.146}, 'data_train_vec': ['2025-05-08', '2026-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.146', 'weight': '0.057'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260508_16 190842428816790462 (Recorders: 2/5)

	Recorder: 2b3547edd42944f29ccbc53f94056817

		Model: {'id': '2b3547edd42944f29ccbc53f94056817', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.159, 'Rank IC': 0.019, 'Rank ICIR': 0.157}, 'data_train_vec': ['2024-05-08', '2025-11-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.157', 'weight': '0.062'}

	Recorder: c5f8a1b42ef74ab59a2de79219c08953

		Model: {'id': 'c5f8a1b42ef74ab59a2de79219c08953', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.075, 'ICIR': 0.508, 'Rank IC': 0.02, 'Rank ICIR': 0.146}, 'data_train_vec': ['2025-05-08', '2026-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.146', 'weight': '0.057'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260508_14 771571750860020829 (Recorders: 3/5)

	Recorder: 10e30b75539c4412a3abea7a11af2a29

		Model: {'id': '10e30b75539c4412a3abea7a11af2a29', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.04, 'Rank IC': 0.031, 'Rank ICIR': 0.175}, 'data_train_vec': ['2022-05-08', '2025-05-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.175', 'weight': '0.069'}

	Recorder: 512d83465bcc42f9a5270dfcefc0e8d3

		Model: {'id': '512d83465bcc42f9a5270dfcefc0e8d3', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.028, 'Rank IC': 0.03, 'Rank ICIR': 0.179}, 'data_train_vec': ['2023-05-08', '2025-08-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.179', 'weight': '0.070'}

	Recorder: e604a1110f614bf1bd30c1ce42d3fd1a

		Model: {'id': 'e604a1110f614bf1bd30c1ce42d3fd1a', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.445, 'Rank IC': 0.018, 'Rank ICIR': 0.142}, 'data_train_vec': ['2025-05-08', '2026-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.142', 'weight': '0.056'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260508_14 308956777742822370 (Recorders: 4/5)

	Recorder: bf161d6925c44558895eea7a5a7fb4ea

		Model: {'id': 'bf161d6925c44558895eea7a5a7fb4ea', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.03, 'Rank IC': 0.019, 'Rank ICIR': 0.17}, 'data_train_vec': ['2021-05-08', '2025-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.170', 'weight': '0.067'}

	Recorder: 6399a4ab42ce4bd5962f08222d6d1484

		Model: {'id': '6399a4ab42ce4bd5962f08222d6d1484', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.012, 'Rank IC': 0.026, 'Rank ICIR': 0.209}, 'data_train_vec': ['2022-05-08', '2025-05-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.209', 'weight': '0.082'}

	Recorder: 7eaf59712959457d83041310558e4ec5

		Model: {'id': '7eaf59712959457d83041310558e4ec5', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.058, 'Rank IC': 0.02, 'Rank ICIR': 0.181}, 'data_train_vec': ['2024-05-08', '2025-11-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.181', 'weight': '0.071'}

	Recorder: 3ba84f646dca4dfcb704546e464a8d17

		Model: {'id': '3ba84f646dca4dfcb704546e464a8d17', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.054, 'ICIR': 0.513, 'Rank IC': 0.023, 'Rank ICIR': 0.19}, 'data_train_vec': ['2025-05-08', '2026-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.190', 'weight': '0.075'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260508_14 606632688829644283 (Recorders: 3/5)

	Recorder: de23ab6abad448f19cc7f0496d0ec546

		Model: {'id': 'de23ab6abad448f19cc7f0496d0ec546', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.015, 'Rank IC': 0.022, 'Rank ICIR': 0.131}, 'data_train_vec': ['2023-05-08', '2025-08-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.131', 'weight': '0.051'}

	Recorder: b9ac725e623847c18a34acc71f0cdcb9

		Model: {'id': 'b9ac725e623847c18a34acc71f0cdcb9', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.027, 'Rank IC': 0.012, 'Rank ICIR': 0.099}, 'data_train_vec': ['2024-05-08', '2025-11-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.099', 'weight': '0.039'}

	Recorder: f33338389a044b40b04a115904872939

		Model: {'id': 'f33338389a044b40b04a115904872939', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.072, 'ICIR': 0.622, 'Rank IC': 0.042, 'Rank ICIR': 0.382}, 'data_train_vec': ['2025-05-08', '2026-02-07'], 'train_time_vec': ['2026-05-08', '2026-05-08'], 'rank_icir': '0.382', 'weight': '0.150'}
