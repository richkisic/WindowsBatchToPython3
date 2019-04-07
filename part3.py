# Python 3.6.3 Scripting Examples by Rich K for Task 29842
# Note a lot of this is similar in Python 2, but not the same
# Remember, Ctrl+Z then Enter to exit a command line python session in Windows

def gotoReplacement():
  print("Use functions instead")

# Write JSON
import sys, os, shutil, json
print ("*************Write JSON*************")
import xml.etree.cElementTree as ET

jsonData = {}  
jsonData['people'] = []  
jsonData['people'].append({  
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
jsonData['people'].append({  
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
jsonData['people'].append({  
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('json.txt', 'w') as outfile:  
    json.dump(jsonData, outfile)
print ("Wrote json.txt")

# Read JSON
print ("*************Read JSON*************")
with open('json.txt') as json_file:  
    jsonData = json.load(json_file)
    for p in jsonData['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')


# HTTP Requests
print ("*************HTTP Requests*************")
print ("(ensure you pip install requests in Windows, first)")
import requests 

URL = "http://maps.googleapis.com/maps/api/geocode/json"
location = "Psychology Software Tools, Inc"
PARAMS = {'address':location} 
r = requests.get(url = URL, params = PARAMS) 
jsonData = r.json() 
  
# extracting latitude, longitude and formatted address  
# of the first matching location 
print("status = ", jsonData['status'])
print("error message = ", jsonData['error_message'])
if jsonData['status'] == "OK":
  latitude = jsonData['results'][0]['geometry']['location']['lat'] 
  longitude = jsonData['results'][0]['geometry']['location']['lng'] 
  formatted_address = jsonData['results'][0]['formatted_address'] 
  print("HTTP Request, PST at Latitude:%s\nLongitude:%s\nFormatted Address:%s"
    %(latitude, longitude,formatted_address)) 
		
# Read Socket
print ("*************Read Socket*************")
import socket

# the public network interface
HOST = socket.gethostbyname(socket.gethostname())
# create a raw socket and bind it to the public interface
try: # error processing
  s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
  s.bind((HOST, 0))
  s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
  s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
  print ("Receiving a packet, ", s.recvfrom(65565))
  # disabled promiscuous mode
  s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
except OSError as err:
  print("There was a socket error: ", err)

# COM Objects
print ("*************COM Objects*************")
print ("(ensure you pip install pypiwin32 in Windows, first)")
from win32com.client.gencache import EnsureDispatch
print("Opening Excel...")
xl = EnsureDispatch ("Excel.Application")
xl.Visible = True
# then do whatever with your xl application 

# Jumping
print ("*************Jumping*************")
print("There are no goto/label statements in python")
gotoReplacement()

# Env Variables
print ("*************Env Variables*************")
print("PATH var = ", os.environ['PATH'])
# setting it would just be os.environ['PATH'] = "foo"





