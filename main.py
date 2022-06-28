import advinhacao
import forca

menu = int(input('Digite sua opção: \n 1 - ADVINHAÇÃO \n 2 - FORCA'))

if(menu == 1):
    adv = advinhacao
    adv.jogar_advinhacao()
else:
    forc = forca
    forc.jogar_forca()

