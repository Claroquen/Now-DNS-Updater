import requests
import base64
import time


#####################################
#             VARIABLE              #
#####################################
EMAIL= ""
PASSWORD = ""
HOST = ""
#####################################



credentials = EMAIL+":"+PASSWORD
credentials = base64.b64encode(bytes(credentials, 'utf-8'))
credentials = str(credentials).replace("b'","")
headers = {"Authorization": "Basic "+credentials}

def get_ip():
	global my_ip

	my_ip = requests.get('http://icanhazip.com/').text
	my_ip = my_ip.strip()

def change_dns():
	global status
	url = "https://now-dns.com/update?hostname="+HOST+"&myip="+my_ip
	r= requests.get(url,headers = headers)
	status = r.text




while True:
	print ("-------------------------------------------")
	print ("WEB ["+HOST+"]")
	get_ip()
	print ("CURRENT IP ["+my_ip+"]")
	change_dns()
	print ("STATUS ["+status+"]")
	print ("WAITING 5 MINUTES BEFORE THE NEXT EXECUTION")
	print ("-------------------------------------------\n\n")
	time.sleep(300)
