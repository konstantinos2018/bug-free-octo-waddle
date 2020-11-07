#!/usr/bin/python3

### Imports
from matplotlib import pyplot as plt
import pandas as pd
import check_defs

def list_to_series(cpu_usage, timestamp):
	df = pd.Series({'cpu_usage_percent': cpu_usage, 'timestamp': timestamp})
	
	return df
	
if __name__ == '__main__':
	n_secs = 0.2 # time interval
	cpu_usage, timestamp = check_defs.cpu_sampling(n_secs=n_secs, sampling_duration=20)
	df = list_to_series(cpu_usage, timestamp)
	print(df)
	fig = plt.figure(figsize=(20,5))
	plt.plot(df.timestamp, df.cpu_usage_percent)
	plt.title('CPU Usage timeseries (timestep={0} s)'.format(n_secs), fontsize=23)
	plt.xlabel('Timestamp', fontsize=18)
	plt.ylabel('Usage [%]', fontsize=18)
	fig.savefig('./plot.png', dpi=300)