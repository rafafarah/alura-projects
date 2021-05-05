import pandas as pd

'''
Aula 1
Desafio 01: Investigar por que a classe tratamento é tão desbalanceada?
Desafio 02: Plotar as 5 últimas linhas da tabela
Desafio 03: Proporção das classes tratamento
Desafio 04: Quantas tipos de drogas foram investigados
Desafio 05: Procurar na documentação o método query(pandas)
Desafio 06: Renomear as colunas tirando o hífen
Desafio 07: Deixar os gráficos bonitões. (Matplotlib.pyplot)
Desafio 08: Resumo do que você aprendeu com os dados
'''
data = pd.read_csv('dados/dados_experimentos.zip', compression='zip')
def test_filter():
    import matplotlib.pyplot as plt
    # print first rows, default 5
    print(data.head())

    # print last rows, default 5
    print(data.tail())

    # print #rows, #columns
    print(data.shape)

    # print unique values for each column
    print(data['tratamento'].unique())
    print(data['tempo'].unique())
    print(data['dose'].unique())
    print(data['droga'].unique())
    print(data['g-0'].unique(), end='\n\n')

    # frequency of each unique value
    print(data['tratamento'].value_counts())
    print(data['dose'].value_counts(), end='\n\n')

    # proportion
    print(data['tratamento'].value_counts(normalize=True))
    print(data['dose'].value_counts(normalize=True))

    # plot bar graph
    print(data['tempo'].value_counts().plot.bar())
    plt.show()

    filtered_data = data[data['g-0'] > 0]
    print(filtered_data.head())

'''
Aula 2
Desafio 01: Sort graph
    ax = sns.countplot(x = x,
                       data=data_compound,
                       # value_counts(ascending=True)
                       order = data_compound[x].value_counts().index)
Desafio 02: Change axis name
'''
def test_compound_graph():
    map = {'droga':'composto'}
    data.rename(columns=map, inplace=True)
    # get index of 5 most frequent compounds
    compound_ids = data['composto'].value_counts().index[:5]

    data_compound = data.query('composto in @compound_ids')

    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.set()
    plt.figure(figsize=(8,6))
    x = 'composto'
    ax = sns.countplot(x = x,
                       data=data_compound,
                       # value_counts(ascending=True)
                       order = data_compound[x].value_counts().index)
    ax.set_title('Top 5 Compounds')
    plt.show()

'''
Desafio 03: Plot graphs side by side
    fig, axes = plt.subplots(1, 2)
    data['g-0'].hist(bins=200, ax=axes[0])
    data['g-19'].hist(bins=200, ax=axes[1])
'''
def test_histogram():
    import matplotlib.pyplot as plt
    data['g-0'].hist(bins=200)
    data['g-19'].hist(bins=200)
    plt.show()


if __name__ == "__main__":
    test_histogram()