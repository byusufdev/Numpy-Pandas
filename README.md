# Data Processing Practice: NumPy & Pandas

A log of exercises covering core data manipulation, cleaning, and preprocessing techniques in Python.

## What's Covered

- **NumPy Foundations**: Vectorized operations, array broadcasting, Z-score normalisation, and outlier detection using IQR clipping and masked arrays.
- **Data Cleaning**: Parsing raw CSV/TSV files, sanitising messy strings, joining datasets, and identifying unregistered records with boolean masks.
- **Safe Imputation**: Scoped missing-value replacement (avoiding leakage from dirty records) and avoiding `SettingWithCopyWarning` issues.
- **Aggregations & Pipeline Handoff**: Multi-level group aggregations (`.groupby()`) with clean named summaries, along with exporting aligned 1D NumPy arrays for machine learning pipelines.

## Project Structure

```text
├── Numpy/
│   ├── Numpy array basics.py
│   ├── Numpy project 1 - removing anomalies in standard normally distrubuted dataset.py
│   └── Numpy project 2 - removing anomalies in exponentional dataset.py
├── Pandas basics.ipynb                                 # DataFrame indexing and basic manipulation
├── Project 1 - adding, removing and filtering.ipynb    # .assign(), .insert(), .at, boolean filtering
├── Project 2 - Data Cleaning with NaNs.ipynb           # Handling nulls (.fillna), dropping rows, groupby
├── Project 3 - merging and vectorisation.ipynb         # Table merges, conditional logic (np.select)
├── Project 4 - mapping + exporting.ipynb               # String cleaning, label mapping (.map), TSV parsing
├── Project 5 - Pandas summary.ipynb                    # End-to-end event log cleaning and ML array export
└── Data files: orders.csv, Adjusted orders.csv, raw_trials.csv, subjects.tsv, experiment_events.tsv
```
