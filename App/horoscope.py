import random
import datetime


class Horoscope:
    def __init__(self):
        # Definition des signes
        self.signe_zodiaque = [
            "Bélier", "Taureau", "Gémeaux", "Cancer", "Lion", "Vierge",
            "Balance", "Scorpion", "Sagittaire", "Capricorne", "Poissons", "Verseau"
        ]

        # Defintion des phrases qui vont nous servir pour l'horoscope
        self.prevision_jour = [
            "Un petit effort aujourd’hui te permettra d’avoir une grande fierté demain.",
            "Ta créativité va t’aider à résoudre un problème compliqué.",
            "Un nouveau camarade pourrait devenir un super ami.",
            "Attention aux petits malentendus, explique-toi calmement.",
            "Un fou rire inattendu va illuminer ta journée.",
            "Ose essayer quelque chose de nouveau, tu pourrais adorer ça.",
            "Même si quelque chose semble difficile, tu as les capacités pour y arriver.",
            "Prends le temps de respirer si tu te sens stressé(e).",
            "Les étoiles te conseillent d’écouter ton cœur.",
            "Ton esprit d’équipe fera la différence.",
            "Les étoiles te conseillent d’écouter ton cœur, mais ton estomac a sûrement des choses très pertinentes à dire aussi.",
            "Même si quelque chose semble difficile, souviens-toi qu'il existe probablement un tutoriel sur Internet pour le faire à ta place.",
            "Ta patience portera ses fruits, ce qui tombe bien car les fruits, c'est plein de vitamines.",
            "Crois en tes rêves : continue de dormir.",
            "Chaque petit pas compte, surtout s'il te rapproche miraculeusement du frigo.",
            "Une idée de génie va te traverser l'esprit, mais tu vas malheureusement l'oublier le temps de trouver un stylo.",
            "Face à l'adversité, garde la tête haute, ça t'évitera au moins d'avoir un double menton sur les photos.",
            "Ton avenir est brillant, pense à prendre des lunettes de soleil.",
            "Jupiter s'aligne avec Mars : c'est le moment cosmique idéal pour ne rien changer à tes habitudes.",
            "La chance va te sourire aujourd'hui, tu vas réussir à brancher la clé USB du premier coup, un vrai miracle.",
            "Prends le temps de respirer après avoir monté les quatre étages avec ton sac de 12 kilos.",
            "Ta détermination est sans faille aujourd'hui, particulièrement pour ne pas croiser le regard du prof qui cherche un volontaire pour aller au tableau.",
            "Chaque petit pas compte, surtout s'il te rapproche discrètement de la sortie juste avant la sonnerie.",
            "La solution à ton problème est plus proche que tu ne le crois : elle est littéralement écrite dans la consigne que tu n'as pas lue.",
            "Fais la paix avec ton passé, oui, tu as appelé la prof 'Maman' en 6ème, mais promis, les gens ont (presque) oublié.",
            "Sors de ta zone de confort, va t'asseoir au premier rang aujourd'hui. Non, je plaisante, n'en fais pas trop non plus."
        ]

    def get_prediction(self, signe_zodiaque):
        date_jour = datetime.date.today()  # On associe la date du jour

        random.seed(
            str(date_jour))  # On transforme la date en texte pour éviter tout bug avec l'initialisation des random

        phrases_du_jour = random.sample(self.prevision_jour,
                                        len(self.signe_zodiaque))  # On selectionne une phrase aleatoirement sans repetition (on utilise sample)

        random.seed()  # On re-initialise la date pour le jour suivant

        index_signe = self.signe_zodiaque.index(
            signe_zodiaque)  # On cherche l'index du signe voulu et on pioche la phrase associée
        prediction = phrases_du_jour[index_signe]

        return prediction

    def afficher_horoscope(self):
        print("\n✨✨ HOROSCOPE DU JOUR ✨✨")

        for signe in self.signe_zodiaque:
            phrase = self.get_prediction(signe)
            print(f"{signe.capitalize().ljust(12)} : {phrase}")


# =======Polvent/Ravel_Main_Horoscope=============
if __name__ == "__main__":
    mon_horoscope = Horoscope()

    # On appelle la méthode avec le bon nom
    mon_horoscope.afficher_horoscope()

# =================================================
