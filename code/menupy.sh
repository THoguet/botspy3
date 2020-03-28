#!/bin/bash

function greenMessage() {
  echo -e "\\033[32;1m${*}\\033[0m"
}

function magentaMessage() {
  echo -e "\\033[35;1m${*}\\033[0m"
}

function cyanMessage() {
  echo -e "\\033[36;1m${*}\\033[0m"
}

function redMessage() {
  echo -e "\\033[31;1m${*}\\033[0m"
}

function yellowMessage() {
  echo -e "\\033[33;1m${*}\\033[0m"
}

if [ "$1" = "start" ]&&[ "$2" = "" ]; then
	yellowMessage '─────────────────────────────────'
	if ! screen -list | grep -q "BOT_rank"; then
		screen -dmS BOT_rank python3 ./BOT_rank.py
                sleep 1
		if ! screen -list | grep -q "BOT_rank"; then
			redMessage '[BOT_rank] ERROR'
		else
			greenMessage '[BOT_rank] Démarrer avec succès !'
		fi
	else
		greenMessage '[BOT_rank] déjà actif !'
	fi
	if ! screen -list | grep -q "BOT_new"; then
		screen -dmS BOT_new python3 ./BOT_new.py
                sleep 1
		if ! screen -list | grep -q "BOT_new"; then
			redMessage '[BOT_new] ERROR'
		else
			greenMessage '[BOT_new] Démarrer avec succès !'
		fi
	else
		greenMessage '[BOT_new] déjà actif !'
	fi
	if ! screen -list | grep -q "BOT_Anti-VPN"; then
		screen -dmS BOT_Anti-VPN python3 ./BOT_Anti-VPN.py
                sleep 1
		if ! screen -list | grep -q "BOT_Anti-VPN"; then
			redMessage '[BOT_Anti-VPN] ERROR'
		else
			greenMessage '[BOT_Anti-VPN] Démarrer avec succès !'
		fi
	else
		greenMessage '[BOT_Anti-VPN] déjà actif !'
	fi
	if ! screen -list | grep -q "BOT_prison"; then
		screen -dmS BOT_prison python3 ./BOT_prison.py
                sleep 1
		if ! screen -list | grep -q "BOT_prison"; then
			redMessage '[BOT_prison] ERROR'
		else
			greenMessage '[BOT_prison] Démarrer avec succès !'
		fi
	else
		greenMessage '[BOT_prison] déjà actif !'
	fi
	if ! screen -list | grep -q "BOT_KT"; then
		screen -dmS BOT_KT python3 ./BOT_KT.py
                sleep 1
		if ! screen -list | grep -q "BOT_KT"; then
			redMessage '[BOT_KT] ERROR'
		else
			greenMessage '[BOT_KT] Démarrer avec succès !'
		fi
	else
		greenMessage '[BOT_KT] déjà actif !'
	fi
	if ! screen -list | grep -q "BOT_steam"; then
		screen -dmS BOT_steam python3 ./BOT_steam.py
                sleep 1
		if ! screen -list | grep -q "BOT_steam"; then
			redMessage '[BOT_steam] ERROR'
		else
			greenMessage '[BOT_steam] Démarrer avec succès !'
		fi
	else
		greenMessage '[BOT_steam] déjà actif !'
	fi
	if ! screen -list | grep -q "BOT_jeux"; then
		screen -dmS BOT_jeux python3 ./BOT_jeux.py
                sleep 1
		if ! screen -list | grep -q "BOT_jeux"; then
			redMessage '[BOT_jeux] ERROR'
		else
			greenMessage '[BOT_jeux] Démarrer avec succès !'
		fi
	else
		greenMessage '[BOT_jeux] déjà actif !'
	fi
	# if ! screen -list | grep -q "BOT_R6"; then
	# 	screen -dmS BOT_R6 python3 ./BOT_R6.py
 #                sleep 1
	# 	if ! screen -list | grep -q "BOT_R6"; then
	# 		redMessage '[BOT_R6] ERROR'
	# 	else
	# 		greenMessage '[BOT_R6] Démarrer avec succès !'
	# 	fi
	# else
	# 	greenMessage '[BOT_R6] déjà actif !'
	# fi
	yellowMessage '─────────────────────────────────'
	
