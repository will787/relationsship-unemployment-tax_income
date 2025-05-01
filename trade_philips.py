# %%
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
import statsmodels.api as sm

# getting variables

import get_unemployment as un 
import selic as tax

tax_selic = tax.df_selic
unemployment  = un.un_df

#print(f"Date minima: {tradeoff['date'].min()}")
#print(f"Date máxima: {tradeoff['date'].max()}")


tradeoff = pd.merge(tax_selic, unemployment, on='date')
tradeoff = tradeoff[['date', 'month_y_x','selic', 'un_var_%']]
tradeoff = tradeoff.rename(columns={'month_y_x': 'month_y'})
tradeoff
# %% residuals plots

sns.set_theme(style='whitegrid')
plt.figure(figsize = (15, 10))
sns.residplot(
    data=tradeoff,
    y="selic",
    x="un_var_%",
    lowess=True, 
    color="green",
)
plt.xlabel("Taxa de Juros (%)")
plt.ylabel("Residuos do Desemprego")
plt.title("Reg Desemprego & Taxa de Juros")
plt.show()

# %% tradeoff of unemployment vs income tax

# regression to understand more

X = sm.add_constant(tradeoff['un_var_%'])
y = tradeoff['selic']
model = sm.OLS(y, X).fit()
residuos = model.resid

#creating map of color (the more recent, more dark)

norm = plt.Normalize(tradeoff['date'].min().toordinal(), tradeoff['date'].max().toordinal())
colors = plt.cm.Greens(norm(tradeoff['date'].apply(lambda d: d.toordinal())))

plt.figure(figsize=(15, 10))
plt.scatter(tradeoff['un_var_%'], residuos, c=colors, edgecolors='k')
plt.axhline(0, linestyle='--', color='gray')

plt.xlabel("Desemprego (%)")
plt.ylabel("Resíduos da Taxa de Juros")
plt.title("Resíduos da Regressão: Taxa de Juros ~ Desemprego")

sm_ = plt.cm.ScalarMappable(cmap='Greens', norm=norm)
sm_.set_array([])
cbar = plt.colorbar(sm_, orientation='vertical')
cbar.set_label('Data (mais claro = antigo, mais escuro = recente)')

plt.tight_layout()
plt.show()