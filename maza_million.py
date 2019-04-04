import pandas as pd

df = pd.read_csv("Maza2019.csv", encoding="utf-8")

naam_lijst = [f'row_{naam}' for naam in range(1, 9)]

row1 = df.loc[0:124999]

print(len(row1))

