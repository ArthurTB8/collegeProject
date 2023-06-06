import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('dataset.csv')


paises_interesse = ['China', 'United States', 'Indonesia', 'Pakistan', 'Nigeria', 'Brazil']


dados_filtrados = dados[dados['Name'].isin(paises_interesse)]


populacao_total_2022 = dados_filtrados.loc[dados_filtrados['Name'].isin(paises_interesse), '2022'].sum()


dados_filtrados['Porcentagem da População'] = dados_filtrados['2022'] / populacao_total_2022 * 100


plt.figure(figsize=(8, 6))
plt.pie(dados_filtrados['Porcentagem da População'], labels=dados_filtrados['Name'], autopct='%.2f%%')
plt.title('Porcentagem da População por País (2022)')

plt.show()