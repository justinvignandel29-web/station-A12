class Camera:
   def __init__(self, resolution, format_image, chemin_stockage):
       """
       Initialise les propriétés techniques de la caméra.
       """
       self.resolution = resolution
       self.format_image = format_image
       self.chemin_stockage = chemin_stockage
       self.en_enregistrement = False


   def prendre_photo(self):
       """Action de capture d'image fixe"""
       print(f"[CAPTURE] Photo prise en {self.resolution} ({self.format_image})")
       print(f"[SYSTEME] Fichier enregistré dans : {self.chemin_stockage}")


   def enregistrer_flux(self):
       """Démarre l'enregistrement vidéo"""
       self.en_enregistrement = True
       print("[FLUX] Enregistrement vidéo démarré...")


   def get_statut(self):
       """Retourne l'état de fonctionnement du périphérique"""
       etat = "EN COURS D'ENREGISTREMENT" if self.en_enregistrement else "PRET / VEILLE"
       return f"Statut : {etat} | Résolution : {self.resolution}"


#----------------Yohan_Dixneuf_main_class_camera—-----------------
# Exemple d'utilisation technique
# ------------------------------------------------------------------


# On crée un objet camera_1 avec des paramètres spécifiques
camera_1 = Camera("4K", "JPG", "/data/media/shots/")


# On appelle les méthodes définies dans le tableau
print(camera_1.get_statut())
camera_1.prendre_photo()
