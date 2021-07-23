import pandas as pd

result = pd.read_csv("data.csv")

new_result = result[(result["lifeExp"] > 58) & (result["gdpPercap"] > 100000)]
print(new_result.head(4))
