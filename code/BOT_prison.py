#!/usr/bin/Nessar

import time
import ts3
import re

def prog(ts3conn, a):
	ts3conn.send_keepalive()
	try:
		event = ts3conn.wait_for_event(240)
		if a == 1:
			return 2
		print(time.strftime("%H:%M:%S"))
		print(' Info: Evenement' + '\n')
	except:
		print(time.strftime("%H:%M:%S"))
		print(' Warning: Timeout' + '\n')
		#ts3conn.close()
		return 2
	try:
		if event[0]["ctid"] == "45" and event[0]["reasonid"] == "1" and event[0]["invokerid"] != "14":
			clid_ = event[0]["clid"]
			ts3conn.clientpoke(clid=clid_, msg="Bienvenue en PRISON")
			clinfo = ts3conn.clientinfo(clid=clid_)
			cldbid_ = clinfo[0]["client_database_id"]
			clsg = clinfo[0]["client_servergroups"]
			if re.search("19", clsg) is not None:
				ts3conn.servergroupdelclient(sgid=19, cldbid=cldbid_)
			ts3conn.servergroupaddclient(sgid=19, cldbid=cldbid_)
			return 1
			
		if event[0]["ctid"] == "46" and event[0]["reasonid"] == "1" and event[0]["invokerid"] != "14":
			clid_ = event[0]["clid"]
			ts3conn.clientpoke(clid=clid_, msg="Bienvenue en PRISON")
			clinfo = ts3conn.clientinfo(clid=clid_)
			cldbid_ = clinfo[0]["client_database_id"]
			clsg = clinfo[0]["client_servergroups"]
			if re.search("19", clsg) is not None:
				ts3conn.servergroupdelclient(sgid=19, cldbid=cldbid_)
			ts3conn.servergroupaddclient(sgid=19, cldbid=cldbid_)
			return 1
			
		if event[0]["ctid"] == "47" and event[0]["reasonid"] == "1" and event[0]["invokerid"] != "14":
			clid_ = event[0]["clid"]
			ts3conn.clientpoke(clid=clid_, msg="Bienvenue en PRISON")
			clinfo = ts3conn.clientinfo(clid=clid_)
			cldbid_ = clinfo[0]["client_database_id"]
			clsg = clinfo[0]["client_servergroups"]
			if re.search("19", clsg) is not None:
				ts3conn.servergroupdelclient(sgid=19, cldbid=cldbid_)
			ts3conn.servergroupaddclient(sgid=19, cldbid=cldbid_)
			return 1
			
		if event[0]["ctid"] != "47" and event[0]["ctid"] != "46" and event[0]["ctid"] != "45" and event[0]["reasonid"] == "1" and event[0]["invokerid"] != "14":
			clid_ = event[0]["clid"]
			clinfo = ts3conn.clientinfo(clid=clid_)
			cldbid_ = clinfo[0]["client_database_id"]
			clsg = clinfo[0]["client_servergroups"]
			if re.search("19", clsg) is not None:
				ts3conn.servergroupdelclient(sgid=19, cldbid=cldbid_)
			a = 0
			return 1
		
		if event[0]["ctid"] == "131":
			try:
				clid_ = event[0]["clid"]
				ts3conn.clientupdate(client_nickname="Bot grades")
				ts3conn.clientpoke(msg="Pour toute demande de grade repondez :", clid=clid_)
				ts3conn.clientpoke(msg="!rank ask|del R6|CSGO|fortnite|RL|PUBG|LOL|Minecraft|tft|Gmod", clid=clid_)
				ts3conn.clientpoke(msg="Pour demander d'autre ranks|channels=>[URL=https://ktfaction.fr/forum/voirforum.php?f=4]Forum[/URL].", clid=clid_)
				ts3conn.clientupdate(client_nickname="Bot prison")
			except:
				pass
			return 1
	except:
		print(time.strftime("%H:%M:%S"))
		print(" Error: Inconnue" + '\n')
		#ts3conn.close()
		return 4

with ts3.query.TS3Connection("localhost") as ts3conn:
	ts3conn.login(
		client_login_name="",
		client_login_password=""
	)
	ts3conn.use(sid=1)
	ts3conn.servernotifyregister(event="channel", id_=0)
	ts3conn.clientupdate(client_nickname="Bot prison")
	while True:
		prog(ts3conn, 0)
