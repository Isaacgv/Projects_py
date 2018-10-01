import requests
import time
import random
import multiprocessing 
import subprocess
import argparse

#IP of the server
url = _put ip of the server_

#numbers of ids updated n_parallel*data_bus / factor

#number of parallel execution updates
n_parallel = 60

#modify the number of ids updated in one process in the parallel execution
factor = 1

#bus x hours
data_bus = 500


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--factor", required=False, default = factor)
parser.add_argument("-n", "--n_parallel", required=False, default = n_parallel)
parser.add_argument("-u", "--url", required=False, default = url)


args = vars(parser.parse_args())
factor = int(args["factor"])
n_parallel = int(args["n_parallel"])
url = args["url"]

#Update information every 30 seconds
while (True) : 

	#number of ids updated in parallel
	m_numbers_bus = int(data_bus / factor)
	print("[INFO]: m_numbers_bus = " + str(m_numbers_bus))
	print("[INFO]: data_bus = " + str(data_bus))
	print("[INFO]: n_parallel = " + str(n_parallel))
	print("[INFO]: Total number of buses = " + str(m_numbers_bus*n_parallel))
		
	print("[INFO]: Updating parameters ...")

	for i in range(0, m_numbers_bus):
		subprocess.Popen("python2 send_request.py -p "+str(n_parallel)+" -n " + str(i) + " -u "+ url ,shell=True)
		#subprocess.Popen(['C:/Python27/python.exe', path_request, '-p',str(n_parallel) , '-n', str(i), '-u'+url], shell=True)

	print("[INFO]: End send request")

	time.sleep(30)



