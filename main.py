import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('dados/dados_experimentos.zip', compression='zip')
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
Desafio 01: Investigar por que a classe tratamento é tão desbalanceada?
Desafio 02: Plotar as 5 últimas linhas da tabela
Desafio 03: Proporção das classes tratamento
Desafio 04: Quantas tipos de drogas foram investigados
Desafio 05: Procurar na documentação o método query(pandas)
Desafio 06: Renomear as colunas tirando o hífen
Desafio 07: Deixar os gráficos bonitões. (Matplotlib.pyplot)
Desafio 08: Resumo do que você aprendeu com os dados
'''