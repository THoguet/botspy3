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

rankelo = [[1100,1200,1300,1400,1500],[1600,1700,1800,1900,2000],[2100,2200,2300,2400,2500],[2600,2800,3000],[3200,3600,4000],[4400],[5000]]
rankts = [[217,218,219,220,221],[222,223,224,225,226],[227,228,229,230,231],[232,233,234],[235,236,237],[238],[239]]

def prog(ts3conn, cur):
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
	# print(r6)
	# print(pmmr)
	addrank(ts3conn, rankadd, tsuid)

def addrank(ts3conn, rankadd, tsuid):
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

with ts3.query.TS3Connection("localhost") as ts3conn:
	ts3conn.login(
		client_login_name="***REMOVED***",
		client_login_password=""
	)
	ts3conn.use(sid=1)
	ts3conn.clientupdate(client_nickname="Bot R6")
	while True:
		prog(ts3conn,cur)
		time.sleep(60)
