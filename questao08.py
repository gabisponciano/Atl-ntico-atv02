import pandas as pd
##Baixei uma base de dados da kaggle sobre o monitoramento de exercicio de membros da academia.
df = pd.read_csv("gym_members_exercise_tracking.csv")
print(df.head())