elif [ "$1" = "start" ]&&[ "$2" = "KT" ]; then
	yellowMessage '─────────────────────────────────'
	if ! screen -list | grep -q "BOT_KT"; then
		screen -dmS BOT_KT python3 ./BOT_KT.py
                sleep 1
		if ! screen -list | grep -q "BOT_KT"; then
			redMessage '[BOT_KT] ERROR'
		else
			greenMessage '[BOT_KT] Démarrer avec succès !'
	fi
	else
		redMessage '[BOT_KT] déjà actif !'
	fi
	yellowMessage '─────────────────────────────────'

elif [ "$1" = "start" ]&&[ "$2" = "new" ]; then
	yellowMessage '─────────────────────────────────'
	if ! screen -list | grep -q "BOT_new"; then
		screen -dmS BOT_new python3 ./BOT_new.py
                sleep 1
		if ! screen -list | grep -q "BOT_new"; then
			redMessage '[BOT_new] ERROR'
		else
			greenMessage '[BOT_new] Démarrer avec succès !'
	fi
	else
		redMessage '[BOT_new] déjà actif !'
	fi
	yellowMessage '─────────────────────────────────'

elif [ "$1" = "start" ]&&[ "$2" = "jeux" ]; then
	yellowMessage '─────────────────────────────────'
	if ! screen -list | grep -q "BOT_jeux"; then
		screen -dmS BOT_jeux python3 ./BOT_jeux.py
                sleep 1
		if ! screen -list | grep -q "BOT_jeux"; then
			redMessage '[BOT_jeux] ERROR'
		else
			greenMessage '[BOT_jeux] Démarrer avec succès !'
	fi
	else
		redMessage '[BOT_jeux] déjà actif !'
	fi
	yellowMessage '─────────────────────────────────'

# elif [ "$1" = "start" ]&&[ "$2" = "r6" ]; then
# 	yellowMessage '─────────────────────────────────'
# 	if ! screen -list | grep -q "BOT_R6"; then
# 		screen -dmS BOT_R6 python3 ./BOT_R6.py
#                 sleep 1
# 		if ! screen -list | grep -q "BOT_R6"; then
# 			redMessage '[BOT_R6] ERROR'
# 		else
# 			greenMessage '[BOT_R6] Démarrer avec succès !'
# 	fi
# 	else
# 		redMessage '[BOT_R6] déjà actif !'
# 	fi
	yellowMessage '─────────────────────────────────'

elif [ "$1" = "start" ]&&[ "$2" = "vpn" ]; then
	yellowMessage '─────────────────────────────────'
	if ! screen -list | grep -q "BOT_Anti-VPN"; then
		screen -dmS BOT_Anti-VPN python3 ./BOT_Anti-VPN.py
                sleep 1
		if ! screen -list | grep -q "BOT_Anti-VPN"; then
			redMessage '[BOT_Anti-VPN] ERROR'
		else
			greenMessage '[BOT_Anti-VPN] Démarrer avec succès !'
	fi
	else
		redMessage '[BOT_Anti-VPN] déjà actif !'
	fi
	yellowMessage '─────────────────────────────────'

elif [ "$1" = "start" ]&&[ "$2" = "prison" ]; then
	yellowMessage '─────────────────────────────────'
	if ! screen -list | grep -q "BOT_prison"; then
		screen -dmS BOT_prison python3 ./BOT_prison.py
                sleep 1
		if ! screen -list | grep -q "BOT_prison"; then
			redMessage '[BOT_prison] ERROR'
		else
			greenMessage '[BOT_prison] Démarrer avec succès !'
	fi
	else
		redMessage '[BOT_prison] déjà actif !'
	fi
	yellowMessage '─────────────────────────────────'

