# params 
 {'predict_dates': [{'start': '2026-05-15', 'end': '2026-05-15'}], 'provider_uri': '~/.qlib/qlib_data/cn_data/', 'uri_folder': '~/.qlibAssistant/mlruns/', 'analysis_folder': '~/.qlibAssistant/analysis/', 'pfx_name': 'p', 'sfx_name': 's', 'model_name': 'Linear', 'dataset_name': 'Alpha158', 'stock_pool': 'csi300', 'step': 60, 'rolling_type': 'expanding', 'model_filter': ['.*'], 'rec_filter': [{'ic': 0.001}, {'icir': 0.001}, {'rankic': 0.001}, {'rankicir': 0.001}]}



 # model info 

Experiment: EXP_CatBoostModel_Alpha158_csi300_custom_step0_s_20260515_17 413962033132946998 (Recorders: 3/5)

	Recorder: d26b986267514b8eb29e38442d0f8cff

		Model: {'id': 'd26b986267514b8eb29e38442d0f8cff', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.032, 'Rank IC': 0.02, 'Rank ICIR': 0.128}, 'data_train_vec': ['2022-05-15', '2025-05-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.128', 'weight': '0.055'}

	Recorder: d3d14d69a2b64180ab20ea052f040544

		Model: {'id': 'd3d14d69a2b64180ab20ea052f040544', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.002, 'ICIR': 0.017, 'Rank IC': 0.022, 'Rank ICIR': 0.143}, 'data_train_vec': ['2023-05-15', '2025-08-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.143', 'weight': '0.062'}

	Recorder: 592751c7bde04e959f9d9c071c81411d

		Model: {'id': '592751c7bde04e959f9d9c071c81411d', 'model': 'CatBoostModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.081, 'ICIR': 0.54, 'Rank IC': 0.043, 'Rank ICIR': 0.267}, 'data_train_vec': ['2025-05-15', '2026-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.267', 'weight': '0.116'}
Experiment: EXP_LGBModel_Alpha158_csi300_custom_step0_s_20260515_17 520605531650446860 (Recorders: 2/5)

	Recorder: c51e216ef2cf4cc19eb73499eee89fdf

		Model: {'id': 'c51e216ef2cf4cc19eb73499eee89fdf', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.015, 'ICIR': 0.165, 'Rank IC': 0.021, 'Rank ICIR': 0.181}, 'data_train_vec': ['2023-05-15', '2025-08-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.181', 'weight': '0.078'}

	Recorder: 1e897138dd0d473dbd044f8ff785068d

		Model: {'id': '1e897138dd0d473dbd044f8ff785068d', 'model': 'LGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.079, 'ICIR': 0.503, 'Rank IC': 0.026, 'Rank ICIR': 0.156}, 'data_train_vec': ['2025-05-15', '2026-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.156', 'weight': '0.068'}
Experiment: EXP_DEnsembleModel_Alpha158_csi300_custom_step0_s_20260515_14 513843013628935088 (Recorders: 3/5)

	Recorder: 4d581207505c4c6597d273c3c325bd2a

		Model: {'id': '4d581207505c4c6597d273c3c325bd2a', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.007, 'ICIR': 0.044, 'Rank IC': 0.034, 'Rank ICIR': 0.188}, 'data_train_vec': ['2022-05-15', '2025-05-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.188', 'weight': '0.081'}

	Recorder: 94fd48cfe8044339b78fa4a77bb47562

		Model: {'id': '94fd48cfe8044339b78fa4a77bb47562', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.016, 'ICIR': 0.122, 'Rank IC': 0.038, 'Rank ICIR': 0.244}, 'data_train_vec': ['2023-05-15', '2025-08-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.244', 'weight': '0.106'}

	Recorder: 000615e72675418eae81aca9c137ba68

		Model: {'id': '000615e72675418eae81aca9c137ba68', 'model': 'DEnsembleModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.065, 'ICIR': 0.415, 'Rank IC': 0.026, 'Rank ICIR': 0.156}, 'data_train_vec': ['2025-05-15', '2026-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.156', 'weight': '0.068'}
Experiment: EXP_LinearModel_Alpha158_csi300_custom_step0_s_20260515_14 237445905792364386 (Recorders: 3/5)

	Recorder: 1a0c2ed2b1df4568b0ecfde594a74c07

		Model: {'id': '1a0c2ed2b1df4568b0ecfde594a74c07', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.004, 'ICIR': 0.037, 'Rank IC': 0.029, 'Rank ICIR': 0.266}, 'data_train_vec': ['2023-05-15', '2025-08-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.266', 'weight': '0.115'}

	Recorder: 0fdec3e8104343a9a57b8e6ec0646b5e

		Model: {'id': '0fdec3e8104343a9a57b8e6ec0646b5e', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.005, 'ICIR': 0.042, 'Rank IC': 0.016, 'Rank ICIR': 0.142}, 'data_train_vec': ['2024-05-15', '2025-11-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.142', 'weight': '0.062'}

	Recorder: a474ff18752f456bb3540466c6bf9ee2

		Model: {'id': 'a474ff18752f456bb3540466c6bf9ee2', 'model': 'LinearModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.075, 'ICIR': 0.594, 'Rank IC': 0.044, 'Rank ICIR': 0.313}, 'data_train_vec': ['2025-05-15', '2026-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.313', 'weight': '0.136'}
Experiment: EXP_XGBModel_Alpha158_csi300_custom_step0_s_20260515_14 113562577766646125 (Recorders: 1/5)

	Recorder: f0234707ff70434f973078416b8c086c

		Model: {'id': 'f0234707ff70434f973078416b8c086c', 'model': 'XGBModel', 'dataset': 'Alpha158', 'ic_info': {'IC': 0.044, 'ICIR': 0.337, 'Rank IC': 0.017, 'Rank ICIR': 0.123}, 'data_train_vec': ['2025-05-15', '2026-02-14'], 'train_time_vec': ['2026-05-15', '2026-05-15'], 'rank_icir': '0.123', 'weight': '0.053'}
