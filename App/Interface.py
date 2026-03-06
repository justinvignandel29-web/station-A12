class Interface:
   def __init__(self, ecran_initial=1, luminosite=100, theme_defaut="Clair"):
       """
       Initialise les paramètres d'affichage de l'interface.
       """
       # Attributs demandés dans le tableau
       self.ecran_actif = ecran_initial      # ID de la page actuelle
       self.luminosite_ecran = luminosite    # Niveau de luminosité
       self.theme = theme_defaut             # Mode sombre ou clair


   def rafraichir(self):
       """
       Met à jour les valeurs à l'écran.
       """
       print(f"\n--- RAFRAÎCHISSEMENT DE L'INTERFACE ---")
       print(f"Page actuelle  : {self.ecran_actif}")
       print(f"Luminosité     : {self.luminosite_ecran}%")
       print(f"Thème utilisé  : {self.theme}")
       print("---------------------------------------")


   def afficher_erreur(self, message):
       """
       Déclenche une alerte visuelle en cas de problème.
       """
       print(f"⚠️  ALERTE INTERFACE : {message}")


   def changer_page(self, nouvel_id):
       """
       Gère la navigation dans l'interface.
       """
       print(f"Navigation : Passage de la page {self.ecran_actif} à la page {nouvel_id}")
       self.ecran_actif = nouvel_id
       # Après un changement de page, on rafraîchit automatiquement l'écran
       self.rafraichir()


#---------Yohan_Dixneuf_Lina_Ouaarab_main_class_interface—----------
# Exemple d'utilisation technique
# ------------------------------------------------------------------


if __name__ == "__main__":
   # 1. Création de l'objet interface
   mon_interface = Interface(ecran_initial=1, luminosite=80, theme_defaut="Sombre")


   # 2. Affichage de l'état initial
   mon_interface.rafraichir()


   # 3. Simulation d'une navigation vers la page 2
   mon_interface.changer_page(2)


   # 4. Simulation d'une erreur (ex: capteur non détecté)
   mon_interface.afficher_erreur("Signal perdu avec la caméra")