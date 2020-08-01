from __future__ import unicode_literals
from ipaddress import IPv4Address
import json
import sys
import requests

#Put your FMC server IP address here
server = "https://x.x.x.x"

username = "admin"
if len(sys.argv) > 1:
    username = sys.argv[1]
password = "sf"
if len(sys.argv) > 2:
    password = sys.argv[2]
if len(sys.argv) > 3: 
    IP = sys.argv[3]

sourceIP = unicode(IP, "utf-8")

Check_IP = IPv4Address(sourceIP).is_private

#Check if the source IP field from Qradar contains private IP. If it holds true, execution will be stopped. 

if Check_IP == False: 
   SourceIP = IP
else: 
   print("IP is an private IP address. Cannot block. Exiting ... \n")
   sys.exit()

r = None
headers = {'Content-Type': 'application/json'}
api_auth_path = "/api/fmc_platform/v1/auth/generatetoken"
auth_url = server + api_auth_path
try:
    # 2 ways of making a REST call are provided:
    # One with "SSL verification turned off" and the other with "SSL verification turned on".
    # The one with "SSL verification turned off" is commented out. If you like to use that then
    # uncomment the line where verify=False and comment the line with =verify='/path/to/ssl_certificate'
    # REST call with SSL verification turned off:
    r = requests.post(auth_url, headers=headers, auth=requests.auth.HTTPBasicAuth(username,password), verify=False)
    # REST call with SSL verification turned on: Download SSL certificates from your FMC first and provide its path for verification.
    # r = requests.post(auth_url, headers=headers, auth=requests.auth.HTTPBasicAuth(username,password), verify='/path/to/ssl_certificate')
    auth_headers = r.headers
    auth_token = auth_headers.get('X-auth-access-token', default=None)
    if auth_token == None:
        print("auth_token not found. Exiting...")
        sys.exit()
except Exception as err:
    print ("Error in generating auth token --> "+str(err))
    sys.exit()

headers['X-auth-access-token']=auth_token

api_path = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networkgroups/0050568F-3EDA-0ed3-0000-274877911250"    # param
url = server + api_path
if (url[-1] == '/'):
    url = url[:-1]


# GET OPERATION
 
try:
    # REST call with SSL verification turned off: 
    r = requests.get(url, headers=headers, verify=False)
    # REST call with SSL verification turned on:
    # r = requests.get(url, headers=headers, verify='/path/to/ssl_certificate')
    status_code = r.status_code
    resp = r.text
    if (status_code == 200):
        print("GET successful. Response data --> ")
        json_resp = json.loads(resp)
#        print(json.dumps(json_resp,sort_keys=True,indent=4, separators=(',', ': ')))
    else:
        r.raise_for_status()
        print("Error occurred in GET --> "+resp)
except requests.exceptions.HTTPError as err:
    print ("Error in connection --> "+str(err)) 
finally:
   if r: r.close()

# Loading existing blacklist IPs

resp2 = json.loads(resp)

temp = resp2['literals']


# PUT Operations

put_data = {
  "id": "0050568F-3EDA-0ed3-0000-274877911250",
  "name": "Blacklist-IP-Pool",
  "type": "NetworkGroup",
  "literals": [
    {
      "type": "Host",
      "value": SourceIP
    }
  ]
}


temp2 = put_data['literals']

# Adding exisiting blacklisted IP in put_data 

for x in temp:
    temp2.append(x) 

try:
    # REST call with SSL verification turned off:
    r = requests.put(url, data=json.dumps(put_data), headers=headers, verify=False)
    # REST call with SSL verification turned on:
    # r = requests.put(url, data=json.dumps(put_data), headers=headers, verify='/path/to/ssl_certificate')
    status_code = r.status_code
    final_resp = r.text
    if (status_code == 200):
        print("Put was successful...")
        final_json_resp = json.loads(final_resp)
        print(json.dumps(final_json_resp,sort_keys=True,indent=4, separators=(',', ': ')))
    else:
        r.raise_for_status()
        print("Status code:-->"+status_code)
        print("Error occurred in PUT --> "+final_resp)
except requests.exceptions.HTTPError as err:
    print ("Error in connection --> "+str(err))
finally:
    if r: r.close()
