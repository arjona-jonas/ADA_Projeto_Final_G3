# Projeto final (G3)
Este repositório contém a entrega final da trilha de Dados da Ada junto com a RaiaDrogasil. Nele simulamos uma entrega executiva de um projeto. Este é o grupo 3, composto por:
* Anthony Zaneta Mattos de Avila
* Thaís De Souza Marins
* Luiz Gustavo Nogueira Silva
* Gabriel Voltani Vatanabe
* Jonas Henrique Arjona Gonçalves Vieira

# Como utilizar os arquivos
Cada paste dentro de `main` contém uma etapa do processo de análise, um script em .py e um arquivo MD descrevendo melhor aquela etapa. Os scripts dessa análise em específico são independentes e podem ser rodados na ordem que for desejado. Os dados usados e produzidos nas análises ficam na pasta `data` e os gráficos na pasta `outputs`.

Para rodar os mesmos scripts para dados diferentes é preciso que o arquivo seja renomeado como `data_raw.csv` e colocado dentro da pasta `data`. Ele precisa possuir as seguintes colunas e formatos:

|Coluna|Formato|
|---|---|
|`Daily Time Spent on Site`|float|
|`Age`|int|
|`Daily Internet Usage`|float|
|`Timestamp`|indiferente já que não entra na análise|
|`Area Income`|object|
|`City`|object|
|`Male`|int|
|`Country`|object|
|`Clicked on Ad`|int|

Feito isso podemos rodar todos os scripts na sequência proposta no esquema de pastas: começamos pela introdução, EDA, correlações, modelo e conclusão. Todos os gráficos gerados estarão na pasta `outputs`.

Além dos arquivos .py, dentro de `main` temos a pasta `notebook` que contém a análise inteira em formato Jupyter Notebook, caso seja preferível visualizar ela dessa forma.

# Bibliotecas necessárias
Utilizamos bibliotecas de diversas finalidades. Abaixo estão elas:

``` python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
from sklearn.model_selection import train_test_split,cross_validate,StratifiedKFold,RandomizedSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler,OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report,f1_score,accuracy_score,precision_score,recall_score,roc_auc_score
```

No arquivo `requirements.txt` também temos a relação as bibliotecas utilizadas, já num formato útil ao `pip install`.

# O problema de negócios

# Passo a passo sumarizado da solução

# Considerações finais

