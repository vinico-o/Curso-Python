#As listas (ou vetores) permitem armazenar uma coleção de elementos

numeros = [1, 2, 3, 4, 5]
letras = ['a', 'b', 'c']
strings = ["vinicius", "mardegan", "unesp"]


#Acessando elementos
print(numeros[0])
print(letras[1])
print(strings[2])

#Os indices negativos representam a lista na ordem contraria, do final para o comeco
print(numeros[-1])
print(letras[-2])
print(strings[-3])

#Funcoes com Listas
#append(elemento): adiciona um elemento ao final da lista.
numeros.append(6)
print(numeros)

#insert(indice, elemento): insere um elemento em uma posição específica da lista.
numeros.insert(1, 1)
print(numeros)

#remove(elemento): remove a primeira ocorrência de um elemento na lista.
numeros.remove(1)
print(numeros)

#pop(indice): remove e retorna o elemento em uma posição específica da lista.
removido = numeros.pop(0)
print(numeros)
print(removido)

#sort(): ordena os elementos da lista em ordem ascendente.
numeros.sort()
print(numeros)

#reverse(): inverte a ordem dos elementos na lista.
numeros.reverse()
print(numeros)


#Listas de Compreensao
numeros = [1, 2, 3, 4, 5]
#seleciona cada elemento de "numeros" e se forem impares, coloca o quadrado deles na nova lista
quadrados_impares = [x ** 2 for x in numeros if x % 2 != 0]
print(quadrados_impares)