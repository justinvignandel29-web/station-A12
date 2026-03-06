# Il manque plus que de relier les valeurs réelles de la station météo à ce code

from datetime import datetime


class Verification:
    def __init__(self):
        self.liste_erreurs = []
        self.dernier_check = None
        self.etat_systeme = "INCONNU"
        # Prendre les valeurs du code de Khaled : c'est lui qui reçoit les valeurs de la station météo
        self.plages = {
            "temperature": (-20, 60),  # °C
            "pression": (300, 1100),  # hPa
            "pluie": (0, 500),  # mm
            "vent": (0, 200),  # km/h
            "luminosite": (100, 20000000)  # Ohm
        }

    def log_erreur(self, message, niveau="WARNING"):
        """
        Ajoute une erreur dans la liste.
        """
        erreur = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "niveau": niveau,
            "message": message
        }
        self.liste_erreurs.append(erreur)

    def verifier_connexion(self):
        """
        Simulation d'une vérification de connexion.
        """
        connexion_ok = True  # simulation

        if not connexion_ok:
            self.log_erreur("Connexion réseau indisponible", "CRITIQUE")

        return connexion_ok

    def auto_test(self):
        """
        Lance un diagnostic du système.
        """
        self.dernier_check = datetime.now()

        connexion = self.verifier_connexion()

        if connexion and len(self.liste_erreurs) == 0:
            self.etat_systeme = "OK"
        elif len(self.liste_erreurs) > 0:
            self.etat_systeme = "WARNING"
        else:
            self.etat_systeme = "INCONNU"

        return {
            "dernier_check": self.dernier_check,
            "etat_systeme": self.etat_systeme,
            "nombre_erreurs": len(self.liste_erreurs)
        }

    def verifier_plage(self, type_capteur, valeur):
        """Vérifie si la valeur est dans la plage normale"""
        min_val, max_val = self.plages[type_capteur]

        if valeur < min_val or valeur > max_val:
            return f"Valeur hors plage pour {type_capteur}"
        return "OK"

    def verifier_blocage(self, historique):
        """Détecte si la valeur est toujours identique"""
        if len(set(historique)) == 1:
            return "Capteur bloqué"
        return "OK"

    def verifier_variation_brutale(self, ancienne_valeur, nouvelle_valeur, seuil):
        """Détecte un changement trop rapide"""
        if abs(nouvelle_valeur - ancienne_valeur) > seuil:
            return "Variation anormale"
        return "OK"

    def verifier_tous_les_capteurs(self, donnees_capteurs):
        """
        Vérifie les plages de tous les capteurs.
        """
        resultats = {}

        for capteur, valeur in donnees_capteurs.items():

            if capteur in self.plages:

                resultat = self.verifier_plage(capteur, valeur)
                resultats[capteur] = resultat

                if resultat != "OK":
                    self.log_erreur(resultat)

            else:
                message = f"Capteur inconnu : {capteur}"
                resultats[capteur] = message
                self.log_erreur(message)

        return resultats


# =============Khaled--Main-Classe-Capteur===========================================================
# ======   Exemple des données reçues depuis l’Arduino (capteurs, états, mesures)   =========


if __name__ == "__main__":

    verif = Verification()

    print("===== Lancement du diagnostic =====\n")

    # Diagnostic système
    rapport = verif.auto_test()

    print("Etat du système :", rapport["etat_systeme"])
    print("Dernier check :", rapport["dernier_check"])
    print("Nombre d'erreurs :", rapport["nombre_erreurs"])
    print()

    # =============================
    # Données simulées des capteurs
    # =============================
    donnees_capteurs = {
        "temperature": 22,
        "pression": 950,
        "pluie": 5,
        "vent": 210,  # volontairement hors plage
        "luminosite": 50000
    }

    print("=== Vérification de tous les capteurs ===")

    resultats = verif.verifier_tous_les_capteurs(donnees_capteurs)

    for capteur, resultat in resultats.items():
        print(f"{capteur} -> {resultat}")

    print()

    # =============================
    # Test capteur bloqué
    # =============================
    print("=== Test capteur bloqué ===")

    historique = [30, 30, 30, 30]

    resultat_blocage = verif.verifier_blocage(historique)

    print("Historique :", historique, "->", resultat_blocage)

    if resultat_blocage != "OK":
        verif.log_erreur(resultat_blocage)

    print()

    # =============================
    # Test variation brutale
    # =============================
    print("=== Test variation brutale ===")

    ancienne_valeur = 20
    nouvelle_valeur = 50

    resultat_variation = verif.verifier_variation_brutale(
        ancienne_valeur,
        nouvelle_valeur,
        seuil=15
    )

    print(
        f"Ancienne={ancienne_valeur} Nouvelle={nouvelle_valeur} -> {resultat_variation}"
    )

    if resultat_variation != "OK":
        verif.log_erreur(resultat_variation)

    # =============================
    # Journal des erreurs
    # =============================
    print("\n=== Journal des erreurs ===")

    if len(verif.liste_erreurs) == 0:
        print("Aucune erreur détectée")
    else:
        for erreur in verif.liste_erreurs:
            print(f"[{erreur['date']}] {erreur['niveau']} - {erreur['message']}")

    print("\n===== Fin des tests =====")

