import requests
import argparse


#IP of the server
url = _put ip of the server_

#indicate a start bus that is going to be create
numbers_bus_start= 0

#indicate a end bus that is going to be create
numbers_bus = 30000 


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", required=False, default = numbers_bus_start)
parser.add_argument("-e", "--end", required=False, default = numbers_bus)
parser.add_argument("-u", "--url", required=False, default = url)


args = vars(parser.parse_args())
start = int(args["start"])
end = int(args["end"])
url = args["url"]

#Create numbers of buses
def create_buses(numbers_bus):

	print("[INFO]: Creating ID Buses...")

	for i in range(start, end): 
		bus_id = "bus_" + str(i)
		info = { "id": bus_id, "type": "iotdevice", \
			"position": { "type": "geo:point", "value": "0,0" } }
		requests.post(url , json = info)
		print("[INFO]: #id Bus: "+ str(i))
	print("[INFO]: End creating ID Buses")


create_buses( numbers_bus )
