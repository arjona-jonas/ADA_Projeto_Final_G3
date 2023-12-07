#bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#abrindo base
df = pd.read_csv('../../data/01-intro.csv',index_col=0)
print(df.shape)

# funcao auxiliar para obter limites
def get_limits(data_variable):
    q1=data_variable.quantile(0.25)
    q3=data_variable.quantile(0.75)
    iqr=q3-q1
    lim_sup=q3+1.5*iqr
    lim_inf=q1-1.5*iqr
    return (lim_inf,lim_sup)

# funcao auxiliar de contar outliers
def count_outliers(df_coluna):
    li,ls = get_limits(df_coluna)
    results = [((df_coluna<li) | (df_coluna>ls)).sum(), #outliers
               ((df_coluna>li) & (df_coluna<ls)).sum(), #normais
               len(df_coluna)] #total
    return results

#contando outliers
results = {}
for var_num in ['Daily Time Spent on Site','Age','Area Income','Daily Internet Usage']:
    results[var_num] = count_outliers(df[var_num])

print(pd.DataFrame(results,index=['Outlier','Normal','Total']))

#distribuicao das vars de tempo
print(df[['Daily Time Spent on Site','Daily Internet Usage']].describe())

#histogramas dos tempos
fig, ax = plt.subplots (2,1,figsize=(10,8))

sns.histplot(df,
             x='Daily Time Spent on Site',
             kde=True,edgecolor = 'white',ax=ax[0])

ax[0].set_title('Tempo diário no site\n(minutos)')
ax[0].set_ylabel('Número de observações',size=13)
ax[0].set_xlabel('')

sns.histplot(df,
             x='Daily Internet Usage',
             kde=True,edgecolor = 'white',
             ax=ax[1])
ax[1].set_title('Tempo diário na internet\n(minutos)')
ax[1].set_ylabel('Número de observações',size=13)
ax[1].set_xlabel('')

fig.tight_layout(pad=2)
fig.figure.savefig('../../outputs/tempo_site_internet.png',dpi=600)


#distribuicao de age
print(df['Age'].describe())

#histograma de age
fig,ax=plt.subplots(figsize=(15,6))
sns.histplot(data=df,
            x='Age',bins=np.linspace(0,120,30),
            kde=True,
            edgecolor = 'white')

plt.xlabel('Idade',size=13)
plt.ylabel('Número de observações',size=13)
plt.title('Número de observações por idade',size=15)

fig.figure.savefig('../../outputs/idade.png',dpi=600)


#distribuicao de area income
print(df['Area Income'].describe())

#histograma de area income
fig,ax=plt.subplots(figsize=(15,6))

sns.histplot(df['Area Income'],
             kde=True,
             edgecolor = 'white',
             bins = np.linspace(0,140000,40))

plt.xlabel('Renda da região (dólares por ano)',size=13)
plt.ylabel('Número de observações',size=13)
plt.title('Número de observações por renda da região (dólares por ano)',size=15)

fig.figure.savefig('../../outputs/area-income.png',dpi=600)


#distribuicao de ad topic line, city e country
print(df.loc[:,['Ad Topic Line','City','Country']].describe())

#abrindo arquivo com continentes
continents = pd.read_csv('../../data/continents.csv')

#uniao dos arquivos
df = df.merge(continents,left_on='Country',right_on='Country',how='inner')

#grafico de barras dos continentes
fig,ax=plt.subplots(figsize=(15,6))

sns.barplot(df['Continent'].value_counts(),orient='h')

plt.xlabel('Continent',size=13)
plt.ylabel('Número de observações',size=13)
plt.title('Número de observações por continente',size=15)

fig.figure.savefig('../../outputs/continents.png',dpi=600)


#criando var de tamanho do titulo
df['Topic_len'] = df['Ad Topic Line'].str.len()

#histograma tamanho do titulo e situacao do clique
bins = np.linspace(10,60,num=20)

fig,ax=plt.subplots(figsize=(7,7))

sns.histplot(df.query('`Clicked on Ad`==1'),
             x='Topic_len',
             label='Clicou',
             kde=True,
             bins=bins,alpha=0.4)

sns.histplot(df.query('`Clicked on Ad`==0'),
             x='Topic_len',
             label='Não clicou',
             kde=True,
             bins=bins,alpha=0.7)

plt.xlabel('Tamanho do título',size=13)
plt.ylabel('Número de observações',size=13)
plt.title('Tamanho dos títulos dos anúncios',size=15)
plt.legend(title='Clicou no anúncio?')

fig.figure.savefig('../../outputs/clique_topic_len.png',dpi=600)


#distribuicao situacao do clique
fig,ax = plt.subplots(figsize = (6,6))

sns.countplot(df,
              x='Clicked on Ad',
              hue='Clicked on Ad',
              palette=['#ff7f0e','#1f77b4'],stat='percent')

plt.xlabel('Clicou no anúncio?',size=13)
plt.ylabel('Propoção',size=13)
plt.xticks(ticks=[0,1],labels=['Não clicou','Clicou'])
plt.legend('').remove()

plt.annotate('37.88%',xy=(-0.1,38.88)) #clicou
plt.annotate('62.11%',xy=(0.9,63)) #n_clicou

plt.title('Distribuição da situação de cliques',size=15)

fig.figure.savefig('../../outputs/clique.png',dpi=600)

#distribuicao de genero
df['Male'].value_counts(normalize=True)

#situacao da base
print(df.shape)

#exportando csv com continents
df.to_csv('../../data/02-eda.csv')