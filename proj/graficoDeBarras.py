import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('dataset.csv')


paises = ['China', 'India', 'United States', 'Brazil']
populacoes = dados.loc[dados['Name'].isin(paises), '2022']


fig, ax = plt.subplots()
indice = range(len(paises))

cores = ['b', 'g', 'r', 'y']  
barras = ax.bar(indice, populacoes, color=cores)


ax.set_xticks(indice)
ax.set_xticklabels(paises)


def autolabel(barras):
    for barra in barras:
        altura = barra.get_height()
        ax.annotate('{}'.format(altura),
                    xy=(barra.get_x() + barra.get_width() / 2, altura),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(barras)


ax.set_xlabel('Países')
ax.set_ylabel('População')
ax.set_title('Comparação de População (2022)')

plt.tight_layout()
plt.show()