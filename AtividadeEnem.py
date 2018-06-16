import pandas as pd
data = pd.read_csv('C:\\GitHub\\TrabalhoFinalPython\\train.csv', sep=',')
data = data.loc[:,['NU_INSCRICAO','NU_NOTA_REDACAO','NU_NOTA_MT','NU_NOTA_LC','NU_NOTA_CH','NU_NOTA_CN']]
data = data.dropna(subset=['NU_NOTA_REDACAO','NU_NOTA_MT','NU_NOTA_LC','NU_NOTA_CH','NU_NOTA_CN'])

final = (data['NU_NOTA_REDACAO']*3+data['NU_NOTA_MT']*3+data['NU_NOTA_CN']*2+data['NU_NOTA_LC']*1.5+data['NU_NOTA_CH'])/5
data['final'] = final
data = data.sort_values(by=['final'], ascending=False)
#print(final)
print("token : 1234")
print("email : placido_antonio@estudante.sc.senai.br")
print("answer :")
print(data.head(20))