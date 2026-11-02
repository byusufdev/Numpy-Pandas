Data Processing Practice: NumPy & Pandas
A hands-on log of exercises covering core data manipulation, cleaning, and preprocessing techniques in Python.

What’s Covered
NumPy Foundations: Vectorized operations, array broadcasting, Z-score normalization, and outlier detection using both IQR clipping and masked arrays (numpy.ma).

Data Cleaning & Wrangling: Parsing raw CSV/TSV files, sanitizing messy strings, joining datasets, and identifying unregistered records with boolean masks.

Safe Imputation: Scoped missing-value replacement (avoiding data leakage from dirty records) and preventing SettingWithCopyWarning issues with .copy().

Aggregations & Pipeline Handoff: Multi-level group aggregations (.groupby()) with clean named summaries, along with exporting aligned 1D NumPy arrays for machine learning pipelines.


├── 01_numpy_outliers_scaling/        # Z-scores, numpy.ma masking, and IQR clipping
├── 02_pandas_foundations/            # DataFrame indexing, .assign(), and basic manipulation
├── 03_data_cleaning_aggregation/     # Handling nulls (.fillna), dropping rows, and groupby
├── 04_relational_joins_logic/        # Table merges, conditional logic (np.select), multi-agg
└── 05_experimental_event_pipeline/   # End-to-end event log cleaning and ML array export
