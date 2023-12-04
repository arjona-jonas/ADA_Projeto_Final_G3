#bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

#abrindo base
df = pd.read_csv('../../data/02-eda.csv',index_col=0)

#correlacoes
corr_matrix = df.corr(numeric_only=True)

#heatmap das correlacoes
fig,ax = plt.subplots(figsize = (10,10))

sns.heatmap(corr_matrix, annot=True, cmap='BuPu', annot_kws={"fontsize":9})
plt.title('Matriz de Correlação',size=15)
fig.tight_layout(pad=2)
fig.savefig('../../outputs/heatmap.png',dpi=600)


#histograma clique e idade
bins = np.linspace(0,90,num=30)

fig,ax=plt.subplots(figsize=(15,6))

sns.histplot(df.query('`Clicked on Ad`==1'),
             x='Age',
             bins=bins,kde=True,alpha=0.4,label='Clicou')

sns.histplot(df.query('`Clicked on Ad`==0'),
             x='Age',
             bins=bins,kde=True,alpha=0.7,label='Não clicou')

plt.xlabel('Idade',size=13)
plt.ylabel('Número de observações',size=13)
plt.title('Situação do clique por idade',size=15)
plt.legend(loc=1,title='Situação do clique')

fig.figure.savefig('../../outputs/corr_clique_idade.png',dpi=600)

#teste de hipotese entre diferentes medias de idade
age_wide=pd.DataFrame({
    'clicou':df.loc[df['Clicked on Ad']==1,'Age'],
    'n_clicou':df.loc[df['Clicked on Ad']==0,'Age']
})

print('\n',ttest_ind(age_wide['clicou'],age_wide['n_clicou'],nan_policy='omit'))
print('p-valor menor que zero, negamos H0, as duas médias são diferentes')


#histograma clique e temp no site/tempo na internet
fig,ax = plt.subplots(2,1,figsize=(13,8))

sns.histplot(df,
             x='Daily Internet Usage',
             hue='Clicked on Ad',
             ax=ax[0],
             palette=['#ff7f0e','#1f77b4'])

sns.histplot(df,
             x='Daily Time Spent on Site',
             hue='Clicked on Ad',
             ax=ax[1],palette=['#ff7f0e','#1f77b4'])


ax[0].set_title('Uso diário de internet',size=15)
ax[0].set_ylabel('Número de observações',size=13)
ax[0].set_xlabel('Minutos',size=13)
ax[0].legend(title = 'Situação do clique',
             labels = ['Clicou','Não clicou'])

ax[1].set_title('Tempo diário no Site',size=15)
ax[1].set_ylabel('Número de observações',size=13)
ax[1].set_xlabel('Minutos',size=13)
ax[1].legend(title = 'Situação do clique',
             labels = ['Clicou','Não clicou'])

fig.tight_layout(pad=2)
fig.figure.savefig('../../outputs/corr_clique_tempo.png',dpi=600)


#teste de hipotese entre diferentes medias de uso da internet
internet_wide=pd.DataFrame({
    'clicou':df.loc[df['Clicked on Ad']==1,'Daily Internet Usage'],
    'n_clicou':df.loc[df['Clicked on Ad']==0,'Daily Internet Usage']
})

print('\n',ttest_ind(internet_wide['clicou'],internet_wide['n_clicou'],nan_policy='omit'))
print('p-valor menor que zero, negamos H0, as duas médias são diferentes')

#teste de hipotese entre diferentes medias de acesso do site
site_wide=pd.DataFrame({
    'clicou':df.loc[df['Clicked on Ad']==1,'Daily Time Spent on Site'],
    'n_clicou':df.loc[df['Clicked on Ad']==0,'Daily Time Spent on Site']
})

print('\n',ttest_ind(internet_wide['clicou'],internet_wide['n_clicou'],nan_policy='omit'))
print('p-valor menor que zero, negamos H0, as duas médias são diferentes')


#histograma clique e renda
bins = np.linspace(0,180000,50)

fig,ax=plt.subplots(figsize=(15,6))

sns.histplot(df.query('`Clicked on Ad`==1'),
             x='Area Income',
             bins=bins,kde=True,alpha=0.4,label='Clicou',color='#1f77b4')

sns.histplot(df.query('`Clicked on Ad`==0'),
             x='Area Income',
             bins=bins,kde=True,alpha=0.7,label='Não clicou',color='#ff7f0e')

plt.xlabel('Renda da região (em US$)',size=13)
plt.ylabel('Número de observações',size=13)
plt.title('Situação do clique por renda da região (em US$)',size=15)
plt.legend(loc=1,title='Situação do clique')

fig.figure.savefig('../../outputs/corr_clique_income.png',dpi=600)


income_wide=pd.DataFrame({
    'clicou':df.loc[df['Clicked on Ad']==1,'Area Income'],
    'n_clicou':df.loc[df['Clicked on Ad']==0,'Area Income']
})

#teste de hipotese entre diferentes medias de acesso do site
print('\n',ttest_ind(income_wide['clicou'],income_wide['n_clicou'],nan_policy='omit'))
print('p-valor menor que zero, negamos H0, as duas médias são diferentes')


#gráficos de barras entre clique e continente
fig,ax=plt.subplots(figsize=(15,6))

sns.countplot(df,
              x='Continent',
              hue='Clicked on Ad',palette=['#ff7f0e','#1f77b4'])

plt.title('Situação de cliques por continente',size=15)
plt.xlabel('Continentes',size=13)
plt.xticks(ticks=df['Continent'].unique(),
           labels=['Europa','América do Norte','Oceania','Ásia','América do Sul','África'],
           size=11)
plt.ylabel('Número de observações',size=13)
plt.legend(title='Situação do clique',
           labels=['Não clicou','Clicou'])

fig.figure.savefig('../../outputs/corr_clique_continent.png',dpi=600)
