# params 
 {'predict_dates': [{'start': '2026-05-14', 'end': '2026-05-14'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260514_17 466369815188921222 (Recorders: 3/5)

	Recorder: 5f6db4ce5e2d44778efc24d82ceea169

		Model: {'id': '5f6db4ce5e2d44778efc24d82ceea169', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.053, 'Rank IC': 0.021, 'Rank ICIR': 0.138}, 'data_train_vec': ['2022-05-14', '2025-05-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.138', 'weight': '0.056'}

	Recorder: 568165fcbc9f4b2e86ade153a9bcd71d

		Model: {'id': '568165fcbc9f4b2e86ade153a9bcd71d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.138, 'Rank IC': 0.011, 'Rank ICIR': 0.075}, 'data_train_vec': ['2024-05-14', '2025-11-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.075', 'weight': '0.030'}

	Recorder: 819d10440c5c44ddbce9b43bd739607e

		Model: {'id': '819d10440c5c44ddbce9b43bd739607e', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.073, 'ICIR': 0.473, 'Rank IC': 0.037, 'Rank ICIR': 0.229}, 'data_train_vec': ['2025-05-14', '2026-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.229', 'weight': '0.092'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260514_17 156593749913593346 (Recorders: 3/5)

	Recorder: 3f0afcd351324c4d962ef8cdf97715fe

		Model: {'id': '3f0afcd351324c4d962ef8cdf97715fe', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.018, 'ICIR': 0.19, 'Rank IC': 0.027, 'Rank ICIR': 0.225}, 'data_train_vec': ['2023-05-14', '2025-08-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.225', 'weight': '0.091'}

	Recorder: 415ae5ef668046068ea20fef2fd8bcf3

		Model: {'id': '415ae5ef668046068ea20fef2fd8bcf3', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.127, 'Rank IC': 0.006, 'Rank ICIR': 0.057}, 'data_train_vec': ['2024-05-14', '2025-11-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.057', 'weight': '0.023'}

	Recorder: 99d9eac610a8441c95d6d39323080752

		Model: {'id': '99d9eac610a8441c95d6d39323080752', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.095, 'ICIR': 0.639, 'Rank IC': 0.046, 'Rank ICIR': 0.304}, 'data_train_vec': ['2025-05-14', '2026-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.304', 'weight': '0.122'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260514_14 252428652614460554 (Recorders: 3/5)

	Recorder: c8f71201148b462595fd247b728a1753

		Model: {'id': 'c8f71201148b462595fd247b728a1753', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.025, 'Rank IC': 0.031, 'Rank ICIR': 0.174}, 'data_train_vec': ['2022-05-14', '2025-05-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.174', 'weight': '0.070'}

	Recorder: 91e56c0e6790473084cfaab7745a44f6

		Model: {'id': '91e56c0e6790473084cfaab7745a44f6', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.014, 'ICIR': 0.11, 'Rank IC': 0.036, 'Rank ICIR': 0.229}, 'data_train_vec': ['2023-05-14', '2025-08-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.229', 'weight': '0.092'}

	Recorder: 710c016bed2c4fd399009a454120d236

		Model: {'id': '710c016bed2c4fd399009a454120d236', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.072, 'ICIR': 0.432, 'Rank IC': 0.03, 'Rank ICIR': 0.174}, 'data_train_vec': ['2025-05-14', '2026-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.174', 'weight': '0.070'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260514_14 764009015431103293 (Recorders: 3/5)

	Recorder: f0d9c762f7c447f69db2bfc98ebdf7af

		Model: {'id': 'f0d9c762f7c447f69db2bfc98ebdf7af', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.021, 'Rank IC': 0.027, 'Rank ICIR': 0.246}, 'data_train_vec': ['2023-05-14', '2025-08-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.246', 'weight': '0.099'}

	Recorder: 96dc3e932b844c2898b2c072ac93b4b3

		Model: {'id': '96dc3e932b844c2898b2c072ac93b4b3', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.076, 'Rank IC': 0.019, 'Rank ICIR': 0.166}, 'data_train_vec': ['2024-05-14', '2025-11-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.166', 'weight': '0.067'}

	Recorder: 9484ab89b17c4deba62fce6fdc4dc4d6

		Model: {'id': '9484ab89b17c4deba62fce6fdc4dc4d6', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.073, 'ICIR': 0.528, 'Rank IC': 0.044, 'Rank ICIR': 0.277}, 'data_train_vec': ['2025-05-14', '2026-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.277', 'weight': '0.112'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260514_14 656996102431859337 (Recorders: 2/5)

	Recorder: c2f7a89201954f8e98d39a5844a4efcd

		Model: {'id': 'c2f7a89201954f8e98d39a5844a4efcd', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.121, 'Rank IC': 0.002, 'Rank ICIR': 0.018}, 'data_train_vec': ['2024-05-14', '2025-11-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.018', 'weight': '0.007'}

	Recorder: 088e13c5a4d24468bcf663a5384f3e26

		Model: {'id': '088e13c5a4d24468bcf663a5384f3e26', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.064, 'ICIR': 0.489, 'Rank IC': 0.025, 'Rank ICIR': 0.171}, 'data_train_vec': ['2025-05-14', '2026-02-13'], 'train_time_vec': ['2026-05-14', '2026-05-14'], 'rank_icir': '0.171', 'weight': '0.069'}
