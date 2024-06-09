import pandas as pd
import matplotlib.pyplot as plt

# Définir les données CSV
data = [
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [15,1,1,1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1],
    [0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,0,0,0,1,1,0,0,0,1,1]
]
df = pd.read_csv('resultats_comparaison.csv')
# Créer un DataFrame pandas
#df = pd.DataFrame(data)
print(df)
# Calculer la somme de chaque colonne
sums = df.sum()

# Définir les couleurs : rouge pour les valeurs < 10, bleu sinon
colors = ['red' if val < 10 else 'blue' for val in sums]

# Afficher les résultats sous forme d'histogramme
plt.figure(figsize=(10, 6))
sums.plot(kind='bar', color=colors)
plt.xlabel('questions')
plt.ylabel('nombre de reponse juste')
plt.title('fréquence des réponse par question')
# Sauvegarder l'histogramme en tant qu'image PNG
plt.savefig('fréquence des réponse par question.png')

plt.show()
