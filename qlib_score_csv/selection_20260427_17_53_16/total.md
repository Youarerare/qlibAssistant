# params 
 {'predict_dates': [{'start': '2026-04-27', 'end': '2026-04-27'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260427_16 148801485959627849 (Recorders: 2/5)

	Recorder: a1475f23176c4c42b3000eacd884d56b

		Model: {'id': 'a1475f23176c4c42b3000eacd884d56b', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.045, 'Rank IC': 0.027, 'Rank ICIR': 0.161}, 'data_train_vec': ['2023-04-27', '2025-07-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.161', 'weight': '0.099'}

	Recorder: 3db33b0b7a8045158f23cd8eae54c11f

		Model: {'id': '3db33b0b7a8045158f23cd8eae54c11f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.023, 'ICIR': 0.154, 'Rank IC': 0.003, 'Rank ICIR': 0.02}, 'data_train_vec': ['2025-04-27', '2026-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.020', 'weight': '0.012'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260427_16 952177657162065970 (Recorders: 3/5)

	Recorder: 13f233356c9642b18ca8a281b73c94ac

		Model: {'id': '13f233356c9642b18ca8a281b73c94ac', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.048, 'Rank IC': 0.03, 'Rank ICIR': 0.211}, 'data_train_vec': ['2023-04-27', '2025-07-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.211', 'weight': '0.129'}

	Recorder: cb47a2b92053419bbf914a98c2ed344d

		Model: {'id': 'cb47a2b92053419bbf914a98c2ed344d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.057, 'Rank IC': 0.015, 'Rank ICIR': 0.121}, 'data_train_vec': ['2024-04-27', '2025-10-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.121', 'weight': '0.074'}

	Recorder: d36feadcbab64f319b998a2a0a2ba88d

		Model: {'id': 'd36feadcbab64f319b998a2a0a2ba88d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.036, 'ICIR': 0.24, 'Rank IC': 0.021, 'Rank ICIR': 0.136}, 'data_train_vec': ['2025-04-27', '2026-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.136', 'weight': '0.083'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260427_14 876778277607744537 (Recorders: 3/5)

	Recorder: 22aafc69a45349bb9ed6c172f0c0e4ca

		Model: {'id': '22aafc69a45349bb9ed6c172f0c0e4ca', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.102, 'Rank IC': 0.045, 'Rank ICIR': 0.265}, 'data_train_vec': ['2023-04-27', '2025-07-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.265', 'weight': '0.162'}

	Recorder: caa1dafdf7a24c44ad01836208310171

		Model: {'id': 'caa1dafdf7a24c44ad01836208310171', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.011, 'ICIR': 0.096, 'Rank IC': 0.011, 'Rank ICIR': 0.094}, 'data_train_vec': ['2024-04-27', '2025-10-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.094', 'weight': '0.058'}

	Recorder: 5ab33faf9aaf45158d72fc348084c108

		Model: {'id': '5ab33faf9aaf45158d72fc348084c108', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.027, 'ICIR': 0.16, 'Rank IC': 0.01, 'Rank ICIR': 0.054}, 'data_train_vec': ['2025-04-27', '2026-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.054', 'weight': '0.033'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260427_14 694141976762082433 (Recorders: 2/5)

	Recorder: 035ac3e3aa3f42238f48f6c96e75a94d

		Model: {'id': '035ac3e3aa3f42238f48f6c96e75a94d', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.014, 'Rank IC': 0.009, 'Rank ICIR': 0.072}, 'data_train_vec': ['2024-04-27', '2025-10-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.072', 'weight': '0.044'}

	Recorder: b3970259e8ff4607b3b66897949f527a

		Model: {'id': 'b3970259e8ff4607b3b66897949f527a', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.059, 'ICIR': 0.457, 'Rank IC': 0.032, 'Rank ICIR': 0.223}, 'data_train_vec': ['2025-04-27', '2026-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.223', 'weight': '0.136'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260427_14 445886479531116761 (Recorders: 2/5)

	Recorder: e0ba856c8a0049488627b4abdb2cfa52

		Model: {'id': 'e0ba856c8a0049488627b4abdb2cfa52', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.01, 'ICIR': 0.081, 'Rank IC': 0.029, 'Rank ICIR': 0.265}, 'data_train_vec': ['2024-04-27', '2025-10-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.265', 'weight': '0.162'}

	Recorder: 32785d30cd5e4b0ab06f344cf8cf31bf

		Model: {'id': '32785d30cd5e4b0ab06f344cf8cf31bf', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.055, 'Rank IC': 0.002, 'Rank ICIR': 0.012}, 'data_train_vec': ['2025-04-27', '2026-01-26'], 'train_time_vec': ['2026-04-27', '2026-04-27'], 'rank_icir': '0.012', 'weight': '0.007'}
