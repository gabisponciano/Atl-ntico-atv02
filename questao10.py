import pandas as pd

df = pd.read_csv("gym_members_exercise_tracking.csv")

##Aqui verifica se tem valores ausentes
print(df.isna().sum())
 ##Nesse caso não possui valores ausente
 ## Para resolver os valores ausentes podemos:
 ##Retirar a coluna e as linha como abaixo:
df_na = df.dropna()
df_na_colunas = df.dropna(axis=1)

##Tentas preencher os valores ausentes com alguns metodos
## como com preencher com um valor especifico (0), com média, mediana ou moda. Pode-se até mesmo fazer a interpolação.


