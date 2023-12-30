#!/bin/bash
# Challenge Linux : Script de Sauvegarde
# Ce script crée une sauvegarde compressée d'un répertoire source spécifié.

SOURCE_DIR="/path/to/source"  # Répertoire source à sauvegarder.
BACKUP_DIR="/path/to/backup"  # Répertoire de destination pour la sauvegarde.

# Vérification de l'existence des répertoires source et de destination.
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Erreur : Le répertoire source $SOURCE_DIR n'existe pas."
    exit 1
fi

if [ ! -d "$BACKUP_DIR" ]; then
    echo "Erreur : Le répertoire de sauvegarde $BACKUP_DIR n'existe pas."
    exit 1
fi

# Création de l'archive compressée.
FILENAME="backup-$(basename $SOURCE_DIR)-$(date +%Y%m%d-%H%M%S).tar.gz"
tar -czf $BACKUP_DIR/$FILENAME $SOURCE_DIR

echo "Sauvegarde réussie de $SOURCE_DIR dans $FILENAME."
