# %%
import ipeadatapy as ipea
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import pandas as pd

df_amostras = ipea.list_series()    

# %%

start_d = df_amostras[df_amostras['NAME'].str.contains('Desemprego', case=False)]
desocupacao = df_amostras[df_amostras['CODE'] == 'PNADC12_TDESOC12']
serie = desocupacao.iloc[0,0]
print(serie)

# %%

# importando os dados da serie
un_df = ipea.timeseries(serie)
un_df = un_df.rename(columns={'VALUE ((%))': 'un_var_%'})
un_df = un_df.rename(columns={'MONTH': 'month'})
un_df = un_df.rename(columns={'YEAR': 'year'})
un_df.reset_index(inplace=True)
un_df = un_df.rename(columns={'DATE': 'date'})
un_df = un_df.drop(columns={'DAY', 'CODE', 'RAW DATE'})

# transforming to month, section of datetime.
un_df['month_y'] = un_df['date'].dt.strftime('%Y-%m')
un_df['month_y'] = pd.to_datetime(un_df['month_y'], format='%Y-%m')
un_df = un_df[['date', 'month_y', 'un_var_%']]
un_df.head()
# %%
plt.figure(figsize = (15, 10))
sns.histplot(data=un_df, x='un_var_%', kde=True)
plt.title('Frequency of Unemployment Brazil')
plt.xlabel('Distribution')
plt.ylabel('Level (%%)')
plt.show()

# %% 
un_df['un_var_%'].describe()
un_df.dtypes