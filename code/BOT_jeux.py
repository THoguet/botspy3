#!/usr/bin/Nessar

import time
import ts3
import re
import requests
import json
import MySQLdb
import asyncio
import r6sapi as api

db = MySQLdb.connect(host="localhost",user="***REMOVED***",passwd="", db="forum")
cur = db.cursor()
apikeylol = ""
apikeytft = ""

rankelo = [[1100,1200,1300,1400,1500],[1600,1700,1800,1900,2000],[2100,2200,2300,2400,2500],[2600,2800,3000],[3200,3600,4000],[4400],[5000]]
rankts = [[217,218,219,220,221],[222,223,224,225,226],[227,228,229,230,231],[232,233,234],[235,236,237],[238],[239]]

def progr6(ts3conn, cur):
	cur.execute("SELECT * FROM forum_membres")
	for row in cur.fetchall():
		r6 = row[9]
		tsuid = row[8]
		if tsuid != None:
			if r6 != None:
				try:
					cldbid_ = ts3conn.clientgetdbidfromuid(cluid=tsuid)
					cldbid_ = cldbid_[0]['cldbid']
					clids = ts3conn.clientgetids(cluid=tsuid)
					clid_ = clids[0]['clid']
					clinfo = ts3conn.clientinfo(clid=clid_)
					clsg = clinfo[0]['client_servergroups']
					if re.search("27", clsg):
						r6rank(ts3conn, cur, r6, tsuid)
				except:
					pass

def r6rank(ts3conn, cur, r6, tsuid):
	cur.execute("SELECT * FROM forum_membres")
	# info = json.loads(response.text)
	try:
		async def run(a):
			auth = api.Auth("", "")
			player = await auth.get_player(a, api.Platforms.UPLAY)
			mmr2 = await player.get_rank(api.RankedRegions.EU)
			rank = mmr2.mmr
			await auth.close()
			return rank
		pmmr = asyncio.get_event_loop().run_until_complete(run(r6))
	except:
		rank = 0
		tier = 0
		pmmr = 0
	rankadd = 0
	if pmmr != 0:
		if pmmr <= 5000:
			for i in range(len(rankelo)):
				for i2 in range(len(rankelo[i])):
					if pmmr < rankelo[i][i2]:
						if i2 == 0:
							if i == 0:
								rankadd = str(rankts[i][i2])
								break
							else:
								rankadd = str(rankts[i-1][int(len(rankelo[i-1])-1)])
								break
						else:
							rankadd = str(rankts[i][i2-1])
							break
				if rankadd != 0:
					break

		else:
			rankadd = str(rankts[6][0])
	else:
		rankadd = 0
	print(r6)
	print(pmmr)
	time.sleep(5)
	addrankr6(ts3conn, rankadd, tsuid)

def addrankr6(ts3conn, rankadd, tsuid):
	if rankadd != 0:
			cldbid_ = ts3conn.clientgetdbidfromuid(cluid=tsuid)
			cldbid_ = cldbid_[0]['cldbid']
			clids = ts3conn.clientgetids(cluid=tsuid)
			clid_ = clids[0]['clid']
			clinfo = ts3conn.clientinfo(clid=clid_)
			clsg = clinfo[0]['client_servergroups']
			n = 217
			while n <= 239:
				if re.search(str(n), clsg):
					if n == int(rankadd):
						return 5
					sgdel = n
					ts3conn.servergroupdelclient(sgid=int(sgdel), cldbid=cldbid_)
					break
				n = n + 1
			ts3conn.servergroupaddclient(sgid=int(rankadd), cldbid=cldbid_)

def proglol(ts3conn, cur):
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
		response = requests.get("https://euw1.api.riotgames.com/tft/summoner/v1/summoners/by-name/"+lol+"?api_key="+apikeytft)
	except:
		rank = 0
		tier = 0
	info = json.loads(response.text)
	if info['id'] != '':
		lolid = info['id']
		try:
			response = requests.get("https://euw1.api.riotgames.com/tft/league/v1/entries/by-summoner/"+lolid+"?api_key="+apikeytft)
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
	addranklol(ts3conn, rank, tier, tsuid, 1)

def lol(ts3conn,cur,lol,tsuid):
	cur.execute("SELECT * FROM forum_membres")
	try:
		response = requests.get("https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+lol+"?api_key="+apikeylol)
	except:
		rank = 0
		tier = 0
	info = json.loads(response.text)
	if info['id'] != '':
		lolid = info['id']
		try:
			response = requests.get("https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+lolid+"?api_key="+apikeylol)
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
						# print(tier1+lol)
					else:
						tier = tier2
						# print(tier2+lol)
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
	addranklol(ts3conn, rank, tier, tsuid, 0)

def addranklol(ts3conn, rank, tier, tsuid, jeu):
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
		client_login_password=""
	)
	ts3conn.use(sid=1)
	ts3conn.clientupdate(client_nickname="Bot Jeux")
	while True:
		proglol(ts3conn,cur)
		time.sleep(60)
		progr6(ts3conn,cur)
		time.sleep(60)
