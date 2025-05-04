🕹️ Jeu d’aventure Python (Flask + HTML/CSS)

Bienvenue dans un jeu narratif en ligne, développé avec Python et Flask.
Une mini-aventure textuelle et visuelle, à mi-chemin entre mystère, humour… et autodérision sur l’apprentissage du code.
🚀 Aperçu

    "Tu te réveilles dans une vallée brumeuse...
    Un puits, une cabane, un vieux livre ‘Apprends Python en 24h’...
    Et LinkedIn qui clignote au loin. Que vas-tu faire ?"

📁 Structure du projet

mon_jeu_flask/
├── app.py                  # Logique du jeu
├── templates/              # Pages HTML
│   ├── accueil.html
│   ├── jeu.html
│   └── fin.html
├── static/
│   ├── style.css           # Design CSS
│   └── images/             # Illustrations pixel art

🧰 Prérequis

    Python 3.8+

    Flask

📦 Installation

# Clone ou télécharge le repo
cd mon_jeu_flask

# (Optionnel) Crée un environnement virtuel
python -m venv env
env\Scripts\activate        # Windows
source env/bin/activate     # macOS/Linux

# Installe Flask
pip install flask

▶️ Lancer le jeu

python app.py

Puis ouvre http://127.0.0.1:5000 dans ton navigateur.
🎨 Crédits

    Histoire & code : Ysshar
    Illustrations : Générées en pixel art avec assistance IA

    Framework : Flask

🧠 Message du jeu

    Apprendre Python ne prend pas 24h.
    Mais ça peut commencer avec une aventure comme celle-ci.
