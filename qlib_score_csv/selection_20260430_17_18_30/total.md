# params 
 {'predict_dates': [{'start': '2026-04-30', 'end': '2026-04-30'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260430_16 287558502068478851 (Recorders: 2/5)

	Recorder: 777ff0cc73a9493cab190cc3ce23ad13

		Model: {'id': '777ff0cc73a9493cab190cc3ce23ad13', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.06, 'Rank IC': 0.013, 'Rank ICIR': 0.127}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.127', 'weight': '0.085'}

	Recorder: 34ab6330ece049ddb1d76a8a421de990

		Model: {'id': '34ab6330ece049ddb1d76a8a421de990', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.406, 'Rank IC': 0.019, 'Rank ICIR': 0.167}, 'data_train_vec': ['2025-04-30', '2026-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.167', 'weight': '0.112'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260430_16 353923896143959294 (Recorders: 2/5)

	Recorder: 54e4dc2208044ae3923872e28120976e

		Model: {'id': '54e4dc2208044ae3923872e28120976e', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.058, 'Rank IC': 0.01, 'Rank ICIR': 0.086}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.086', 'weight': '0.058'}

	Recorder: be4d8907b2eb4dea8534c62aada15658

		Model: {'id': 'be4d8907b2eb4dea8534c62aada15658', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.075, 'ICIR': 0.643, 'Rank IC': 0.035, 'Rank ICIR': 0.287}, 'data_train_vec': ['2025-04-30', '2026-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.287', 'weight': '0.193'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260430_14 200536854473546428 (Recorders: 2/5)

	Recorder: 8e9669296eba4171ae9049dd4ae21a40

		Model: {'id': '8e9669296eba4171ae9049dd4ae21a40', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.072, 'Rank IC': 0.005, 'Rank ICIR': 0.044}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.044', 'weight': '0.030'}

	Recorder: e61e37fa57064f11befa7651026cd38a

		Model: {'id': 'e61e37fa57064f11befa7651026cd38a', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.32, 'Rank IC': 0.014, 'Rank ICIR': 0.096}, 'data_train_vec': ['2025-04-30', '2026-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.096', 'weight': '0.064'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260430_14 789311429798786268 (Recorders: 2/5)

	Recorder: 334b1bb32a5b4ade83bde30f8904c412

		Model: {'id': '334b1bb32a5b4ade83bde30f8904c412', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.003, 'ICIR': 0.022, 'Rank IC': 0.009, 'Rank ICIR': 0.072}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.072', 'weight': '0.048'}

	Recorder: eb4391c03037416ba00347a8594a4e75

		Model: {'id': 'eb4391c03037416ba00347a8594a4e75', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.057, 'ICIR': 0.598, 'Rank IC': 0.03, 'Rank ICIR': 0.273}, 'data_train_vec': ['2025-04-30', '2026-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.273', 'weight': '0.183'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260430_14 847916514024750762 (Recorders: 3/5)

	Recorder: 285272d9dc36452ca63505297b4fd9e5

		Model: {'id': '285272d9dc36452ca63505297b4fd9e5', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.006, 'ICIR': 0.043, 'Rank IC': 0.013, 'Rank ICIR': 0.075}, 'data_train_vec': ['2021-04-30', '2025-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.075', 'weight': '0.050'}

	Recorder: 14c74e73454b47df9dfc5e063fd20ace

		Model: {'id': '14c74e73454b47df9dfc5e063fd20ace', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.049, 'Rank IC': 0.017, 'Rank ICIR': 0.145}, 'data_train_vec': ['2024-04-28', '2025-10-27'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.145', 'weight': '0.097'}

	Recorder: d50111e5726e44e19362834353b272a1

		Model: {'id': 'd50111e5726e44e19362834353b272a1', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.025, 'ICIR': 0.271, 'Rank IC': 0.01, 'Rank ICIR': 0.118}, 'data_train_vec': ['2025-04-30', '2026-01-29'], 'train_time_vec': ['2026-04-30', '2026-04-30'], 'rank_icir': '0.118', 'weight': '0.079'}
