#!/usr/bin/Nessar

import time
import ts3
import re
import requests
import json
import MySQLdb

db = MySQLdb.connect(host="localhost",user="***REMOVED***",passwd="***REMOVED***", db="forum")
cur = db.cursor()
apikey = "***REMOVED***"

def prog(ts3conn, cur):
	cur.execute("SELECT * FROM forum_membres")
	for row in cur.fetchall():
		loli = row[7]
		tsuid = row[8]
		if tsuid != None:
			if loli != None:
				try:
					cldbid_ = ts3conn.clientgetdbidfromuid(cluid=tsuid)
					cldbid_ = cldbid_[0]['cldbid']
					clids = ts3conn.clientgetids(cluid=tsuid)
					clid_ = clids[0]['clid']
					clinfo = ts3conn.clientinfo(clid=clid_)
					clsg = clinfo[0]['client_servergroups']
					if re.search("36", clsg):
						lol(ts3conn, cur, loli, tsuid)
					if re.search("41", clsg):
						tft(ts3conn, cur, loli, tsuid)
				except:
					pass

def tft(ts3conn,cur,lol,tsuid):
	cur.execute("SELECT * FROM forum_membres")
	try:
		response = requests.get("https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+lol+"?api_key="+apikey)
	except:
		rank = 0
		tier = 0
	info = json.loads(response.text)
	if info['id'] != '':
		lolid = info['id']
		try:
			response = requests.get("https://euw1.api.riotgames.com/tft/league/v1/entries/by-summoner/"+lolid+"?api_key="+apikey)
		except:
			rank = 0
			tier = 0
		info = json.loads(response.text)
		try:
			rank = info[0]['tier']
			tier = info[0]['rank']
		except:
			rank = 0
			tier = 0
	addrank(ts3conn, rank, tier, tsuid, 1)

def lol(ts3conn,cur,lol,tsuid):
	cur.execute("SELECT * FROM forum_membres")
	try:
		response = requests.get("https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+lol+"?api_key="+apikey)
	except:
		rank = 0
		tier = 0
	info = json.loads(response.text)
	if info['id'] != '':
		lolid = info['id']
		try:
			response = requests.get("https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+lolid+"?api_key="+apikey)
		except:
			rank = 0
			tier = 0
		info = json.loads(response.text)
		try:
			rank1 = info[0]['tier']
			tier1 = info[0]['rank']
			try:
				rank2 = info[1]['tier']
				tier2 = info[1]['rank']
				if rankchiffre(rank1) == rankchiffre(rank2):
					rank = rank1
					if romainlatin(tier1) > romainlatin(tier2):
						tier = tier1
						print(tier1+lol)
					else:
						tier = tier2
						print(tier2+lol)
				elif rankchiffre(rank1) > rankchiffre(rank2):
					rank = rank1
					tier = tier1
				else:
					rank = rank2
					tier = tier2
			except:
				rank = rank1
				tier = tier1
		except:
			rank = 0
			tier = 0
	addrank(ts3conn, rank, tier, tsuid, 0)

def addrank(ts3conn, rank, tier, tsuid, jeu):
	if jeu == 0:
		a = None
		if rank != 0:
			sglist = [[162,163,164,165],[167,168,169,170],[171,172,173,174],[175,176,177,178],[179,180,181,182],[183,184,185,186],187,188,189]
			cldbid_ = ts3conn.clientgetdbidfromuid(cluid=tsuid)
			cldbid_ = cldbid_[0]['cldbid']
			clids = ts3conn.clientgetids(cluid=tsuid)
			clid_ = clids[0]['clid']
			clinfo = ts3conn.clientinfo(clid=clid_)
			clsg = clinfo[0]['client_servergroups']
			a = romainlatin(tier)
			b = rankchiffre(rank)
			if a == 0:
				sgadd = sglist[b]
			else:
				sgadd = sglist[b][a-1]
			n = 162
			while n <= 189:
				if re.search(str(n), clsg):
					if n == sgadd:
						return 5
					sgdel = n
					ts3conn.servergroupdelclient(sgid=int(sgdel), cldbid=cldbid_)
					break
				n = n + 1
			ts3conn.servergroupaddclient(sgid=int(sgadd), cldbid=cldbid_)
	elif jeu ==1:
		a = None
		if rank != 0:
			sglist = [[190,191,192,193],[194,195,196,197],[198,199,200,201],[202,203,204,205],[206,207,208,209],[210,211,212,213],214,215,216]
			cldbid_ = ts3conn.clientgetdbidfromuid(cluid=tsuid)
			cldbid_ = cldbid_[0]['cldbid']
			clids = ts3conn.clientgetids(cluid=tsuid)
			clid_ = clids[0]['clid']
			clinfo = ts3conn.clientinfo(clid=clid_)
			clsg = clinfo[0]['client_servergroups']
			a = romainlatin(tier)
			b = rankchiffre(rank)
			if a == 0:
				sgadd = sglist[b]
			else:
				sgadd = sglist[b][a-1]
			n = 190
			while n <= 216:
				if re.search(str(n), clsg):
					if n == sgadd:
						return 5
					sgdel = n
					ts3conn.servergroupdelclient(sgid=int(sgdel), cldbid=cldbid_)
					break
				n = n + 1
			ts3conn.servergroupaddclient(sgid=int(sgadd), cldbid=cldbid_)

def romainlatin(a):
	if a == "I":
		b = 4
	elif a == "II":
		b = 3
	elif a == "III":
		b = 2
	elif a == "IV":
		b = 1
	else:
		b = 0
	return b

def rankchiffre(a):
	if a == "IRON":
		b = 0
	elif a == "BRONZE":
		b = 1
	elif a == "SILVER":
		b = 2
	elif a == "GOLD":
		b = 3
	elif a == "PLATINUM":
		b = 4
	elif a == "DIAMOND":
		b = 5
	elif a == "MASTER":
		b = 6
	elif a == "GRANDMASTER":
		b = 7
	elif a == "CHALLENGER":
		b = 8
	return b

with ts3.query.TS3Connection("localhost") as ts3conn:
	ts3conn.login(
		client_login_name="***REMOVED***",
		client_login_password="***REMOVED***"
	)
	ts3conn.use(sid=1)
	ts3conn.clientupdate(client_nickname="Bot LoL")
	while True:
		prog(ts3conn,cur)
		time.sleep(60)