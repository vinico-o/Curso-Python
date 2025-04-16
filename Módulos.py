#Módulo é um arquivo que possui definição de funções, classes e variáveis que podem ser utilizados em outros programas
#A importação de módulos permite utilizar suas funcionalidades
#fazemos uma importação utilizando a declaração import

import math
import random
import datetime

numero = 25
raiz = math.sqrt(numero) #math.sqrt é uma função do módulo math
print(raiz)

#podemos utilizar funções específicas de um módulo, utilizando "from "módulo" import "função""
from math import sqrt
numero = 25
raiz = sqrt(numero)
print(raiz)

#Exemplos comuns de módulos
aleatorio = random.randint(1, 10) #gera um inteito aleaorio entre 1 e 10
print(aleatorio)

data = datetime.datetime.now() #retorna a data e a hora atual
print(data)