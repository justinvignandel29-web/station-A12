"""
A12
Membres :
Lina Ouaarab
Celia Navaud
Cette classe a pour but de creer un fichier historique afin de stocker les données
"""
from datetime import datetime


class Historique:
    def __init__(self):
        # Initialise la liste de stockage des relevés archivés
        self.donnees = []

    def traiter_trame(self, trame_brute):
        """
        Nettoie, découpe et convertit la trame en liste de floats.
        Exemple de trame : "$ARDLM,21,60,500,15*" -> [21.0, 60.0, 500.0, 15.0]
        """
        try:
            # Nettoyage : suppression des caractères de début ($) et de fin (*)
            trame_propre = trame_brute.strip().replace('$', '').replace('*', '')

            # Découpage : on sépare par les virgules et on ignore l'entête (ex: ARDLM)
            elements = trame_propre.split(',')

            # Conversion des valeurs numériques en float (on commence à l'index 1 pour sauter l'entête)
            valeurs_numeriques = [float(x) for x in elements[1:]]

            # Ajout à l'historique en mémoire
            self.donnees.append(valeurs_numeriques)

            return valeurs_numeriques
        except (ValueError, IndexError) as e:
            print(f"Erreur lors du traitement de la trame : {e}")
            return None