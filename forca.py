import random

def jogar_forca():
    print('ola ao jogo forca')
    palavraSortida = [] # lista para receber uma palavra soteada
    acerto = 0
    errou = 0
    enforcou = False
    acertou = False

    arquivo = open('palavras.txt','r') # abra o arquivo.tx com as palavras a ser escolhidas

    for x in arquivo: # peca o conteudo do arquivo e coloca dentro da palavraSortida
        palavraSortida.append(x.strip())# elimina os espaços e adiciona na lista
    arquivo.close()# fecha a leitura do arquivo

    posicao = random.randrange(0,len(palavraSortida))# gera um numero aleatório com base na quantidade de palavras

    cont = len(palavraSortida[posicao])
    lista = ["_" for cont in palavraSortida[posicao]] # inicia uma lista com o caracter "_" para cada letra da palavra_secreta

    print('Forca -> ', lista) #mostra a lista a ser completada

    while (not enforcou and not acertou):
        index = 0
        chute = input("informe um letra? ")
        if(chute.lower() in palavraSortida[posicao]):
            for x in palavraSortida[posicao]:
                if(chute.lower() == x): #valida se existe a letra digitada mesmo sendo maiuscula
                    lista[index] = chute #coloca a letra achada na posição certa
                    acerto+=1 #soma os acertos
                index += 1
        else:
             errou+=1
        print('lista', lista)
        if(acerto==cont):
            print('Parabéns você ganho!!!')
            acertou=True
        if(errou==cont):
            print('Você foi enforcado!!')
            enforcou=True

if(__name__ == "__main__"):
    jogar_forca()