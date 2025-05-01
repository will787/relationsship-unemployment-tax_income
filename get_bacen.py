# %%
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# %%
def get_bacen_data(serie, start='01/01/2000'):
    url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{serie}/dados?formato=json&dataInicial={start}'
    print(url)
    response = requests.get(url)
    if(response.status_code != 200):
        return print("Erro", response.status_code)
    data = response.json()
    df = pd.DataFrame(data)
    df['data'] = pd.to_datetime(df['data'], dayfirst=False)
    df['valor'] = df['valor'].astype(float)

    return df

ipca_df = get_bacen_data(433) # dados ipca


# %%
print(ipca_df.head())
