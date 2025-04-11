#Entrada/Saida
#Utilizamos entradas e saidas para interagir com o usuario

#Funcao Input
#para o usuario passar as informacoes, utilizamos a funcao input()
nome = input("Digite seu Nome: ")
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Maior de Idade!")
else:
    print("Menor de Idade!")
#A funcao input retorna apenas strings, por isso, quando necessario, utilizamos casting, ou seja, idade e int

#Saida
#Para realizar a saida, utilizamos a funcao print
print("Nome: " + nome + ", " + str(idade) + " anos") #nao podemos utilizar + idade +, pois idade e inteiro, entao usamos casting
#ou utilizando a f-string e {}, para digitar as variaveis diretamente
print(f"Nome: {nome}, {idade} anos")