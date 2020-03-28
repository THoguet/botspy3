#!/usr/bin/env python3

# Modules

import time
import ts3

#Variables

start = 1

pseudo = input("Choisir le pseudo: ")
if (pseudo == ""):
	exit()
	
delay = (input("Choisir le delai entre les pokes: "))
if (delay == ""):
	delay = 1
else:
	delay = float(delay)

msg = input("Choisir le message: ")
if (msg == ""):
	msg = "Je suis désolé :-)"

num = input("Choisir le nombre de poke(rien = infini): ")
if (num == ""):
	num = -1
else:
	num = int(num)

def poke(pseudo, delay, msg, num, ts3conn):			
		clients = ts3conn.clientfind(pattern=pseudo)
		clients = [client["clid"] for client in clients]
			
		while True:
			for clid in clients:
				ts3conn.clientpoke(msg=msg, clid=clid)
			time.sleep(delay)
			return num
with ts3.query.TS3Connection("localhost") as ts3conn:
		ts3conn.login(client_login_name="***REMOVED***", client_login_password="***REMOVED***")
		ts3conn.use(sid=1)
		while True:
			if poke(pseudo, delay, msg, num, ts3conn) > 0 or start == 1 or num == -1:
				start = 0
				if num != -1:
					num = num -1
				print(num)
			else:
				print("FINI")
				exit()
