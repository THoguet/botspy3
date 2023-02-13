#!/usr/bin/Nessar3

import time
import ts3
import re

def prog(ts3conn):
	try:
		ts3conn.send_keepalive()	
		event = ts3conn.wait_for_event(240)
		if event[0]["reasonid"] == '0' and event[0]["client_type"] != 1:
				ts3conn.servergroupaddclient(sgid=35, cldbid=int(event[0]["client_database_id"]))
				ts3conn.servergroupaddclient(sgid=43, cldbid=int(event[0]["client_database_id"]))
				ts3conn.servergroupaddclient(sgid=34, cldbid=int(event[0]["client_database_id"]))
				ts3conn.servergroupaddclient(sgid=33, cldbid=int(event[0]["client_database_id"]))
				ts3conn.servergroupaddclient(sgid=44, cldbid=int(event[0]["client_database_id"]))
				ts3conn.servergroupaddclient(sgid=8, cldbid=int(event[0]["client_database_id"]))
				return 1
	except:
		return 2
				
with ts3.query.TS3Connection("localhost") as ts3conn:
	ts3conn.login(
		client_login_name="",
		client_login_password=""
	)
	ts3conn.use(sid=1)
	ts3conn.clientupdate(client_nickname="Bot nouveaux")
	ts3conn.servernotifyregister(event="server")
	while True:
		prog(ts3conn)
