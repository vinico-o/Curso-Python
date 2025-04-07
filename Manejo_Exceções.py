#Manejo de excecões em Python
#permite captorar e lidar com erros de maneira mais controlada

#Try
#Contem um codigo que pode gerar um excecao, se ocorrer essa excecao, o fluxo de execucao é alterado

try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisao por 0")

#Except
#Especifica o tipo de excecao que queremos lidar, podemos ter varios blocos except 
try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisao por 0")
except ValueError:
    print("Valor invalido")

#Finally
#Esse bloco sempre e executado, serve para realizar limpeza ou liberacao de recursos
try:
    arquivo = open("arquivo.txt", "w")
except FileNotFoundError:
    print("Arquivo nao existente")
finally:
    arquivo.close()
