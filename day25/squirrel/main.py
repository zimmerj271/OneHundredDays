import pandas as pd

df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_df = df.groupby('Primary Fur Color').agg({'Primary Fur Color': 'count'})
fur_df.columns = ['Count']
fur_df.index.names = ['Fur Color']
fur_df = fur_df.reset_index()
fur_df.to_csv('fur_color.csv', index=False)
# print(fur_df.reset_index())
