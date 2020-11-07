#!/usr/bin/python3

### Imports
from matplotlib import pyplot as plt
import pandas as pd
import check_defs

def list_to_dataframe(cpu_usage, timestamp):
	df = pd.DataFrame({'cpu_usage_percent': cpu_usage, 'timestamp': timestamp})
	
	return df
	
if __name__ == '__main__':
	cpu_usage, timestamp = check_defs.cpu_sampling(n_secs=0.1, sampling_duration=5)
	df = list_to_dataframe(cpu_usage, timestamp)
	print(df)