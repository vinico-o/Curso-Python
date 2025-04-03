#As funcoes sao blocos reutilizaveis de codigos que sao somente executadas quando sao chamadas
#Elas ajudam a organizar o codigo e otimizar, em casos de repeticoes de codigos

#Definicao
#def nome_funcao (parametros):
def hello ():
    print("hello world!")

#Chamada
hello()

#Parametros e Argumentos
#As funcoes aceitam parametros (valores poassados quando a funcao e chamada)
nome = "Vinicius"
def Saudacao(nome):
    print("Bom dia,", nome)

Saudacao(nome)

#Para passar um numero indefinido de argumentos, utilizamos *parametro, que indica que pode ser passado mais de um parametro
def media(*numeros):
    soma = sum(numeros)
    qntd = len(numeros)
    return soma / qntd
print(media(10, 20, 30, 40))

#Valores de retorno
#A funcao pode retornar um resultado, atraves de "return" e o que sera retornado
num1 = 10
num2 = 20
def Soma(num1, num2):
    return num1 + num2

resultado = Soma(num1, num2)
print(resultado)

#Funcoes Anonimas (Lambda)
#Funcoes sem nome e defindas em uma unica linha, geralmente usada em funcoes pequenas
dobro = lambda x: 2 * x
print(dobro(10))

#EScopo de Variaveis
numero = 10
def FuncaoGlobal():
    print(numero)
def FuncaoLocal():
    numero = 20 #O valor de 10 somente e alterado no escopo dessa funcao
    var_local = 10
    print(var_local)
    print(numero)

FuncaoGlobal()
FuncaoLocal()
FuncaoGlobal()
#print(var_local) #e gerado um erro, pois var_local so e visivel na FuncaoLocal

