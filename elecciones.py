votosTotales = int (input())
candidatos = {}
while votosTotales > 0:
    candidato = input()
    if candidato in candidatos:
        candidatos[candidato] +=1
    else:
        candidatos[candidato] = 1
    votosTotales -=1
lista = []
for candidato,voto in candidatos.items():
    lista.append([voto, candidato]) 
valor = max(lista)
print (valor[1])
