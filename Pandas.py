import pandas as pd

result = pd.read_csv("data.csv")

print(result[['year', 'continent']])
