import pandas as pd

df = pd.read_csv("data.csv")

pt = pd.pivot_table(df, index=['continent', 'year'], values=['lifeExp', 'country'],
                    aggfunc={'lifeExp': 'mean', 'country': 'count'}).reset_index()
pt.rename(columns={'country': 'countries', 'lifeExp': 'avg_LifeExp'}, inplace=True)

print(pt)
