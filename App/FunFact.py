import random




class FunFact:
   def __init__(self, liste_anecdotes, index_jour=0):
       """
       Initialise la base d'anecdotes.
       """
       self.liste_anecdotes = liste_anecdotes  # Une liste de chaînes de caractères
       self.index_jour = index_jour  # Un entier pour suivre la progression


   def get_random_fact(self):
       """Sélectionne et retourne une anecdote au hasard"""
       if not self.liste_anecdotes:
           return "Aucune anecdote disponible."


       anecdote = random.choice(self.liste_anecdotes)
       return f"Le saviez-vous ? : {anecdote}"


   def update_base(self, nouvelle_anecdote):
       """Ajoute une nouvelle anecdote à la liste existante"""
       self.liste_anecdotes.append(nouvelle_anecdote)
       print(f"[BASE] Nouvelle anecdote ajoutée. Total : {len(self.liste_anecdotes)}")




#---------Yohan_Dixneuf_Louis_Bourgouin_main_class_camera—-----------
# Exemple d'utilisation technique
# ------------------------------------------------------------------


# Données d'exemple
mes_anecdotes = [
   "Les pieuvres ont trois cœurs.",
   "Le miel est le seul aliment qui ne se périme jamais.",
   "Un nuage peut peser plusieurs tonnes."
]


# Création de l'objet
divertissement = FunFact(mes_anecdotes)


# Utilisation des méthodes
print(divertissement.get_random_fact())
divertissement.update_base("Les flamants roses sont roses à cause de leur nourriture.")