elif [ "$1" = "start" ]&&[ "$2" = "steam" ]; then
	yellowMessage '─────────────────────────────────'
	if ! screen -list | grep -q "BOT_steam"; then
		screen -dmS BOT_steam python3 ./BOT_steam.py
                sleep 1
		if ! screen -list | grep -q "BOT_steam"; then
			redMessage '[BOT_steam] ERROR'
		else
			greenMessage '[BOT_steam] Démarrer avec succès !'
	fi
	else
		redMessage '[BOT_steam] déjà actif !'
	fi
	yellowMessage '─────────────────────────────────'

elif [ "$1" = "start" ]&&[ "$2" = "rank" ]; then
	yellowMessage '─────────────────────────────────'
	if ! screen -list | grep -q "BOT_rank"; then
		screen -dmS BOT_rank python3 ./BOT_rank.py
                sleep 1
		if ! screen -list | grep -q "BOT_rank"; then
			redMessage '[BOT_rank] ERROR'
		else
			greenMessage '[BOT_rank] Démarrer avec succès !'
	fi
	else
		redMessage '[BOT_rank] déjà actif !'
	fi 
	yellowMessage '─────────────────────────────────'

elif [ "$1" = "stop" ]&&[ "$2" = "" ]; then
	screen -S BOT_new -X quit
	screen -S BOT_KT -X quit
	screen -S BOT_rank -X quit
	screen -S BOT_prison -X quit
	screen -S BOT_Anti-VPN -X quit
	screen -S BOT_steam -X quit
	screen -S BOT_jeux -X quit
	# screen -S BOT_R6 -X quit
    	sleep 2
	yellowMessage '─────────────────────────────────'
	if ! screen -list | grep -q "BOT_KT"; then
		redMessage '[BOT_KT] Arreté avec succès !'
	else
		greenMessage '[BOT_KT] Fontionne toujours !'
	fi
	if ! screen -list | grep -q "BOT_Anti-VPN"; then
		redMessage '[BOT_Anti-VPN] Arreté avec succès !'
	else
		greenMessage '[BOT_Anti-VPN] Fontionne toujours !'
	fi
	if ! screen -list | grep -q "BOT_prison"; then
		redMessage '[BOT_prison] Arreté avec succès !'
	else
		greenMessage '[BOT_prison] Fontionne toujours !'
	fi
	if ! screen -list | grep -q "BOT_new"; then
		redMessage '[BOT_new] Arreté avec succès !'
	else
		greenMessage '[BOT_new] Fontionne toujours !'
	fi
	if ! screen -list | grep -q "BOT_rank"; then
		redMessage '[BOT_rank] Arreté avec succès !'
	else
		greenMessage '[BOT_rank] Fontionne toujours !'
	fi
	if ! screen -list | grep -q "BOT_steam"; then
		redMessage '[BOT_steam] Arreté avec succès !'
	else
		greenMessage '[BOT_steam] Fontionne toujours !'
	fi
	if ! screen -list | grep -q "BOT_jeux"; then
		redMessage '[BOT_jeux] Arreté avec succès !'
	else
		greenMessage '[BOT_jeux] Fontionne toujours !'
	fi
	# if ! screen -list | grep -q "BOT_R6"; then
	# 	redMessage '[BOT_R6] Arreté avec succès !'
	# else
	# 	greenMessage '[BOT_R6] Fontionne toujours !'
	# fi
	yellowMessage '─────────────────────────────────'
	
elif [ "$1" = "stop" ] && [ "$2" = "KT" ]; then 
	if ! screen -list | grep -q "BOT_KT"; then
		yellowMessage '─────────────────────────────────'
		redMessage '[BOT_KT] Déjà inactif'
                yellowMessage '─────────────────────────────────'
	else
		screen -S BOT_KT -X quit
		sleep 1
		yellowMessage '─────────────────────────────────'
                if ! screen -list | grep -q "BOT_KT"; then
                                redMessage '[BOT_KT] Arreté avec succès !'
                        else
                                greenMessage '[BOT_KT] Fontionne toujours !'
                fi
                yellowMessage '─────────────────────────────────'
        fi

