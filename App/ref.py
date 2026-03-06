#le code a été réalisé à l'aide de la documentation pycharm sous indication de Mr Zirek


import sys


# On importe os pour pouvoir vérifier si un fichier existe sur l'ordinateur
import os


# On importe plusieurs éléments de PySide6 pour créer l'interface graphique
from PySide6.QtWidgets import (
  QApplication, QWidget, QVBoxLayout,   # éléments de base pour créer la fenêtre et organiser les widgets
  QPushButton, QInputDialog             # bouton et fenêtre pour demander une valeur à l'utilisateur
)


# On importe les classes nécessaires pour lire une vidéo et gérer le son
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput


# Widget spécial qui permet d'afficher la vidéo dans la fenêtre
from PySide6.QtMultimediaWidgets import QVideoWidget


# Outils utiles : QUrl pour les chemins de fichiers et Qt pour les alignements
from PySide6.QtCore import QUrl, Qt




# On crée une classe appelée VideoAccueil
# Elle hérite de QWidget, ce qui veut dire que notre classe est une fenêtre graphique
class VideoAccueil(QWidget):




  # La méthode __init__ est le constructeur de la classe
  # Elle est appelée automatiquement quand on crée un objet VideoAccueil
  def __init__(self):


      # On appelle le constructeur de la classe parent (QWidget)
      # C'est important pour que la fenêtre fonctionne correctement
      super().__init__()


      # On définit le titre de la fenêtre
      self.setWindowTitle("Lecteur vidéo météo")


      # On définit la taille de la fenêtre (largeur 800, hauteur 500)
      self.resize(800, 500)




      # ----------- Demande de la température -----------


      # On affiche une boîte de dialogue pour demander à l'utilisateur la température
      # getDouble permet de saisir un nombre décimal
      # La fonction renvoie deux valeurs :
      # - la température entrée
      # - un booléen (ok) qui indique si l'utilisateur a validé ou annulé
      self.temperature, ok = QInputDialog.getDouble(
          self,
          "Température",                     # titre de la fenêtre
          "Quelle température fait-il ?",    # message affiché
          decimals=1                         # nombre de décimales autorisées
      )




      # Si l'utilisateur annule la saisie, on ferme complètement le programme
      if not ok:
          sys.exit()




      # ----------- Création du layout -----------


      # Un layout sert à organiser les éléments dans la fenêtre
      # Ici on utilise un layout vertical (les éléments seront empilés)
      self.layout = QVBoxLayout()


      # On applique ce layout à la fenêtre principale
      self.setLayout(self.layout)




      # ----------- Création du lecteur vidéo -----------


      # QMediaPlayer est l'objet qui va lire la vidéo
      self.player = QMediaPlayer()


      # QAudioOutput sert à gérer le son de la vidéo
      self.audio = QAudioOutput()


      # On relie le lecteur vidéo à la sortie audio
      self.player.setAudioOutput(self.audio)




      # ----------- Zone d'affichage de la vidéo -----------


      # On crée un widget spécial pour afficher la vidéo
      self.videoWidget = QVideoWidget()


      # On fixe sa taille (640x360)
      self.videoWidget.setFixedSize(640, 360)


      # On ajoute ce widget dans le layout et on le centre
      self.layout.addWidget(self.videoWidget, alignment=Qt.AlignCenter)




      # On indique au lecteur vidéo où afficher la vidéo
      self.player.setVideoOutput(self.videoWidget)




      # ----------- Création du bouton fermer -----------


      # On crée un bouton avec le texte "FERMER"
      self.bouton_fermer = QPushButton("FERMER")


      # On définit sa taille
      self.bouton_fermer.setFixedSize(120, 40)


      # On applique un style CSS pour modifier son apparence
      self.bouton_fermer.setStyleSheet("""
          QPushButton {
              background-color: red;   # couleur de fond
              color: white;            # couleur du texte
              font-weight: bold;       # texte en gras
              border: none;            # pas de bordure
          }
          QPushButton:hover {
              background-color: darkred;  # couleur quand la souris passe dessus
          }
      """)


      # On ajoute le bouton dans le layout et on le centre
      self.layout.addWidget(self.bouton_fermer, alignment=Qt.AlignCenter)


      # Quand on clique sur le bouton, la fonction fermer_video sera exécutée
      self.bouton_fermer.clicked.connect(self.fermer_video)




      # On lance la vidéo au démarrage
      self.lancer_video()




  # ----------- Choix de la vidéo selon la température -----------


  def choisir_video(self):


      # Si la température est inférieure à 5°C
      if self.temperature < 5:
          # On retourne le chemin de la vidéo "très froid"
          return r"C:\video\Tarpinfroid.mov"


      # Si la température est entre 5°C et 20°C
      elif self.temperature < 20:
          # On retourne la vidéo "température tiède"
          return r"C:\video\Tarpintiede.mov"


      # Sinon (température >= 20°C)
      else:
          # On retourne la vidéo "chaud"
          return r"C:\video\Tarpinchaud.mov"




  # ----------- Lancement de la vidéo -----------


  def lancer_video(self):


      # On récupère le chemin de la vidéo à lire
      video_path = self.choisir_video()


      # On vérifie si le fichier vidéo existe bien sur l'ordinateur
      if os.path.exists(video_path):


          # On donne le chemin de la vidéo au lecteur
          self.player.setSource(QUrl.fromLocalFile(video_path))


          # On lance la lecture de la vidéo
          self.player.play()


      else:
          # Si la vidéo n'existe pas, on affiche un message dans la console
          print("Vidéo introuvable :", video_path)




  # ----------- Fonction pour fermer la vidéo -----------


  def fermer_video(self):


      # On arrête la lecture de la vidéo
      self.player.stop()


      # On ferme la fenêtre
      self.close()




# ----------- Point d'entrée du programme -----------


# Cette condition vérifie que le fichier est exécuté directement
# et pas importé comme module
if __name__ == "__main__":


  # QApplication est l'application principale qui gère l'interface graphique
  app = QApplication(sys.argv)


  # On crée une instance (un objet) de notre classe VideoAccueil
  window = VideoAccueil()


  # On affiche la fenêtre
  window.show()


  # On démarre la boucle principale de l'application
  # Le programme restera actif tant que la fenêtre est ouverte
  sys.exit(app.exec())


#==Loïck-Halle-Jules-David-Main-Class.VideoAccueil=====



