import random

import sorteio


def jogar_forca():
    print('ola ao jogo forca')
  #  palavraSortida = [] # lista para receber uma palavra soteada
    acerto = 0
    errou = 0
    enforcou = False
    acertou = False

    palavraSecreta = sorteio.sortear()
    cont = len(palavraSecreta)
    lista = ["_" for cont in palavraSecreta] # inicia uma lista com o caracter "_" para cada letra da palavra_secreta
    print('Forca -> ', lista) #mostra a lista a ser completada

    while (not enforcou and not acertou):
        index = 0
        chute = input("informe um letra? ")
        if(chute.lower() in palavraSecreta):
            for x in palavraSecreta:
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