elif [ "$1" = "stop" ]&&[  "$2" = "prison" ]; then
	if ! screen -list | grep -q "BOT_prison"; then
		yellowMessage '─────────────────────────────────'
		redMessage '[BOT_prison] Déjà inactif'
		yellowMessage '─────────────────────────────────'
	else
		screen -S BOT_prison -X quit
                sleep 1
		yellowMessage '─────────────────────────────────'
		if ! screen -list | grep -q "BOT_prison"; then
				redMessage '[BOT_prison] Arreté avec succès !'
			else
				greenMessage '[BOT_prison] Fontionne toujours !'
		fi
		yellowMessage '─────────────────────────────────'
	fi

elif [ "$1" = "stop" ]&&[  "$2" = "jeux" ]; then
	if ! screen -list | grep -q "BOT_jeux"; then
		yellowMessage '─────────────────────────────────'
		redMessage '[BOT_jeux] Déjà inactif'
		yellowMessage '─────────────────────────────────'
	else
		screen -S BOT_jeux -X quit
                sleep 1
		yellowMessage '─────────────────────────────────'
		if ! screen -list | grep -q "BOT_jeux"; then
				redMessage '[BOT_jeux] Arreté avec succès !'
			else
				greenMessage '[BOT_jeux] Fontionne toujours !'
		fi
		yellowMessage '─────────────────────────────────'
	fi

# elif [ "$1" = "stop" ]&&[  "$2" = "r6" ]; then
# 	if ! screen -list | grep -q "BOT_R6"; then
# 		yellowMessage '─────────────────────────────────'
# 		redMessage '[BOT_R6] Déjà inactif'
# 		yellowMessage '─────────────────────────────────'
# 	else
# 		screen -S BOT_R6 -X quit
#                 sleep 1
# 		yellowMessage '─────────────────────────────────'
# 		if ! screen -list | grep -q "BOT_R6"; then
# 				redMessage '[BOT_R6] Arreté avec succès !'
# 			else
# 				greenMessage '[BOT_R6] Fontionne toujours !'
# 		fi
# 		yellowMessage '─────────────────────────────────'
# 	fi
	
elif [ "$1" = "stop" ]&&[  "$2" = "rank" ]; then
	if ! screen -list | grep -q "BOT_rank"; then
		yellowMessage '─────────────────────────────────'
		redMessage '[BOT_rank] Déjà inactif'
		yellowMessage '─────────────────────────────────'
	else
		screen -S BOT_rank -X quit
                sleep 1
		yellowMessage '─────────────────────────────────'
		if ! screen -list | grep -q "BOT_rank"; then
				redMessage '[BOT_rank] Arreté avec succès !'
			else
				greenMessage '[BOT_rank] Fontionne toujours !'
		fi
		yellowMessage '─────────────────────────────────'
	fi

elif [ "$1" = "stop" ]&&[  "$2" = "vpn" ]; then
	if ! screen -list | grep -q "BOT_Anti-VPN"; then
		yellowMessage '─────────────────────────────────'
		redMessage '[BOT_Anti-VPN] Déjà inactif'
		yellowMessage '─────────────────────────────────'
	else
		screen -S BOT_Anti-VPN -X quit
                sleep 1
		yellowMessage '─────────────────────────────────'
		if ! screen -list | grep -q "BOT_Anti-VPN"; then
				redMessage '[BOT_Anti-VPN] Arreté avec succès !'
			else
				greenMessage '[BOT_Anti-VPN] Fontionne toujours !'
		fi
		yellowMessage '─────────────────────────────────'
	fi

