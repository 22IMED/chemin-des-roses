# Chemin-des-Roses

À la fin de ce guide, vous pourrez tester le Chatbot et le Quizz sur votre ordinateur personnel.

## Étape 1 : Installation des dépendances
Pour lancer le Chatbot, installez les dépendances répertoriées dans le fichier `requirements.txt` :

```bash
pip install -r requirements.txt
```

## Étape 2 : Lancement de l'API
Lancez le serveur API (fichier `Server.py`) pour l'analyse des données et la prédiction, avec le point de terminaison suivant :
Exemple : `http://127.0.0.1:5000/predict`

Dans la ligne de commande, accédez au répertoire du projet :
```bash
cd chemin-des-roses
```

Pour démarrer l'API, exécutez la commande suivante :

```bash
python Server.py
```

## Étape 3 : Lancement du front-end
Lancez le serveur web local en exécutant la commande suivante :

```bash
python -m http.server 8000
```

## Étape 4 : Accéder au Chatbot et au Quizz

Pour ouvrir le Chatbot : `http://localhost:8000/Breast_cancer.html`

Pour lancer le Quizz : `http://localhost:8000/Quizz.html`





