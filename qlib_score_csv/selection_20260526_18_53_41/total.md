# params 
 {'predict_dates': [{'start': '2026-05-26', 'end': '2026-05-26'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260526_18 286382106525717723 (Recorders: 3/5)

	Recorder: 3ea728864f0d41b083c7c883e2b8bf0a

		Model: {'id': '3ea728864f0d41b083c7c883e2b8bf0a', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.032, 'Rank IC': 0.029, 'Rank ICIR': 0.167}, 'data_train_vec': ['2022-05-26', '2025-05-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.167', 'weight': '0.050'}

	Recorder: 4bf27653658c43f18019a6cec5810786

		Model: {'id': '4bf27653658c43f18019a6cec5810786', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.057, 'Rank IC': 0.028, 'Rank ICIR': 0.177}, 'data_train_vec': ['2023-05-26', '2025-08-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.177', 'weight': '0.053'}

	Recorder: 976215a1ab67417ca387661e21b8ef30

		Model: {'id': '976215a1ab67417ca387661e21b8ef30', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.042, 'ICIR': 0.193, 'Rank IC': 0.035, 'Rank ICIR': 0.191}, 'data_train_vec': ['2025-05-26', '2026-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.191', 'weight': '0.057'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260526_18 375184080711094474 (Recorders: 3/5)

	Recorder: 59e51e646fb54179bcfda12cefbe38e9

		Model: {'id': '59e51e646fb54179bcfda12cefbe38e9', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.019, 'ICIR': 0.198, 'Rank IC': 0.029, 'Rank ICIR': 0.236}, 'data_train_vec': ['2023-05-26', '2025-08-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.236', 'weight': '0.070'}

	Recorder: 969a1272343744a2a66b359b42db8f0b

		Model: {'id': '969a1272343744a2a66b359b42db8f0b', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.021, 'ICIR': 0.2, 'Rank IC': 0.01, 'Rank ICIR': 0.084}, 'data_train_vec': ['2024-05-26', '2025-11-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.084', 'weight': '0.025'}

	Recorder: f4a71bbeab1942d58071b416275dc2c8

		Model: {'id': 'f4a71bbeab1942d58071b416275dc2c8', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.085, 'ICIR': 0.451, 'Rank IC': 0.045, 'Rank ICIR': 0.217}, 'data_train_vec': ['2025-05-26', '2026-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.217', 'weight': '0.065'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260526_16 114537772141113150 (Recorders: 4/5)

	Recorder: 7ab5f12da7804422b3ce87103eccc350

		Model: {'id': '7ab5f12da7804422b3ce87103eccc350', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.029, 'Rank IC': 0.029, 'Rank ICIR': 0.196}, 'data_train_vec': ['2021-05-26', '2025-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.196', 'weight': '0.058'}

	Recorder: 3e30eaceb1a14725a16aaecd13b7a0a8

		Model: {'id': '3e30eaceb1a14725a16aaecd13b7a0a8', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.065, 'Rank IC': 0.041, 'Rank ICIR': 0.231}, 'data_train_vec': ['2022-05-26', '2025-05-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.231', 'weight': '0.069'}

	Recorder: 9028426b271a4742bbcfaa51e3f36d6b

		Model: {'id': '9028426b271a4742bbcfaa51e3f36d6b', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.02, 'ICIR': 0.166, 'Rank IC': 0.038, 'Rank ICIR': 0.253}, 'data_train_vec': ['2023-05-26', '2025-08-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.253', 'weight': '0.075'}

	Recorder: 478c56b3aaf242069543638fd834a33e

		Model: {'id': '478c56b3aaf242069543638fd834a33e', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.064, 'ICIR': 0.361, 'Rank IC': 0.041, 'Rank ICIR': 0.22}, 'data_train_vec': ['2025-05-26', '2026-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.220', 'weight': '0.066'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260526_16 362398425084254574 (Recorders: 4/5)

	Recorder: 7d0663236c424122b40fe58f35ad04bc

		Model: {'id': '7d0663236c424122b40fe58f35ad04bc', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.059, 'Rank IC': 0.032, 'Rank ICIR': 0.278}, 'data_train_vec': ['2021-05-26', '2025-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.278', 'weight': '0.083'}

	Recorder: 3c9656912c414cca9d28991f84010a74

		Model: {'id': '3c9656912c414cca9d28991f84010a74', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.108, 'Rank IC': 0.038, 'Rank ICIR': 0.345}, 'data_train_vec': ['2023-05-26', '2025-08-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.345', 'weight': '0.103'}

	Recorder: 7b871058090e4cd4a5c600638babed11

		Model: {'id': '7b871058090e4cd4a5c600638babed11', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.023, 'Rank IC': 0.011, 'Rank ICIR': 0.087}, 'data_train_vec': ['2024-05-26', '2025-11-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.087', 'weight': '0.026'}

	Recorder: e3f3ae0876074015b821289d3893e7cc

		Model: {'id': 'e3f3ae0876074015b821289d3893e7cc', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.104, 'ICIR': 0.612, 'Rank IC': 0.081, 'Rank ICIR': 0.416}, 'data_train_vec': ['2025-05-26', '2026-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.416', 'weight': '0.124'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260526_15 534504088173332935 (Recorders: 1/5)

	Recorder: ea8aa9d6ef064e318da5e58dd0fa1035

		Model: {'id': 'ea8aa9d6ef064e318da5e58dd0fa1035', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.052, 'ICIR': 0.302, 'Rank IC': 0.038, 'Rank ICIR': 0.255}, 'data_train_vec': ['2025-05-26', '2026-02-25'], 'train_time_vec': ['2026-05-26', '2026-05-26'], 'rank_icir': '0.255', 'weight': '0.076'}
