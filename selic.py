# %% 
import numpy as np
import pandas as pd
from bcb import sgs
import matplotlib.pyplot as plt
import seaborn as sns

# %% busca a série da SELIC no SGS
df_selic = sgs.get({'selic': 432}, start='2017-01-01')
df_selic.reset_index(inplace=True)
df_selic = df_selic.rename(columns={'Date': 'date'})
df_selic['month_y'] = df_selic['date'].dt.strftime('%Y-%m')
df_selic['month_y'] = pd.to_datetime(df_selic['month_y'])
df_selic.dtypes
# %%  plot sem mex
plt.figure(figsize = (15, 10))
sns.histplot(data=df_selic, x='selic', kde=True, bins=10)
plt.title('Frequency of Selic')
plt.xlabel('Distribution')
plt.ylabel('Level of Tax (%%)')
plt.show()