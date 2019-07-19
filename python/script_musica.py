from musica import *


cancao = [ (Do,0.3),(Re,1)]

for nota,tempo in cancao:
      nota.tocafade(tempo)


nova = Nota("FaChar",0.2)
nova.toca(1)


def novizia_rebelde(option=1):
    notas= [Do,Re,Mi,Do,Mi,Do, Mi,
            Re, Mi, Fa,  Fa , Mi, Re, Fa ]
    duracao = [300,200,300,200,300,300,500,
               300,200,200,200,200,200,1000]
    for i,nota in enumerate(notas):
        tempo=duracao[i]/1000
        if option == 1:
            nota.toca(tempo)
        elif option == 2:
            nota.tocafade(tempo)
            sleep(tempo*.9) #sleep e uma funcao do modulo time que ja existe no modulo musica

#novizia_rebelde(2)
