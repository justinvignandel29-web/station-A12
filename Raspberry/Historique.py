"""
A12
Membres :
Lina Ouaarab
Celia Navaud

Cette classe permet de traiter des trames météo et de les enregistrer
dans un fichier historique avec la date et l'heure.
"""

import datetime


class Historique:

    def __init__(self):
        # Liste qui stocke toutes les trames traitées
        self.donnees = []

    def traiter_trame(self, trame_brute):
        """
        Nettoie, découpe et convertit la trame en liste de floats.
        Exemple :
        "$ARDLM,21,60,500,15*" -> [21.0, 60.0, 500.0, 15.0]
        """
        try:
            # Vérification de la trame
            if not trame_brute:
                return None

            # Nettoyage des caractères inutiles
            trame_propre = trame_brute.strip().replace("$", "").replace("*", "")

            # Découpage de la trame
            elements = trame_propre.split(",")

            # Vérification qu'il y a bien des valeurs
            if len(elements) < 2:
                raise ValueError("Trame invalide")

            # Conversion des valeurs numériques
            valeurs = [float(x) for x in elements[1:]]

            # Ajout dans l'historique
            self.donnees.append(valeurs)

            return valeurs
        # retourne erreur si erreur dans la conversion de la trame
        except ValueError as e:
            print("Erreur conversion trame :", e)
            return None

    def enregistrer_trame(self, valeurs, nom_fichier="historique_meteo.txt"):

        #Enregistre les valeurs dans un fichier avec date et heure.

        if valeurs is None:
            return

        try:
            # Date et heure actuelles
            date_heure = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Format de la ligne
            ligne = f"{date_heure} | {valeurs}\n"

            # Écriture dans le fichier
            with open(nom_fichier, "a", encoding="utf-8") as fichier:
                fichier.write(ligne)

            #retourne erreur si un problème et rencontré
        except Exception as e:
            print("Erreur lors de l'enregistrement :", e)

    def get_donnees(self):

        # Retourne toutes les données enregistrées en mémoire.

        return self.donnees
# Célia-Navaud-Main-Historique
import time
from Historique import Historique


def main():
    historique = Historique()
    # On définit l'intervalle en secondes (30 minutes)
    INTERVALLE = 30 * 60

    print("Démarrage du relevé météo (toutes les 30 minutes)...")

    while True:
        # 1. Simulation de la réception d'une trame (à remplacer par votre lecture réelle)
        trame = "$ARDLM,21,60,500,15*"

        # 2. Traitement et enregistrement
        valeurs = historique.traiter_trame(trame)
        if valeurs:
            historique.enregistrer_trame(valeurs)
            print(f"Données enregistrées à {time.strftime('%H:%M:%S')} : {valeurs}")

        # 3. Pause du programme pendant 30 minutes
        print(f"Prochain relevé dans 30 minutes...")
        time.sleep(INTERVALLE)


if __name__ == "__main__":
    main()

