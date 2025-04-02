#Conjunto e uma estrutura de dados mutavel (nao ordenada) que armazena uma colecao de elementos

#Criacao (sem ou com a funcao set())
carros = {"chevette", "opala", "eclipse"}
frutas = set(["banana", "melancia"])

#Assim coomo na matemtica, e possivel utilizar operacoes de conjuntos

#uniao (utilizando |)
pares = {2, 4, 6}
impares = {1, 3, 5}
primos = {2, 3, 5, 7}
numeros = pares | impares
print(numeros)

#intersecao (utilizando &) (presente nos dois conjuntos)
numeros = pares & impares #deve retornar vazio (set())
print(numeros)
numeros = impares & primos #deve retornar 3 e 5
print(numeros)

#diferenca (utilizando -) (subtrai um conjunto do outro, ou seja, retorna apenas os numeros exclusivos do primeiro conjunto)
numeros = primos - impares #deve retornar 2 e 7
print(numeros)

#diferenca simetrica (utilizando ^) (exclui o que e comum nos dois conjuntos)
numeros = primos ^ impares #deve retornar 1, 2 e 7
print(numeros)

#Metodos de Conjuntos

#add(elemento) adiciona o elemento no conjunto
print(carros)
carros.add("galante")
print(carros)

#remove(elemento) remove um elemento do conjunto (se ele nao existir, gera um erros)
print(carros)
#carros.remove("teste") #deve gerar erros
carros.remove("chevette")
print(carros)

#discard(elemento) remove um elemento do conjunto (se ele nao existir, nada occore)
print(carros)
carros.discard("chevette")
print(carros)

#clear() remove todos os elementos do conjunto
print(carros)
carros.clear()
print(carros)