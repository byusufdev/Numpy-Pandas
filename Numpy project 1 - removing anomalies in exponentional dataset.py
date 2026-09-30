import numpy as np

# 1. Setup seed and create data
np.random.seed(101)
data = np.random.exponential(scale=2.0, size=(200, 4))

# Inject extreme spikes
spike_rows = np.random.randint(0, 200, size=8)
spike_cols = np.random.randint(0, 4, size=8)
data[spike_rows, spike_cols] = np.random.uniform(100.0, 250.0, size=8)

# --- Your pipeline starts here ---
q3, q1 = np.percentile(data, [75, 25], axis = 0)
# print(q3, q1)
iqr = q3 - q1
# print(iqr)

l_bound = q1 - (1.5*iqr)
u_bound = q3 + (1.5*iqr)

winsorized_data = np.clip(data, l_bound, u_bound)

col_min = np.min(winsorized_data, axis = 0)
col_max = np.max(winsorized_data, axis = 0)

scaled_data = (winsorized_data - col_min)/(col_max- col_min)

print(np.min(scaled_data, axis = 0))
print(np.max(scaled_data, axis = 0))


print(np.median(scaled_data, axis = 0))
print(np.subtract(*np.percentile(scaled_data, [75, 25], axis = 0)))