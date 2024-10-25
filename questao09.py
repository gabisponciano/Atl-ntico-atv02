import pandas as pd

df = pd.read_csv("gym_members_exercise_tracking.csv")
filtro = df.loc[df['Age'] < 20 , 'Workout_Frequency (days/week)']
print(filtro)