#!/bin/bash

# Recevoir les valeurs du nombre d'octets reçus et envoyés par l'interface wlan0 du mobile pour la première fois
initial_line=$(adb shell cat /proc/net/dev | grep -w wlan0)
initial_received=$(echo "$initial_line" | awk '{print $2}') #initial_received <- nb octets reçus par wlan0
initial_sent=$(echo "$initial_line" | awk '{print $10}') #initial_sent <- nb octets envoyés par wlan0

# Boucle sur 100 secondes
for i in {1..100}; do
    sleep 1
    current_line=$(adb shell cat /proc/net/dev | grep -w wlan0)
    current_received=$(echo "$current_line" | awk '{print $2}')
    current_sent=$(echo "$current_line" | awk '{print $10}')

    # Octets envoyés/reçus cette seconde = octets envoyés/reçus maintenant - octets envoyés/reçus la seconde précédente
    bytes_sent=$((current_sent - initial_sent))
    bytes_received=$((current_received - initial_received))

    # Ecrire les valeurs dans les fichiers
    echo "$bytes_sent" >> network_bytes_sent_black.txt
    echo "$bytes_received" >> network_bytes_received_black.txt

    # On met à jour la valeur du nombre d'octets envoyés/reçus de la seconde précédente par les valeurs de la seconde courante
    # -> ces valeurs seront celles de la seconde précédente de la prochaine itération dans une seconde
    initial_sent=$current_sent
    initial_received=$current_received
done
