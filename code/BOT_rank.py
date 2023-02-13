#!/usr/bin/Nessar3

import time
import ts3
import re
import os

jeux = ['r6', 'csgo', 'rl', 'fortnite', 'pubg', 'lol', 'minecraft', 'gmod','tft']
groupe = ['27', '28', '29', '30', '31', '36', '37', '45','41']
jeuxstr = ", ".join(jeux)

def prog(ts3conn, jeux, groupe):
	ts3conn.send_keepalive()
	a = -1
	success = 0
	try:
		event = ts3conn.wait_for_event(240)
		print(time.strftime("%H:%M:%S"))
		print(' Info: Evenement' + '\n')
	except:
		print(time.strftime("%H:%M:%S"))
		print('Warning: Timeout' + '\n')
		return 2
	try:
		Iid = event[0]["invokerid"]
		Iuid = event[0]["invokeruid"]
		Idbid = ts3conn.clientdbfind(pattern=Iuid, uid=True)
		Idbid = Idbid[0]['cldbid']
		msg = event[0]['msg']
		msg = msg.lstrip(' ').rstrip(' ')
		msg = msg.lower()
	except:
		print(time.strftime("%H:%M:%S"))
		print('Error: DBid' + '\n')
		return 2
	if msg[:5] == "!rank" :
		if msg[6:9] == "ask":
			for i in jeux:
				a += 1
				if msg[10:] == i:
					clinfo = ts3conn.clientinfo(clid=Iid)
					clsg = clinfo[0]['client_servergroups']
					if re.search(groupe[a], clsg) is None:
						ts3conn.servergroupaddclient(sgid=int(groupe[a]), cldbid=int(Idbid))
						ts3conn.sendtextmessage(targetmode=2, target=131, msg="Vous avez bien été ajouté au groupe")
						success = 1
					else:
						ts3conn.sendtextmessage(targetmode=2, target=131, msg="Vous avez déjà ce grade ! Si vous voulez le supprimer faites: !grade del "+i)
			if success == 0:
				ts3conn.sendtextmessage(targetmode=2, target=131, msg="Seuls les jeux: "+jeuxstr+" sont acceptés pour l'instant. Si vous en voulez d'autre => [URL=https://nessar.fr/forum/voirforum.php?f=4]Forum[/URL].")
		elif msg[6:9] == "del":
			for i in jeux:
				a += 1
				if msg[10:] == i:
					clinfo = ts3conn.clientinfo(clid=Iid)
					clsg = clinfo[0]['client_servergroups']
					if re.search(groupe[a], clsg) is not None:
						ts3conn.servergroupdelclient(sgid=int(groupe[a]), cldbid=int(Idbid))
						ts3conn.sendtextmessage(targetmode=2, target=131, msg="Vous avez bien été supprimé au groupe")
						success = 1
					else:
						ts3conn.sendtextmessage(targetmode=2, target=131, msg="Vous n'avez pas ce grade ! Si vous voulez l'ajouter faites: !grade ask "+i)
			if success == 0:
				ts3conn.sendtextmessage(targetmode=2, target=131, msg="Seuls les jeux: "+jeuxstr+" sont acceptés pour l'instant. Si vous en voulez d'autre => [URL=https://nessar.fr/forum/voirforum.php?f=4]Forum[/URL].")
	elif msg[:5] == "!help":
		ts3conn.sendtextmessage(targetmode=2, target=131, msg="Voici la liste des commandes:")
		ts3conn.sendtextmessage(targetmode=2, target=131, msg="!rank ask")
		ts3conn.sendtextmessage(targetmode=2, target=131, msg="!rank del")
		ts3conn.sendtextmessage(targetmode=2, target=131, msg="Seuls les jeux: "+jeuxstr+" sont acceptés pour l'instant. Si vous en voulez d'autre => [URL=https://nessar.fr/forum/voirforum.php?f=4]Forum[/URL].")

	else:
		ts3conn.sendtextmessage(targetmode=2, target=131, msg="Commande incorrecte")

with ts3.query.TS3Connection("localhost") as ts3conn:
	ts3conn.login(
		client_login_name="",
		client_login_password=""
	)
	ts3conn.use(sid=1)
	ts3conn.clientupdate(client_nickname="Bot grade")
	ts3conn.servernotifyregister(event="textchannel")	
	clidbot = ts3conn.clientfind(pattern="Bot grade")
	ts3conn.clientmove(clid=clidbot[0]['clid'], cid=131)
	while True:
		prog(ts3conn, jeux, groupe)
