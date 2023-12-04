## Projeto final - Ada & RD

Neste Notebook executamos as análises do projeto final da trilha de Dados da Ada junto com a RD. Nosso grupo (G3) e é composto por:
* Anthony Zaneta Mattos de Avila
* Thaís De Souza Marins
* Luiz Gustavo Nogueira Silva
* Gabriel Voltani Vatanabe
* Jonas Henrique Arjona Gonçalves Vieira

### Introdução
Este é um projeto de análise de dados com técnicas de aprendizado de máquina proposto como trabalho final da trilha de Dados. Nele usamos uma base de dados de Marketing que contém informações sobre cliques e não-cliques em anúncios, bem como vários outras informações demográficas. O objetivo é um modelo preditivo capaz de melhorar o disparo de anúncios, apresentando anúncios exatamente para os possíveis compradores.

### Pergunta de negócio e contexto
Nossa empresa foi contratada para prestar consultoria para uma outra empresa de soluções Tech para negócios como:

* Produção de websites;
* Consultoria para produção de *softwares*;
* Consultoria para produção de conteúdo;
* Etc.

O principal objetivo da contratante é otimizar o disparo de anúncios ao aumentar a taxa de acerto dos cliques. Isto é, aumentar a conversão dos anúncios, reduzindo a quantidade de anúncios mostrados para usuários que não clicariam.

O processo atualmente não é feito usando dados, o que produz prejuízos ao gerar despesas que não são convertidas em receita.
Os dados que a empresa contratante nos oferecem advém do seu Google Analytics para uma campanha de disparo feita anteriormente. Neles temos:

* Dados demográficos dos usuários (país, cidade, sexo, idade);
* Informações do perfil de uso dos usuários (tempo de uso da internet e acesso ao site);
* Informações relacionadas ao anúncio (título, data da visualização e se foi clicado ou não).

Há um viés na base já que ele advém de uma campanha anterior de disparo. Isso significa que nossos usuários já podem ter sido considerados possíveis compradores segundo outras perspectivas que não a de dados.
Dado que a empresa vende produtos e que há na plataforma desta um impedimento para o cadastro de usuários menores que 18 anos, consideramos essa informação na hora de filtrar nossos dados.
As variáveis presentes são:

> *Variáveis quantitativas*
>
> `Daily Time Spent on Site`, tempo diário passado no site em minutos
>
> `Age`, idade em anos inteiros 
>
> `Daily Internet Usage`, uso diário de internet em minutos
>
> `Timestamp`, data e hora da visualização do anúncio
>
> *Variáveis qualitativas*
>
> `Ad Topic Line`, texto-título do anúncio 
>
> `City`, cidade do usuário
>
> `Male`, se o usuário é homem (1) ou não (0)
>
> `Country`, país do usuário
>
> `Clicked on Ad`, se o usuário clicou (1) ou não (0) no anúncio

## Parte 1 - EDA e tratamento de dados

Executamos o tratamento da base, procurando e removendo dados nulos e usuários menores de 18 anos (dada nossa regra de negócio).

Além disso, também estudamos quais variáveis são relevantes para nossa análise, seja porque são correlacionadas com nosso alvo (o clicar no anúncio), seja porque apresentam comportamentos diferentes para cada valor (como qualitativas). 

### A base

Nossa base consiste de 101.450 entradas sem nulos, mas com alguns valores negativos que não fazem sentido: renda, tempo e idade. Juntas essas entradas totalizam 6772 observações, cerca de 6,68% da base original. Optamos por removê-las já que não sabemos qual o tipo de erro causou elas.

Além disso, como parte da nossa regra de negócio, os usuários deveriam ter mais que 18 anos para adquirir um produto que a empresa vende. Logo, filtramos-os, reduzindo em 12.768 entradas a nossa base (13,49%).

O corte de aproximadamente 20% das entradas é considerável. Mas tendo em mente que estes seriam erros na base ou usuários que mesmo clicando no anúncio não comprariam por inviabilidade dada a regra de negócio do site, mantê-los poderia influenciar nossos resultados. Nos sobraram 81.910 entradas.



