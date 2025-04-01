#Os operadores aritmeticos sao utilizados para realizar operacoes matematicas basicas

a = 10
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
modulo = a % b #retorna o resto de a / b
exponenciacao = a ** b

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(divisao_inteira)
print(modulo)
print(exponenciacao)


#Os Operadores de comparacao sao utilizados para comparar dois valores e retornar um valor booleano, de acordo com o resultado
igual_a = a == b
diferente_de = a != b
maior = a > b
menor = a < b
maior_igual = a >= b
menor_igual = a <= b

print(igual_a)
print(diferente_de)
print(maior)
print(menor)
print(maior_igual)
print(menor_igual)

#Os operadores logicos combinam expressoes e retornam valores booleanos
operador_and = (a != b) and (a > b)
operador_or  = (a != b) or (a > b)
operador_not = not(a == b)

print(operador_and) #retorna True se ambas operacoes sao True
print(operador_or) #retorna True se ao menos uma das operacoes e True
print(operador_not) #inverte o valor da operacao