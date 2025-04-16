#Leitura e Escrita em arquivos
#Temos alguns modos para abrir o arquivos, leitura (r), escrita (w) e anexar (a)

#leitura de arquivos
#o arquivo deve ser aberto com open() no modo de leitura, podemos ler o conteudo com read ou readlines
#read() le o arquivo inteiro, enquanto readlines() somente uma linha
arquivo = open("teste.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

#Escrita de arquivos
#o arquivo deve ser aberto com open() no modo de escrita, se o arquivo nao esxistir, sera criado
#obs: se o arquivo ja existir, ele sera sobrescrito
arquivo = open("teste.txt", "w")
arquivo.write("Vinicius Mardegan")
arquivo.close()

#para fechar os arquivos de forma automatica, utilizamos a declaracao with
with arquivo.open("teste.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
#o arquivo e fechado automaticamente ao acabar o bloco