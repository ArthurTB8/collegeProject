import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')

paises = ['China', 'India', 'United States', 'Brazil']


for pais in paises:
    populacao = df.loc[df['Name'] == pais, ['2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970']]
    anos = populacao.columns.astype(int)
    plt.plot(anos, populacao.values.flatten(), label=pais)

plt.xlabel('Ano')
plt.ylabel('População')
plt.title('Evolução da População')


for pais in paises:
    populacao = df.loc[df['Name'] == pais, ['2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970']]
    anos = populacao.columns.astype(int)
    valores = populacao.values.flatten()
    for i in range(len(anos)):
        plt.annotate(str(int(valores[i])), (anos[i], valores[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.legend()
plt.show()
