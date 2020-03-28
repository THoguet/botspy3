#!/usr/bin/Nessar

import urllib.request
import json
import time
from time import strftime
import ts3
import re

def lookup(ip):

	response = urllib.request.Request("http://v2.api.iphub.info/ip/{}".format(ip))
	response.add_header("X-Key", "***REMOVED***")
	
	try:
		response = json.loads(urllib.request.urlopen(response).read().decode())
	except:
		return False # In the case of an error, pass all IP's to avoid blocking innocents

	return response.get("block") # Defaults to None if failed to get block value

def vieprog(cluid, clname):
	time = strftime("%d/%m/%Y %H:%M:%S")
	banclient = 0
	with open("/home/pi/Documents/python/data_file.json", "r") as read_file:
		identites = json.load(read_file)
	try:
		if identites[cluid] is not None:
			if identites[cluid]["vie"] != 0:
				identites[cluid]["vie"] = identites[cluid]["vie"] - 1
			identites[cluid]['time'] = time
	except:
		identites.update({cluid: {"clname": clname, "vie": 2, "time": time}})

	with open("/home/pi/Documents/python/data_file.json", "w") as write_file:
		json.dump(identites, write_file)
	
	return identites[cluid]['vie']

# response = requests.get("https://api.xdefcon.com/proxy/check/?ip=")
# info = json.loads(response.text)
# print (info['message'])

def prog(ts3conn):
	ts3conn.send_keepalive()
	try:
		event = ts3conn.wait_for_event(240)
		print(time.strftime("%H:%M:%S"))
		print(' Info: Evenement' + '\n')
	except:
		print(time.strftime("%H:%M:%S"))
		print('Warning: Timeout' + '\n')
		return 2
	try:
		if event[0]["reasonid"] == '0' and event[0]["client_type"] != 1 :
			clsg = event[0]['client_servergroups']
			if re.search("6",clsg) is None and re.search("9",clsg) is None and re.search("18",clsg) is None:
				clinfo = ts3conn.clientinfo(clid=event[0]['clid'])
				clip = clinfo[0]["connection_client_ip"]
				clname = clinfo[0]['client_nickname']
				clid = event[0]["clid"]
				if lookup(clip) == 1:
					vie = vieprog(event[0]['client_unique_identifier'], clname)
					if vie > 0:
						vie = str(vie)
						ts3conn.clientpoke(msg="Pas de proxy ! (Seulement l'ip est ban, il te reste "+vie+" vie(s) avant que ton identite soit ban !", clid=clid)
						ts3conn.banadd(ip=clip, banreason="Pas de Proxy !", time=0)
					else:
						ts3conn.clientpoke(msg="Pas de proxy ! Ton identite est aussi ban !", clid=clid)
						ts3conn.banadd(uid=event[0]['client_unique_identifier'], banreason="Pas de Proxy "+clname+"!", time=0)
						ts3conn.banadd(ip=clip, banreason="Pas de Proxy !", time=0)
	except:
		print(time.strftime("%H:%M:%S"))
		print('Warning: ERROR' + '\n')
		return 3

with ts3.query.TS3Connection("localhost") as ts3conn:
	ts3conn.login(
		client_login_name="***REMOVED***",
		client_login_password="***REMOVED***"
	)
	ts3conn.use(sid=1)
	ts3conn.clientupdate(client_nickname="Bot Anti-VPN")
	ts3conn.servernotifyregister(event="server")
	while True:
		prog(ts3conn)