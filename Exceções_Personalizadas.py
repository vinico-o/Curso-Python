#Exceções personalizadas
#Também é possível criar exceções personalisadas, utilizadas quando há situações específicas

def positivo(x):
    if x < 0:
        raise Exception("Numero negativo!") #criacao e drescricao do erro
    
numero = -9

try:
    positivo(numero)
except Exception as e: #a excecao e capturada utilizando a varivael "e"
    print(f"Erro: {e}") #aqui, utilizamos f antes da string para expecificar que utilizaremos o valor da variavel na impressao
                        #Nesse caso, da variavel e, que e uma excecao

