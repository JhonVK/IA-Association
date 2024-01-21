import pandas as pd

base_mercado1= pd.read_csv(r'C:\Users\joaov\OneDrive\Área de Trabalho\python\CSV\mercado.csv', header=None)
#eclat n gera regras, apenas os itens frequentes...
from pyECLAT import ECLAT

eclat= ECLAT(data= base_mercado1)

print(eclat.df_bin)
print(eclat.uniq_)

indices, suporte= eclat.fit(min_support=0.3, min_combination=1, max_combination=3)

print(indices)
print()
print(suporte)