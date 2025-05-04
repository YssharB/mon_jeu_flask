"""name= input("Entrez votre nom: ")
print("Bonjour",name," Bienvenue dans mon jeu d'aventure !")

doit_on_jouer = input("Voulez-vous jouer ? (Oui/Non): ").lower()
if doit_on_jouer== "oui":
    print("Super ! Commençons.")

    direction = input("La nuit est tombée sur la vallée silencieuse.\n Où voulez-vous aller ? (Gauche/Droite): ").lower()
    if direction == "gauche":

        print("Tu tournes à gauche, où le sentier disparaît peu à peu sous la brume...\n"
    )
        choix_gauche_oui= input("Au loin, un puits. Continuer dans cette direction ? (o/n)").lower()
        if choix_gauche_oui == "o":
         print("Tu te penches au-dessus du puits. Il est profond. Noir. Une odeur étrange s’en échappe.\n"
    "Puis une voix, rauque, s’élève des ténèbres :\n"
    "« Dis-moi, voyageur... sais-tu comment on sort d’une boucle while ? »\n"
    "Avant même que tu puisses répondre, le sol tremble. Tu glisses, tu tombes !\n"
    "Tu ouvres les yeux... et tu es devant un ordinateur, les yeux rouges, 35 onglets ouverts.\n"
    "Sur l’un d’eux, un article : *“Apprends Python en 24h — la méthode ultime”*.\n"
    "LinkedIn clignote : 2 likes sur ton post “J'ai appris Python en 24h”.\n"
    "Tu souris, un peu perdu, mais déterminé...\n"
    "Et tu relances le terminal.\n"
    "**Tu le sais : ça prendra plus que 24h.**")
        else: print("Tu te réveilles dans ton lit. Ton ordinateur est ouvert, l’onglet LinkedIn toujours actif.\n"
    "Un post te saute aux yeux : « J’ai appris Python en 24h, j’automatise tout maintenant 🔥 »\n"
    "Tu éclates de rire. C’était donc un cauchemar. Ou peut-être un message.\n"
    "Tu ouvres ton éditeur de code, tapes une ligne.\n"
    "SyntaxError.\n"
    "Tu souris encore. Ce n’est que le début. Mais cette fois, tu le sais : ça prendra plus que 24h.\n"
    "Et ce sera mille fois plus drôle.")
            
    elif direction == "droite":
        print("Tu tournes à droite, où le sentier disparaît peu à peu sous la brume...\n"
    )
        choix_droite_oui= input("Au loin, une cabane. Continuer dans cette direction ? (o/n)").lower()
        if choix_droite_oui == "o":
            print("Tu accélères, ton souffle devient haletant, les battements de ton cœur résonnent dans ta tête.\n"
    "La brume s’éclaircit un peu, laissant apparaître une petite cabane en ruine.\n"
    "Sa porte est entrouverte, et une faible lumière tremble à l’intérieur.\n")
            choix_cabane_oui = input("Y entrer ? (o/n)").lower()
            if choix_cabane_oui == "o":
                print("Tu franchis le seuil. À l’intérieur, des bougies éclairent un autel poussiéreux.\n"
    "Un vieux livre t’y attend. Sur la couverture : « Maîtriser Python en 24h ».\n"
    "Tu l’ouvres... rien que des pages blanches. Une seule phrase griffonnée tout au fond :\n"
    "\"Spoiler : il t’en faudra plus. »\n"
    "Tu souris, malgré tout. Quelqu’un est passé par là avant toi.")
            else:print("Tu te réveilles dans ton lit. Ton ordinateur est ouvert, l’onglet LinkedIn toujours actif.\n"
    "Un post te saute aux yeux : « J’ai appris Python en 24h, j’automatise tout maintenant 🔥 »\n"
    "Tu éclates de rire. C’était donc un cauchemar. Ou peut-être un message.\n"
    "Tu ouvres ton éditeur de code, tapes une ligne.\n"
    "SyntaxError.\n"
    "Tu souris encore. Ce n’est que le début. Mais cette fois, tu le sais : ça prendra plus que 24h.\n"
    "Et ce sera mille fois plus drôle."
    "#ApprentiDev #PythonDansLaBrume")
        
        else: print("Tu te réveilles dans ton lit. Ton ordinateur est ouvert, l’onglet LinkedIn toujours actif.\n"
    "Un post te saute aux yeux : « J’ai appris Python en 24h, j’automatise tout maintenant 🔥 »\n"
    "Tu éclates de rire. C’était donc un cauchemar. Ou peut-être un message.\n"
    "Tu ouvres ton éditeur de code, tapes une ligne.\n"
    "SyntaxError.\n"
    "Tu souris encore. Ce n’est que le début. Mais cette fois, tu le sais : ça prendra plus que 24h.\n"
    "Et ce sera mille fois moins drôle.")



else:
    print("Dommage peut-être une autre fois.")
    exit()"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def accueil():
    if request.method == "POST":
        nom = request.form.get("nom")
        return render_template("jeu.html", nom=nom, etape="intro", image="gauche ou droite.png")
    return render_template("accueil.html")

@app.route("/jeu", methods=["POST"])
def jeu():
    nom = request.form.get("nom")
    etape = request.form.get("etape")
    choix = request.form.get("choix")

    if etape == "intro":
        if choix == "gauche":
            texte = ""
            return render_template("jeu.html", nom=nom, etape="gauche", texte=texte, image="puit.png")
        elif choix == "droite":
            texte = ""
            return render_template("jeu.html", nom=nom, etape="droite", texte=texte, image="droite.png")

    elif etape == "gauche":
        if choix == "o":
            texte = "« Dis-moi... sais-tu sortir d’une boucle while ? »\nTu te réveilles devant ton ordi, 35 onglets ouverts, Python en tête...\n"
            return render_template("fin.html", nom=nom, texte=texte, image="fin puit.png")
        else:
            texte = "Tu fuis le puits... mais la forêt te rattrape. Une dernière pensée : Il faudrait peut-etre plus que 24h en fin de compte..."
        return render_template("fin.html", nom=nom, texte=texte, image="fui puits.png")

    elif etape == "droite":
        if choix == "o":
            texte = "Dans la cabane, un vieux livre : « Maîtriser Python en 24h ». Les pages sont blanches. Une seule phrase au fond : « Spoiler : il t’en faudra plus. »"
            return render_template("fin.html", nom=nom, texte=texte, image="maitriser python.png")
        else:
            texte = "Tu restes dehors. Ton téléphone vibre. Une notif LinkedIn : « J’ai appris Python en 24h, je code l’avenir 🔥 »\nTu soupires, puis relances ton éditeur."
        return render_template("fin.html", nom=nom, texte=texte,  image="fin cabane éditeur.png")

    return render_template("fin.html", nom=nom, texte="Une erreur narrative est survenue. Peut-être un bug...")

if __name__ == "__main__":
    app.run(debug=True)
