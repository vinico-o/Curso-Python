#Dicionario é uma Estrutura de dados mutável que armazena e pares de chave-valor

#Criação
pessoa = {"nome": "Vinicius", "cidade": "Aracatuba", "idade": 18}
pessoa2 = {"profissao": "programador"}

print(pessoa) #imprime o dicionario

#Acesso
print(pessoa["nome"])
print(pessoa["cidade"])
print(pessoa["idade"])

#Metodos
print(pessoa.keys()) #retorna dict_keys + todas as chaves do dicionario
print(pessoa.values()) #retorna dict_values + valores de todas as chaves do dicionario
print(pessoa.items()) #retorna dict_items + todos os pares chave-valor do dicionario

pessoa.update(pessoa2) #agrega um outro dicionario ao que chamou a funcao
print(pessoa)
pessoa.update({"pais": "brasil"}) #tambem pode ser feito assim
print(pessoa)
