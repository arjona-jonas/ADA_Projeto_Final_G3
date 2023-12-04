#bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#bibliotecas especificas de machine learning
from sklearn.model_selection import train_test_split,cross_validate,StratifiedKFold,RandomizedSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler,OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report,f1_score,accuracy_score,precision_score,recall_score,roc_auc_score

#abrindo base
df = pd.read_csv('../../data/02-eda.csv',index_col=0)

#fazendo a separação entre variaveis de features e o target
X = df.drop(columns=['Ad Topic Line','City','Country','Timestamp','Clicked on Ad'])
y = df['Clicked on Ad']

#separando os dados entre treino e teste (mantendo a proporcao do target)
X_train,X_test,y_train,y_test = train_test_split(X,y,
                                                 test_size=0.2,
                                                 random_state=42,stratify=y)

### PIPELINE DE TRATAMENTO
#pipeline para variaveis numericas
pipe_num = Pipeline([
    ('imputer_num',SimpleImputer(strategy='mean')),
    ('scaler_num',MinMaxScaler())
])

#pipeline para male
pipe_cat_male = Pipeline([
    ('imputer_cat_male',SimpleImputer(strategy='most_frequent'))
])

#pipeline para continent
pipe_cat_cont = Pipeline([
    ('imputer_cat_cont',SimpleImputer(strategy='most_frequent')),
    ('one_hot',OneHotEncoder())
])

#relacao das variaveis numericas
colunas_num = ['Daily Time Spent on Site','Area Income','Daily Internet Usage','Age','Topic_len']

#pipeline unindo tudo
preprocessing = ColumnTransformer([
    ('transf_num',pipe_num,colunas_num),
    ('transf_cat_male',pipe_cat_male,['Male']),
    ('transf_cat_cont',pipe_cat_cont,['Continent'])],
    verbose_feature_names_out=False)

#como ficam as variaveis apos os tratamentos?
print(pd.DataFrame(preprocessing.fit_transform(X_train),
             columns=preprocessing.get_feature_names_out()))


#instanciando validacao cruzada
skfolds = StratifiedKFold(n_splits=5,shuffle=True,random_state=42)

#pipeline com preprocess e modelo
pipe_final = Pipeline([
    ('preprocess',preprocessing),
    ('tree',DecisionTreeClassifier(max_depth=7,random_state=42))
])

#primeira abordagem
metricas = ['f1','accuracy','precision','recall','roc_auc']

results = cross_validate(pipe_final,
                         X_train,y_train,
                         cv=skfolds,
                         scoring=metricas,
                         return_train_score=True,
                         return_estimator=True)

#metricas iniciais
print('F1 de treino:', results['train_f1'].mean())
print('F1 de validacao:', results['test_f1'].mean())

print('\nAccuracy de treino:', results['train_accuracy'].mean())
print('Accuracy de validacao:', results['test_accuracy'].mean())

print('\nPrecision de treino:', results['train_precision'].mean())
print('Precision de validacao:', results['test_precision'].mean())

print('\nRecall de treino:', results['train_recall'].mean())
print('Recall de validacao:', results['test_recall'].mean())

print('\nRoc_auc de treino:', results['train_roc_auc'].mean())
print('Roc_auc de validacao:', results['test_roc_auc'].mean())

#arvore do modelo inicial
fig, ax = plt.subplots(figsize=(20,20))
plot_tree(results['estimator'][1][1])
fig.savefig('../../outputs/arvore_original.png',dpi=600)


#OTIMIZAÇÃO
#hiperparametros a serem testados
param_distributions = {
    'tree__criterion': ['gini', 'entropy'],
    'tree__splitter': ['best', 'random'],
    'tree__max_depth': list(range(2, 11)),
    'tree__min_samples_split': list(range(2, 11)),
    'tree__min_samples_leaf': list(range(1, 11)),
}

#codigo do otimizador
rand_search = RandomizedSearchCV(pipe_final,
                                 param_distributions,
                                 n_iter=30,
                                 cv=skfolds,
                                 scoring='precision',return_train_score=True,
                                 random_state=42)

#start no processo
rand_search.fit(X_train,y_train)

#quais foram os melhores resultados?
print('\nmelhores parametros:',rand_search.best_params_)
print('melhor score de precision:',rand_search.best_score_)

#como as metricas se comportaram nos testes?
print('\nprecision dos treinos: ',sorted(rand_search.cv_results_['mean_train_score']))
print('\nprecision das validações: ',sorted(rand_search.cv_results_['mean_test_score']))


#rodando modelo otimizado nos dados de treino
y_train_pred = rand_search.predict(X_train)

ConfusionMatrixDisplay.from_predictions(y_train,y_train_pred)
plt.title('Matriz de confusão para dados de treino')
plt.xlabel('Valores preditos')
plt.ylabel('Valores reais')
plt.savefig('../../outputs/matrix_modelo_treino.png',dpi=600)

#metricas no treino
print('\nf1 de treino: ',f1_score(y_train,y_train_pred))
print('accuracy de treino: ',accuracy_score(y_train,y_train_pred))
print('precision de treino: ',precision_score(y_train,y_train_pred))
print('recall de treino: ',recall_score(y_train,y_train_pred))
print('roc_auc de treino: ',roc_auc_score(y_train,y_train_pred))

#rodando modelo otimizado nos dados de teste
y_test_pred = rand_search.predict(X_test)

ConfusionMatrixDisplay.from_predictions(y_test,y_test_pred)
plt.title('Matriz de confusão para dados de teste')
plt.xlabel('Valores preditos')
plt.ylabel('Valores reais')
plt.savefig('../../outputs/matrix_modelo_teste.png',dpi=600)

#metricas no teste
print('\nf1 de teste: ',f1_score(y_test,y_test_pred))
print('accuracy de teste: ',accuracy_score(y_test,y_test_pred))
print('precision de teste: ',precision_score(y_test,y_test_pred))
print('recall de teste: ',recall_score(y_test,y_test_pred))
print('roc_auc de teste: ',roc_auc_score(y_test,y_test_pred))