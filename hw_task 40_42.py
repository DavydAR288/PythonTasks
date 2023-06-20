# Задача 40:

import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')
mean_price = df.loc[df['population']<=500, 'median_house_value'].mean()
print(mean_price)

# Задача 42:

import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')
min_pop = df['population'].min()
max_house = df.loc[df['population']==min_pop, 'households'].max()
print(max_house)