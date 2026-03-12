class RecommandationVetement:
   def __init__(self, categorie, seuil_froid):
       """
       Initialise la recommandation


       Args:
           categorie (str): Haut, Bas ou Accessoires
           seuil_froid (float): Température limite
       """
       self.categorie = categorie
       self.seuil_froid = seuil_froid
       self.conseil_actuel = ""


   def analyser_meteo(self, temperature, pluie):
       """
       Analyse la météo en fonction de la température et de la pluie
       """
       if temperature < self.seuil_froid:
           if pluie:
               self.conseil_actuel = f"Prévoir un {self.categorie} chaud et imperméable."
           else:
               self.conseil_actuel = f"Prévoir un {self.categorie} chaud."
       else:
           if pluie:
               self.conseil_actuel = f"Prévoir un {self.categorie} léger mais imperméable."
           else:
               self.conseil_actuel = f"Un {self.categorie} léger suffit."


   def generer_recommandation(self):
       """
       Retourne le conseil généré
       """
       return self.conseil_actuel




#----------------Yohan_Dixneuf_main_class_vêtement—-----------------
# Exemple des tenues en fonction de la météo
# ------------------------------------------------------------------


def main():
   # Création des catégories
   haut = RecommandationVetement("manteau", seuil_froid=10)    #vêtement haut du corps
   bas = RecommandationVetement("pantalon", seuil_froid=5)
#Vêtement bas du corps
   accessoires = RecommandationVetement("accessoires", seuil_froid=8)
#Création des accessoires


   # Exemple 1 : Il fait froid et il pleut
   print("---- Situation 1 : 5°C et pluie ----")
   haut.analyser_meteo(temperature=5, pluie=True)
   bas.analyser_meteo(temperature=5, pluie=True)
   accessoires.analyser_meteo(temperature=5, pluie=True)


#Création des recommandations pour un temps froid avec de la     pluie


   print(haut.generer_recommandation())
   print(bas.generer_recommandation())
   print(accessoires.generer_recommandation())


   print()


   # Exemple 2 : Il fait doux et pas de pluie
   print("---- Situation 2 : 18°C sans pluie ----")
   haut.analyser_meteo(temperature=18, pluie=False)
   bas.analyser_meteo(temperature=18, pluie=False)
   accessoires.analyser_meteo(temperature=18, pluie=False)


#Création des recommandations pour un temps doux avec de la     pluie


   print(haut.generer_recommandation())
   print(bas.generer_recommandation())
   print(accessoires.generer_recommandation())




if __name__ == "__main__":
   main()



