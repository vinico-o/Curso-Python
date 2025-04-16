#Pacotes são utilizados para organizar módulos em uma estrutura de diretório, evitando conflitos de nome, por exemplo

#Criar e Utilizar
#Devemos criar um diretório com um arquivo __init__.py dentro dele, junto com os módulos
from pacotes import modulo1, modulo2
num1 = 10
num2 = 5

modulo1.soma(num1, num2)
modulo2.subtracao(num1, num2)
