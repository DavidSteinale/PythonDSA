import random

def sortear():
    arquivo = open('palavras.txt', 'r')  # abra o arquivo.tx com as palavras a ser escolhidas
    palavraSortida = []  # lista para receber uma palavra soteada

    for x in arquivo:  # peca o conteudo do arquivo e coloca dentro da palavraSortida
        palavraSortida.append(x.strip())  # elimina os espaços e adiciona na lista
    arquivo.close()  # fecha a leitura do arquivo
    posicao = random.randrange(0, len(palavraSortida))  # gera um numero aleatório com base na quantidade de palavras
    return palavraSortida[posicao]

if(__name__ == "__main__"):
    sortear()