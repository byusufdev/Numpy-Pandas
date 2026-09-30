import numpy as np

# 1. Setup seed and create data
np.random.seed(42)
data = np.random.randn(100, 5)

# Inject outliers
bad_row_idx = np.random.randint(0, 100, size=10)
bad_col_idx = np.random.randint(0, 5, size=10)
data[bad_row_idx, bad_col_idx] = np.random.choice([15.0, -15.0], size=10)

# --- Column means, std and meadians ---
column_means = np.mean(data, axis = 0)
column_stds = np.std(data, axis = 0)
column_mead = np.median(data, axis = 0)

print(np.mean(data)) #print mean and std with anomally data
print(np.std(data))

data_scaled = (data - column_means)/column_stds # z score column standardisation
outliers = np.absolute(data_scaled) > 2.5 # boolean mask to detect anomalies outside of absolute cut off

print(f"Total outliers = {np.sum(outliers)}")

# row_index, col_index = np.where(outliers) # determine anomaly index positions
# data[outliers] = column_mead[col_index] # replace anomaly with respective column means

data = np.where(outliers, column_mead, data)

print(np.mean(data, axis = 0)) #print mean and std without anomally data
print(np.std(data, axis = 0))