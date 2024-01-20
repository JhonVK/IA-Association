import pandas as pd
from apyori import apriori

base_mercado1= pd.read_csv(r'C:\Users\joaov\OneDrive\Área de Trabalho\python\CSV\mercado.csv', header=None)

print(base_mercado1)
    #Transformando em uma lista
transacoes=[]

for i in range(len(base_mercado1)):
    #print(i)
    #print(base_mercado1.values[i, 0])
    transacoes.append([str(base_mercado1.values[i, j]) for j in range (4)])
    
print(transacoes)
print(type(transacoes))

    #Gerar regras
regras = apriori(transacoes, min_support= 0.3, min_confidence=0.8, min_lift=2)

    #Transformar em lista para melhor visualização
resultados = list(regras) 
print(resultados)
print(len(resultados))
print()
print(resultados[2])
r=resultados[2][2] ##somente as regras

print(r)

print(r[2][0])#se
print(r[2][1])#entao
print(r[2][2])#confiança
print(r[2][3])#lift


    #Codificação para visualizar melhor os resultados

A = []
B = []
suporte = []
confianca = []
lift = []

for resultado in resultados:
  s = resultado[1]
  result_rules = resultado[2]
  for result_rule in result_rules:
    a = list(result_rule[0])
    b = list(result_rule[1])
    c = result_rule[2]
    l = result_rule[3]
    A.append(a)
    B.append(b)
    suporte.append(s)
    confianca.append(c)
    lift.append(l)
                

print(A)
print(B)
print(suporte)
print(confianca)
print(lift)

rules_data= pd.DataFrame({'A': A, 'B': B, 'suporte': suporte, 'confiança':confianca, 'lift':lift })

print(rules_data.sort_values(by= 'lift', ascending=False))