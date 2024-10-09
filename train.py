import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Charger les données depuis le fichier CSV
data = pd.read_csv('data.csv')

# Transformer les données en format numérique
data['Nodule'] = data['Nodule'].apply(lambda x: 1 if x == 'oui' else 0)
data['Douleur'] = data['Douleur'].apply(lambda x: 1 if x == 'oui' else 0)
data['Changement de forme'] = data['Changement_de_forme'].apply(lambda x: 1 if x == 'oui' else 0)
data['Écoulement'] = data['Écoulement'].apply(lambda x: 1 if x == 'oui' else 0)
data['Rougeur'] = data['Rougeur'].apply(lambda x: 1 if x == 'oui' else 0)
data['Ganglions'] = data['Ganglions'].apply(lambda x: 1 if x == 'oui' else 0)
data['Antécédents familiaux'] = data['Antécédents_familiaux'].apply(lambda x: 1 if x == 'oui' else 0)
data['Diagnostic'] = data['Diagnostic'].apply(lambda x: 1 if x == 'Positif' else 0)

# Séparer les caractéristiques (X) et l'étiquette (y)
X = data[['Nodule', 'Douleur', 'Changement de forme', 'Écoulement', 'Rougeur', 'Ganglions', 'Antécédents familiaux']]
y = data['Diagnostic']

# Diviser les données en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le modèle d'arbre de décision
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Prédire sur l'ensemble de test
y_pred = model.predict(X_test)

# Afficher la précision
print(f"Précision du modèle: {accuracy_score(y_test, y_pred)}")

# Sauvegarder le modèle
joblib.dump(model, 'decision_tree_model.pkl')
