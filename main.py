import pandas as pd

# Remplacez 'chemin/vers/le/fichier.xlsx' par le chemin réel du fichier Excel
file_path = 'Online Retail.xlsx'
df = pd.read_excel(file_path)

print(df.head())  # Affiche les premières lignes pour vérification

# Vérification des valeurs manquantes
missing_values = df.isnull().sum()
#print(missing_values)

# Suppression des lignes où la colonne spécifique a des valeurs manquantes
# Remplacez 'nom_colonne' par le nom réel de la colonne
df_clean = df.dropna(subset=['CustomerID'])

# Affichage des premières lignes du DataFrame nettoyé
print(df_clean.head())

# Vérification des valeurs manquantes
missing_values_after_cleaning = df_clean.isnull().sum()
print(missing_values_after_cleaning)
