#!/usr/bin/Nessar3

import time
import ts3
import re

def prog(ts3conn):
	ts3conn.send_keepalive()
	try:
		event = ts3conn.wait_for_event(240)
		print(time.strftime("%H:%M:%S"))
		print(' Info: évenement' + '\n')
	except:
		print(time.strftime("%H:%M:%S"))
		print(' Warning: Timeout' + '\n')
		#ts3conn.close()
		return 2
	try:
		if event[0]["invokeruid"] == "***REMOVED***" or event[0]["invokeruid"] == "***REMOVED***" or event[0]["invokeruid"] == "***REMOVED***":
			msg = event[0]['msg']
			msg = msg.lstrip(' ').rstrip(' ')
			msg = msg.lower()
			Iid = event[0]['invokerid']
			if msg[:3] == "§kt":
				if msg[4:7] == "add":
					new = msg[8:]
					try:
						ts3conn.clientfind(pattern=new)
					except:
						ts3conn.clientpoke(msg="Pseudo incorrect !", clid=Iid)
						print(time.strftime("%H:%M:%S"))
						print(' Warning: Client introuvable' + '\n')
						#ts3conn.close()
						return 4
					newclid = ts3conn.clientfind(pattern=new)
					newinfo = ts3conn.clientinfo(clid=newclid[0]['clid'])
					newdb = newinfo[0]['client_database_id']
					newsg = newinfo[0]['client_servergroups']
					if re.search("21", newsg) is None:
						ts3conn.servergroupaddclient(sgid=21, cldbid=int(newdb))
						ts3conn.channelclientaddperm(cid=91, cldbid=int(newdb), permsid="i_channel_join_power", permvalue=75)
						ts3conn.channelclientaddperm(cid=92, cldbid=int(newdb), permsid="i_channel_join_power", permvalue=75)
						ts3conn.channelclientaddperm(cid=94, cldbid=int(newdb), permsid="i_channel_join_power", permvalue=75)
						ts3conn.clientpoke(msg=new+" a bien été ajouter à la KT", clid=Iid)
						ts3conn.clientpoke(msg="Félicitation pour votre recrutement "+new+" !", clid=newclid[0]['clid'])
					else:
						ts3conn.clientpoke(msg=new+" est déjà dans la KT !", clid=Iid)
				elif msg[4:7] == "del":
					gb = msg[8:]
					try:
						ts3conn.clientfind(pattern=gb)
					except:
						ts3conn.clientpoke(msg="Pseudo incorrect !", clid=Iid)
						print(time.strftime("%H:%M:%S"))
						print(' Warning: Client introuvable' + '\n')
						#ts3conn.close()
						return 4
					gbclid = ts3conn.clientfind(pattern=gb)
					gbinfo = ts3conn.clientinfo(clid=gbclid[0]['clid'])
					gbdb = gbinfo[0]['client_database_id']
					gbsg = gbinfo[0]['client_servergroups']
					if re.search("21", gbsg) is not None:
						ts3conn.servergroupdelclient(sgid=21, cldbid=int(gbdb))
						ts3conn.channelclientdelperm(cid=91, cldbid=int(gbdb), permsid="i_channel_join_power")
						ts3conn.channelclientdelperm(cid=92, cldbid=int(gbdb), permsid="i_channel_join_power")
						ts3conn.channelclientdelperm(cid=94, cldbid=int(gbdb), permsid="i_channel_join_power")
						ts3conn.clientpoke(msg=gb+" a bien été supprimé de la KT", clid=Iid)
						ts3conn.clientpoke(msg="Vous avez été expulsé de la KT "+gb+" !", clid=gbclid[0]['clid'])
					else:
						ts3conn.clientpoke(msg=gb+" n'est pas dans la KT !", clid=Iid)
				elif msg[4:6] == "on":
					info = ts3conn.channelfind(pattern="Recrutement")
					if info[0]['channel_name'][13:15] == "ON":
						ts3conn.clientpoke(msg="Le recrutement est déjà actif !", clid=Iid)
					else:
						ts3conn.channeledit(cid=95, channel_name="Recrutement [ON]", channel_description="[CENTER]La team K.T. [U]RECRUTE ![/U][/CENTER]")
						ts3conn.channeladdperm(cid=95, permsid="i_channel_needed_join_power", permvalue=0)
						ts3conn.clientpoke(msg="Le recrutement est désormais actif.", clid=Iid)

				elif msg[4:7] == "off":
					info = ts3conn.channelfind(pattern="Recrutement")
					if info[0]['channel_name'][13:15] == "OF":
						ts3conn.clientpoke(msg="Le recrutement est déjà inactif !", clid=Iid)
					else:
						ts3conn.channeledit(cid=95, channel_name="Recrutement [OFF]", channel_description="[CENTER]La team K.T. [U]NE RECRUTE PLUS[/U][/CENTER]")
						ts3conn.channeladdperm(cid=95, permsid="i_channel_needed_join_power", permvalue=75)
						ts3conn.clientpoke(msg="Le recrutement est désormais inactif.", clid=Iid)
				else:
					ts3conn.clientpoke(msg="Commande incorrecte (§kt on|off ou §kt add|del pseudo)", clid=Iid)
	except:
		print(time.strftime("%H:%M:%S"))
		print(' Error: Inconnu' + '\n')
		#ts3conn.close()
		return 5

with ts3.query.TS3Connection("localhost") as ts3conn:
	ts3conn.login(
		client_login_name="***REMOVED***",
		client_login_password="***REMOVED***"
	)
	ts3conn.use(sid=1)
	ts3conn.clientupdate(client_nickname="Bot KT")
	ts3conn.servernotifyregister(event="textserver") 
	while True:
			prog(ts3conn)
