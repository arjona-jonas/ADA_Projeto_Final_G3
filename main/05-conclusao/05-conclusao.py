#bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#relacao dos desempenhos
data = [['Clicou',50650,62.11,8769,86.56],
        ['Não Clicou',30892,37.88,1361,13.43],
        ['Total',81542,100,10130,100]]

resumo = pd.DataFrame(data,columns=['Situação','Disparo original','Disparo original (%)',
                      'Indicação do modelo','Indicação do modelo (%)'])

resumo = resumo.melt(id_vars='Situação',value_vars=['Disparo original','Disparo original (%)',
                      'Indicação do modelo','Indicação do modelo (%)'])

resumo_perc = resumo.query('Situação!="Total" & variable.isin(["Disparo original (%)","Indicação do modelo (%)"])')

#grafico de barras dos desempenhos
fig,ax = plt.subplots(figsize=(8,8))

sns.barplot(resumo_perc,
            x='variable',
            hue='Situação',
            y='value')

plt.annotate('62.11%',xy=(-0.30,63.11)) #clicou
plt.annotate('37.88%',xy=(0.10,38.88)) #n_clicou
plt.annotate('86.56%',xy=(0.70,87.56)) #clicou
plt.annotate('13.43%',xy=(1.10,14.43)) #n_clicou

plt.xlabel('')
plt.ylabel('Proporção',size=13)
plt.title('Taxa de acerto de cliques: disparo original e modelo proposto',size=15)

fig.figure.savefig('../../outputs/result_modelo.png',dpi=600)
