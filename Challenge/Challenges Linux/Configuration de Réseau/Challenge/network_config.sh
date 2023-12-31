#!/bin/bash
# Challenge Linux : Configuration de Réseau
# Ce script configure l'adresse IP statique et teste la connectivité.

CONFIGURE_IP() {
    echo "Configuration de l'adresse IP statique..."
    # Commandes pour configurer l'IP (à adapter selon l'environnement)
    # Exemple : ifconfig eth0 192.168.1.100 netmask 255.255.255.0
}

TEST_CONNECTIVITY() {
    echo "Test de connectivité..."
    # Commande pour tester la connectivité (par exemple, ping vers un serveur)
    # Exemple : ping -c 4 google.com
}

# Exécution des fonctions
CONFIGURE_IP
TEST_CONNECTIVITY
