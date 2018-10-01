import requests
import time
import random
import multiprocessing
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--process", required=True)
parser.add_argument("-n", "--n_bus", required=True)
parser.add_argument("-u", "--url", required=True)


args = vars(parser.parse_args())
numbers_process = int(args["process"])
n_bus = int(args["n_bus"])
url = args["url"]

#initialize string of multiprocessing
p = []

#indicate the first bus that their information is going to be update 
bus_start = n_bus*numbers_process

#send request, update buses positions
def send_request(info_geo):

	requests.put( info_geo[0] , json = { "value":str(info_geo[1]) + "," + str(info_geo[2]) } )


#random buses position
for i in range(0, numbers_process): 

	bus_id = "bus_" + str(i+bus_start)

	geo = random.uniform(-20,20)
	point = random.uniform(-20,20)
	url_geo_value = url + bus_id + "/attrs/position"
	info_geo = [url_geo_value, geo, point]
		
	p.append(multiprocessing.Process (target = send_request, args=(info_geo,)))

#start multiprocessing	
for i in range(0, numbers_process):
	p[i].start()

p[numbers_process-3].join()
p[numbers_process-2].join()
p[numbers_process-1].join()

print("[END]: Update "+str(bus_start) +"-" + str(bus_start+numbers_process-1))




