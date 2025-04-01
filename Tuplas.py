#Tuplas sao estruturas de dados imutavel e ordenada
#reforcando a ideia de imutavel, elas nao podem ser alteradas uma vez que criadas (diferente das listas), nao ha remocao, insercao...
#sao uteis para representar coordenadas, ou configuracoes

#Criacao e acesso
ponto = (1, 3)

print(ponto[0])
print(ponto[1])

#Metodos com tuplas
tupla = (1, 2, 3, 2, 4, 5, 7, 2)

#cont(elemento) retorna quantas vezes o elemento aparece
print(tupla.count(2)) 

#index(elemento) retorna o indice do primeira aparicao daquele elemento
print(tupla.index(4))

#len(tupla) retorna o tamanho da tupla
print(len(tupla))