elif [ "$1" = "stop" ]&&[  "$2" = "new" ]; then
	if ! screen -list | grep -q "BOT_new"; then
		yellowMessage '─────────────────────────────────'
		redMessage '[BOT_new] Déjà inactif'
		yellowMessage '─────────────────────────────────'
	else
		screen -S BOT_new -X quit
                sleep 1
		yellowMessage '─────────────────────────────────'
		if ! screen -list | grep -q "BOT_new"; then
				redMessage '[BOT_new] Arreté avec succès !'
			else
				greenMessage '[BOT_new] Fontionne toujours !'
		fi
		yellowMessage '─────────────────────────────────'
	fi

elif [ "$1" = "stop" ]&&[  "$2" = "prison" ]; then
	if ! screen -list | grep -q "BOT_prison"; then
		yellowMessage '─────────────────────────────────'
		redMessage '[BOT_prison] Déjà inactif'
		yellowMessage '─────────────────────────────────'
	else
		screen -S BOT_prison -X quit
                sleep 1
		yellowMessage '─────────────────────────────────'
		if ! screen -list | grep -q "BOT_prison"; then
				redMessage '[BOT_prison] Arreté avec succès !'
			else
				greenMessage '[BOT_prison] Fontionne toujours !'
		fi
		yellowMessage '─────────────────────────────────'
	fi

elif [ "$1" = "stop" ]&&[  "$2" = "steam" ]; then
	if ! screen -list | grep -q "BOT_steam"; then
		yellowMessage '─────────────────────────────────'
		redMessage '[BOT_steam] Déjà inactif'
		yellowMessage '─────────────────────────────────'
	else
		screen -S BOT_steam -X quit
                sleep 1
		yellowMessage '─────────────────────────────────'
		if ! screen -list | grep -q "BOT_prison"; then
				redMessage '[BOT_steam] Arreté avec succès !'
			else
				greenMessage '[BOT_steam] Fontionne toujours !'
		fi
		yellowMessage '─────────────────────────────────'
	fi

elif [ "$1" = "status" ]; then

	yellowMessage '─────────────────────────────────'
	if ! screen -list | grep -q "BOT_KT"; then
		redMessage '[BOT_KT] Actuellement inactif !'
	else 
		greenMessage '[BOT_KT] Actuellement actif'
	fi
	
	if ! screen -list | grep -q "BOT_Anti-VPN"; then
		redMessage '[BOT_Anti-VPN] Actuellement inactif !'
	else 
		greenMessage '[BOT_Anti-VPN] Actuellement actif'
	fi

	if ! screen -list | grep -q "BOT_prison"; then
		redMessage '[BOT_prison] Actuellement inactif !'
	else
		greenMessage '[BOT_prison] Actuellement actif !'
	fi

    if ! screen -list | grep -q "BOT_rank"; then
            redMessage '[BOT_rank] Actuellement inactif !'
    else
            greenMessage '[BOT_rank] Actuellement actif !'
	fi

    if ! screen -list | grep -q "BOT_new"; then
            redMessage '[BOT_new] Actuellement inactif !'
    else
            greenMessage '[BOT_new] Actuellement actif !'
	fi

    if ! screen -list | grep -q "BOT_steam"; then
            redMessage '[BOT_steam] Actuellement inactif !'
    else
            greenMessage '[BOT_steam] Actuellement actif !'
	fi

    if ! screen -list | grep -q "BOT_jeux"; then
            redMessage '[BOT_jeux] Actuellement inactif !'
    else
            greenMessage '[BOT_jeux] Actuellement actif !'
	fi

 #    if ! screen -list | grep -q "BOT_R6"; then
 #            redMessage '[BOT_R6] Actuellement inactif !'
 #    else
 #            greenMessage '[BOT_R6] Actuellement actif !'
	# fi

    yellowMessage '─────────────────────────────────'

else
	yellowMessage 'Utilisation : ./start.sh <start|stop|status> <nom_du_BOT>'
fi
