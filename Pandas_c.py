import pandas as pd
from matplotlib import pylab as plt

df = pd.read_csv("data.csv")

pt = pd.pivot_table(df, index=['continent', 'year'], values=['lifeExp', 'country'],
                    aggfunc={'lifeExp': 'mean', 'country': 'count'})
pt.rename(columns={'country': 'countries', 'lifeExp': 'avg_lifeExp'}, inplace=True)

print('Continents: ', pt.index.levels[0])
print('Years: ', pt.index.levels[1])

for continent in pt.index.levels[0]:
    print('Cycle: ', continent, pt.loc[continent]['avg_lifeExp'].values)

    plt.plot(pt.index.levels[1], pt.loc[continent]['avg_lifeExp'].values, label=continent)

plt.legend()
plt.show()
