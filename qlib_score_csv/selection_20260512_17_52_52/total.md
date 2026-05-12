# params 
 {'predict_dates': [{'start': '2026-05-12', 'end': '2026-05-12'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260512_17 222002692099601690 (Recorders: 4/5)

	Recorder: b37ed29fb21b438ab246f123e30d9817

		Model: {'id': 'b37ed29fb21b438ab246f123e30d9817', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.012, 'ICIR': 0.094, 'Rank IC': 0.013, 'Rank ICIR': 0.081}, 'data_train_vec': ['2022-05-12', '2025-05-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.081', 'weight': '0.027'}

	Recorder: 56efd4c65bc54918b3ec8cb6c4310730

		Model: {'id': '56efd4c65bc54918b3ec8cb6c4310730', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.107, 'Rank IC': 0.02, 'Rank ICIR': 0.136}, 'data_train_vec': ['2023-05-12', '2025-08-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.136', 'weight': '0.046'}

	Recorder: 0576259c27744503a8e4d13e2b60c04f

		Model: {'id': '0576259c27744503a8e4d13e2b60c04f', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.087, 'Rank IC': 0.016, 'Rank ICIR': 0.135}, 'data_train_vec': ['2024-05-12', '2025-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.135', 'weight': '0.045'}

	Recorder: b861f6c0076f49dc8ddf779ca57370c9

		Model: {'id': 'b861f6c0076f49dc8ddf779ca57370c9', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.056, 'ICIR': 0.42, 'Rank IC': 0.018, 'Rank ICIR': 0.145}, 'data_train_vec': ['2025-05-12', '2026-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.145', 'weight': '0.049'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260512_17 332868596188066488 (Recorders: 3/5)

	Recorder: c42dccca6e3c4f689c22cd7b99ae72dd

		Model: {'id': 'c42dccca6e3c4f689c22cd7b99ae72dd', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.079, 'Rank IC': 0.018, 'Rank ICIR': 0.159}, 'data_train_vec': ['2023-05-12', '2025-08-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.159', 'weight': '0.054'}

	Recorder: cfaf8c08e23c43fa9e32bfbd24cefff3

		Model: {'id': 'cfaf8c08e23c43fa9e32bfbd24cefff3', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.146, 'Rank IC': 0.013, 'Rank ICIR': 0.108}, 'data_train_vec': ['2024-05-12', '2025-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.108', 'weight': '0.036'}

	Recorder: bfbe76784fea45a09c3373cde85f9212

		Model: {'id': 'bfbe76784fea45a09c3373cde85f9212', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.075, 'ICIR': 0.586, 'Rank IC': 0.024, 'Rank ICIR': 0.217}, 'data_train_vec': ['2025-05-12', '2026-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.217', 'weight': '0.073'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260512_14 768663439955398678 (Recorders: 4/5)

	Recorder: 13c0d57b3d9c4101ae4ef35c1a74efcd

		Model: {'id': '13c0d57b3d9c4101ae4ef35c1a74efcd', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.024, 'Rank IC': 0.031, 'Rank ICIR': 0.179}, 'data_train_vec': ['2022-05-12', '2025-05-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.179', 'weight': '0.060'}

	Recorder: 478a7c33fe24403091bb0452bb582a68

		Model: {'id': '478a7c33fe24403091bb0452bb582a68', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.069, 'Rank IC': 0.031, 'Rank ICIR': 0.209}, 'data_train_vec': ['2023-05-12', '2025-08-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.209', 'weight': '0.070'}

	Recorder: 898586eb9530482fb48194d7fdd42be6

		Model: {'id': '898586eb9530482fb48194d7fdd42be6', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.038, 'Rank IC': 0.001, 'Rank ICIR': 0.01}, 'data_train_vec': ['2024-05-12', '2025-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.010', 'weight': '0.003'}

	Recorder: bda04fa737e14d19a1f42dcc49d76a53

		Model: {'id': 'bda04fa737e14d19a1f42dcc49d76a53', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.074, 'ICIR': 0.619, 'Rank IC': 0.027, 'Rank ICIR': 0.243}, 'data_train_vec': ['2025-05-12', '2026-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.243', 'weight': '0.082'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260512_14 449072845442855210 (Recorders: 4/5)

	Recorder: 55fef06a647a4c91a49d10e961dc8c79

		Model: {'id': '55fef06a647a4c91a49d10e961dc8c79', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.014, 'Rank IC': 0.02, 'Rank ICIR': 0.188}, 'data_train_vec': ['2021-05-12', '2025-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.188', 'weight': '0.063'}

	Recorder: 1e2c643d65184025843cca4965908a90

		Model: {'id': '1e2c643d65184025843cca4965908a90', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.017, 'Rank IC': 0.026, 'Rank ICIR': 0.225}, 'data_train_vec': ['2023-05-12', '2025-08-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.225', 'weight': '0.076'}

	Recorder: e4d0b54e445245e082e27e03d4fbe7c8

		Model: {'id': 'e4d0b54e445245e082e27e03d4fbe7c8', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.009, 'ICIR': 0.08, 'Rank IC': 0.019, 'Rank ICIR': 0.164}, 'data_train_vec': ['2024-05-12', '2025-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.164', 'weight': '0.055'}

	Recorder: 522ae236231c45fea9cb2ce983e78dbb

		Model: {'id': '522ae236231c45fea9cb2ce983e78dbb', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.047, 'ICIR': 0.622, 'Rank IC': 0.021, 'Rank ICIR': 0.247}, 'data_train_vec': ['2025-05-12', '2026-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.247', 'weight': '0.083'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260512_14 928286013412479172 (Recorders: 4/5)

	Recorder: f6e255b63b8d4a4a8eac1223ac7eb910

		Model: {'id': 'f6e255b63b8d4a4a8eac1223ac7eb910', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.029, 'Rank IC': 0.011, 'Rank ICIR': 0.063}, 'data_train_vec': ['2022-05-12', '2025-05-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.063', 'weight': '0.021'}

	Recorder: a9c719908d14408e863bf813e2a3d482

		Model: {'id': 'a9c719908d14408e863bf813e2a3d482', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.013, 'ICIR': 0.086, 'Rank IC': 0.024, 'Rank ICIR': 0.14}, 'data_train_vec': ['2023-05-12', '2025-08-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.140', 'weight': '0.047'}

	Recorder: ec4b990f26484769a0a2b08b00387af2

		Model: {'id': 'ec4b990f26484769a0a2b08b00387af2', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.008, 'ICIR': 0.071, 'Rank IC': 0.008, 'Rank ICIR': 0.061}, 'data_train_vec': ['2024-05-12', '2025-11-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.061', 'weight': '0.021'}

	Recorder: 97eae4765087402c82043863f9c77ef8

		Model: {'id': '97eae4765087402c82043863f9c77ef8', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.043, 'ICIR': 0.422, 'Rank IC': 0.019, 'Rank ICIR': 0.259}, 'data_train_vec': ['2025-05-12', '2026-02-11'], 'train_time_vec': ['2026-05-12', '2026-05-12'], 'rank_icir': '0.259', 'weight': '0.087'}
