import pandas as pd

# Lire les fichiers CSV
# Lire les deux fichiers CSV
# Read the CSV files
df1 = pd.read_csv('file1.csv', header=None)
df2 = pd.read_csv('file2.csv', header=None)


# Vérifier que les deux DataFrames ont la même longueur
if len(df1) != len(df2):
    print("Les fichiers n'ont pas le même nombre de lignes.")
else:
    # Comparer les lignes et créer une liste des résultats
    comparaison = [(index, 0 if df1.iloc[index].equals(df2.iloc[index]) else 1) for index in df1.index]

    # Afficher les résultats
    for index, result in comparaison:
        print(index, result)