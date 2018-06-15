#Utilizar o pandas
# Utilizar nu_inscricao para pegar o numero de inscrição
# Utilizar nu_idade para pegar a idade 
# Utilizar nu_nota_cn nota de ciencias da natureza
# Utilizar nu_nota_ch nota de ciencias humanas
# Utilizar nu_nota_lc nota de linguagens e codigos
# Utilizar nu_nota_mt nota de matematica
# Utilizar nu_nota_redacao nota da redação
# precisa fazer o calculo ((nu_nota_mt x 3)+(nu_nota_cn x 2)+(nu_nota_lc x 1.5)+(nu_nota_ch)+(nu_nota_redacao x 3))/5 
#DROP NaN para derrubar quem não foi nas provas
#FALTA SORT


import pandas as pd
import csv
dataset = pd.read_csv('C:\\GitHub\\TrabalhoFinalPython\\train.csv', sep=',')
#print(dataset.head())
#print(dataset['NU_IDADE'])

data = dataset.dropna(subset=['NU_NOTA_REDACAO','NU_NOTA_MT','NU_NOTA_LC','NU_NOTA_CH','NU_NOTA_CN'])

final = (data['NU_NOTA_REDACAO']*3+data['NU_NOTA_MT']*3+data['NU_NOTA_CN']*2+data['NU_NOTA_LC']*1.5+data['NU_NOTA_CH'])/5

print(final)
#print(data[['NU_INSCRICAO', 'NU_IDADE','NU_NOTA_REDACAO','NU_NOTA_MT','NU_NOTA_LC','NU_NOTA_CH','NU_NOTA_CN']])