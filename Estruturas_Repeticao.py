#As estruturasd de repeticao permitem executar um bloco de codigo diversas vezes
numero = 1
for numero in range(1, 11): #utilizado quando ja sabemos previamente quantas iteracoes ocorrerao
    print(numero)           #normalmente utilizado para percorrer sequencias


contador = 0
while contador <= 10: #o while e executado enquando a condicao for verdadeira
    print(contador)   #normalmente utilizado quando nao sabemos u numero de iteracoes
    contador += 1

contador = 0
while 1:
    if contador == 5:
        break #o break e utilizado para parar prematuramente um loop
    print(contador)
    contador += 1

contador = 0
for contador in range(1, 10):
    if contador % 2 == 0:
        continue #o continue ignora os blocos de comando posteriores, passando direto para iteracao
    print(contador)

contador = 0
for contador in range(1, 10):
    pass #a instrucao pass nao faz nada, normalmente utilizado para reservar um bloco de codigo para implementar funcoes posteriormente
