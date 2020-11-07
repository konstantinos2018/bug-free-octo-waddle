#!/usr/bin/python3
# The above works for Windows Subsystem for Linux

### Imports
import psutil
import datetime as dt

def cpu_sampling(n_secs=0.1, sampling_duration=5):
	"""
	Arguments
		n_secs -- interval between samplings in seconds
		sampling_duration -- duration of sampling in seconds
	Returns
		cpu_lst -- list of cpu usage in percentage
		cpu_time -- list of time of sampling in datetime object
	"""
	
	# Initialization
	cpu_lst = []
	cpu_time = []
	delta_t = dt.timedelta(seconds=sampling_duration) # duration of sampling
	t_now = dt.datetime.now()
	t_start = t_now # starting point
	
	while t_now < (t_start + delta_t):
		cpu_lst.append(psutil.cpu_percent(n_secs))
		cpu_time.append(t_now)
		t_now = dt.datetime.now()
	
	return cpu_lst, cpu_time
	

if __name__ == '__main__':

	cpu_lst, cpu_time = cpu_sampling(n_secs=0.1)
	print(len(cpu_lst))