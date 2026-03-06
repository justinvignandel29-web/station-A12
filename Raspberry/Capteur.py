class Capteur:
    nom = "Capteur"
    unite = ""
    min_val = None
    max_val = None

    def __init__(self, identifiant=""):
        self.identifiant = identifiant

    def convertir_trame(self, trame: str):
        """
        Convertit une trame du type "(12,5,8)" en liste de nombres.
        Vérifie aussi que chaque valeur est dans l'intervalle autorisé.
        """
        if not isinstance(trame, str):
            raise TypeError("La trame doit être une chaîne de caractères.")

        trame = trame.strip()

        if not trame.startswith("(") or not trame.endswith(")"):
            raise ValueError(f"Trame invalide : {trame}")

        contenu = trame[1:-1].strip()
        if not contenu:
            return []

        try:
            valeurs = [float(x.strip()) for x in contenu.split(",")]
        except ValueError:
            raise ValueError(f"Valeur non numérique dans la trame : {trame}")

        for v in valeurs:
            if self.min_val is not None and v < self.min_val:
                raise ValueError(
                    f"Valeur {v}{self.unite} inférieure au minimum autorisé ({self.min_val}{self.unite})"
                )
            if self.max_val is not None and v > self.max_val:
                raise ValueError(
                    f"Valeur {v}{self.unite} supérieure au maximum autorisé ({self.max_val}{self.unite})"
                )

        return valeurs

    def _aplatir_periode(self, periode_brute):
        """
        Si on reçoit une liste de listes, on l'aplatit.
        Sinon on retourne directement la liste.
        """
        if not periode_brute:
            return []

        if isinstance(periode_brute[0], list):
            trames = []
            for bloc in periode_brute:
                trames.extend(bloc)
            return trames

        return periode_brute

    def _calculer_sur_trames(self, trames, operation: str):
        journaliers = []

        for trame in trames:
            donnees = self.convertir_trame(trame)
            if not donnees:
                continue

            if operation == "min":
                v = min(donnees)
            elif operation == "max":
                v = max(donnees)
            elif operation == "moyenne":
                v = sum(donnees) / len(donnees)
            else:
                raise ValueError("Opération inconnue")

            journaliers.append(v)

        if not journaliers:
            raise ValueError("Aucune donnée valide.")

        if operation == "moyenne":
            global_val = sum(journaliers) / len(journaliers)
        elif operation == "min":
            global_val = min(journaliers)
        else:
            global_val = max(journaliers)

        return journaliers, global_val

    def min_semaine(self, semaine):
        return self._calculer_sur_trames(semaine, "min")

    def max_semaine(self, semaine):
        return self._calculer_sur_trames(semaine, "max")

    def moyenne_semaine(self, semaine):
        return self._calculer_sur_trames(semaine, "moyenne")

    def min_mois(self, mois):
        trames = self._aplatir_periode(mois)
        return self._calculer_sur_trames(trames, "min")

    def max_mois(self, mois):
        trames = self._aplatir_periode(mois)
        return self._calculer_sur_trames(trames, "max")

    def moyenne_mois(self, mois):
        trames = self._aplatir_periode(mois)
        return self._calculer_sur_trames(trames, "moyenne")

    def info(self):
        return f"{self.nom} [{self.unite}] (id={self.identifiant})"


# ------------------ Capteurs spécialisés ------------------

class Pluie(Capteur):
    unite = "mm"
    nom = "Pluviométrie"
    min_val = 0
    max_val = 200


class Soleil(Capteur):
    unite = "W/m²"
    nom = "Index UV"
    min_val = 0
    max_val = 1500


class Vent(Capteur):
    unite = "km/h"
    nom = "Vitesse vent"
    min_val = 0
    max_val = 150


class Pression(Capteur):
    unite = "hPa"
    nom = "Pression Atmo"
    min_val = 950
    max_val = 1050


class Temperature(Capteur):
    unite = "°C"
    nom = "Température"
    min_val = -10
    max_val = 40


class Batterie(Capteur):
    unite = "%"
    nom = "Niveau Énergie"
    min_val = 0
    max_val = 100

    def __init__(self, identifiant="", niveau_batterie=100.0):
        super().__init__(identifiant)
        self.mettre_a_jour_niveau(niveau_batterie)

    def mettre_a_jour_niveau(self, nouveau_niveau: float):
        if not (0 <= nouveau_niveau <= 100):
            raise ValueError("Le niveau de batterie doit être entre 0 et 100%.")
        self.niveau_batterie = float(nouveau_niveau)
        return self.niveau_batterie

    def afficher_etat_batterie(self):
        if self.niveau_batterie < 40:
            return f"Alerte : batterie faible ({self.niveau_batterie}%). Recharge nécessaire."
        return f"Batterie OK ({self.niveau_batterie}%)."


# =================================Khaled-CAPTEUR-Main-Classe==========================================


if __name__ == "__main__":

    donnees_semaine = [
        "(12,5,8)",
        "(20,15,22)",
        "(9,9,9)"
    ]

    capteurs = [
        Vent("V001"),
        Pluie("PL01"),
        Soleil("S001"),
        Pression("P001"),
        Temperature("T001"),
        Batterie("B001", 87)
    ]

    for cap in capteurs:
        print("\n---", cap.info(), "---")
        try:
            mins, min_global = cap.min_semaine(donnees_semaine)
            print("Min journaliers :", mins, "| Min global :", min_global)

            maxs, max_global = cap.max_semaine(donnees_semaine)
            print("Max journaliers :", maxs, "| Max global :", max_global)

            moys, moy_global = cap.moyenne_semaine(donnees_semaine)
            print("Moy journaliers :", moys, "| Moy globale :", moy_global)

        except Exception as e:
            print("Erreur détectée :", e)

    print("\nTest mise à jour batterie :")
    capteurs[-1].mettre_a_jour_niveau(65)
    print("Niveau MAJ :", capteurs[-1].niveau_batterie)

    print("\nTest erreur température impossible :")
    try:
        Temperature("T002").convertir_trame("(50)")
    except Exception as e:
        print("Erreur attendue :", e)

    batterie = Batterie("B001", 35)

    print(batterie.info())

    batterie.mettre_a_jour_niveau(30)
    print(batterie.afficher_etat_batterie())

# =================================FIN_De-DEMO-DU-TEST-DE-CAPTEUR==========================================
