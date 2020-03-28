#!/usr/bin/Nessar

import time
import ts3
import re
import requests
import json
import MySQLdb

db = MySQLdb.connect(host="localhost",user="***REMOVED***",passwd="***REMOVED***", db="forum")
cur = db.cursor()

def prog(ts3conn, cur):
	try:
		event = ts3conn.wait_for_event(60)
	except:
		return 3
	if event[0]["ctid"] == "156":
		siteuid = ""
		clid_ = event[0]["clid"]
		cluid_ = ts3conn.clientgetuidfromclid(clid=clid_)
		name = cluid_[0]['nickname']
		cur.execute("SELECT * FROM `forum_membres` WHERE `membre_pseudo` = '"+name+"'")
		for row in cur.fetchall():
			siteuid = row[19]
		if siteuid != "":
			ts3conn.clientpoke(msg="UID: "+str(cluid_[0]['cluid']), clid=clid_)
			ts3conn.clientpoke(msg="Code Secret: "+siteuid, clid=clid_)
		else:
			ts3conn.clientpoke(msg="Vous devez avoir le même pseudo que sur le site", clid=clid_)

		return 4

def steam(ts3conn, cur):
	cur.execute("SELECT * FROM forum_membres")
	for row in cur.fetchall():
		try:
			jeu = 0
			steam = row[6]
			tsuid = row[8]
			if tsuid is not None:
				if steam is not None:
					steamname = steam[30:]
					try:
						response = requests.get("http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=***REMOVED***&vanityurl="+steamname)
					except:
						jeu = 0
					info = json.loads(response.text)

					if info['response']['success'] == 1:
						steamid = info['response']['steamid']
						try:
							response = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=***REMOVED***&steamids="+steamid)
						except:
							jeu = 0
						info = json.loads(response.text)
						try:
							jeu = info['response']['players'][0]['gameextrainfo']
						except:
							jeu = 0
					elif info['response']['success'] == 42:
						if len(steamname) == 17:
							try:	
								response = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=***REMOVED***&steamids="+steamname)
							except:
								jeu = 0
							info = json.loads(response.text)
							try:
								jeu = info['response']['players'][0]['gameextrainfo']
							except:
								jeu = 0

					addjeu(ts3conn, tsuid, jeu)
		except:
			pass

def addjeu(ts3conn, tsuid, jeu):
	if jeu != 0:
		sglist = ts3conn.servergrouplist()
		cldbid_ = ts3conn.clientgetdbidfromuid(cluid=tsuid)
		cldbid_ = cldbid_[0]['cldbid']
		i = 0
		stop = 0
		c = 0
		while stop != 2:
			try :
				a = sglist[i]['name']
				b = sglist[i]['sgid']
				try:
					clids = ts3conn.clientgetids(cluid=tsuid)
				except:
					break
				clid_ = clids[0]['clid']
				clinfo = ts3conn.clientinfo(clid=clid_)
				clsg = clinfo[0]['client_servergroups']
				if re.search(a, jeu[0:30]) is not None:
					stop = 2
					n = 240
					while n < 300:
						if re.search(str(n), clsg) is not None:
							if re.search(b, clsg) is None:
								sgdel = n
								ts3conn.servergroupdelclient(sgid=sgdel, cldbid=cldbid_)
								ts3conn.servergroupaddclient(sgid=b, cldbid=cldbid_)
								return 4
						n = n + 1
					clinfo = ts3conn.clientinfo(clid=clid_)
					clsg = clinfo[0]['client_servergroups']
					if re.search(b, clsg) is None:
						ts3conn.servergroupaddclient(sgid=b, cldbid=cldbid_)
						return 4
				i = i + 1
			except:
				ts3conn.servergroupadd(name=jeu[0:30])
				sglist = ts3conn.servergrouplist()
				while True:
					try:
						d = sglist[c]['sgid']
						c = c + 1
					except:
						ts3conn.servergroupaddperm(sgid=int(d), permsid="i_group_show_name_in_tree", permvalue=2, permnegated=0, permskip=0)
						break
	elif jeu == 0:
		try:
			cldbid_ = ts3conn.clientgetdbidfromuid(cluid=tsuid)
			cldbid_ = cldbid_[0]['cldbid']
			clids = ts3conn.clientgetids(cluid=tsuid)
			clid_ = clids[0]['clid']
			clinfo = ts3conn.clientinfo(clid=clid_)
			clsg = clinfo[0]['client_servergroups']
			n = 240
			while n < 300:
				if re.search(str(n), clsg):
					sgdel = n
					ts3conn.servergroupdelclient(sgid=sgdel, cldbid=cldbid_)
					return 5
				n = n + 1
			return 5
		except:
			return 6

with ts3.query.TS3Connection("localhost") as ts3conn:
	ts3conn.login(
		client_login_name="***REMOVED***",
		client_login_password="***REMOVED***"
	)
	ts3conn.use(sid=1)
	ts3conn.clientupdate(client_nickname="Bot Steam")
	ts3conn.servernotifyregister(event="channel", id_=156)
	while True:
		ts3conn.send_keepalive()
		print("OK "+str(time.strftime("%H,%M,%S")))
		prog(ts3conn, cur)
		steam(ts3conn, cur)