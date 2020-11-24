from operator import index

lista = [322, 321, 433, 123, 311, 233, 343, 354, 324, 322, 344, 431]
somaTodos = sum(lista)
totalDados = len(lista)


def calculaMedia():
    media = somaTodos / totalDados
    print('Resultado da média {}'.format(media))


def ordenaLista():
    listaSorted = sorted(lista)
    print('Lista ordenada {}'.format(listaSorted))


def posicaoLista():
    listaSort = sorted(lista)
    listalista = len(listaSort)/2
    print('Motra posição na lista', listalista)


posicaoLista()
ordenaLista()
calculaMedia()
#print('Resultado da média {}'.format(media))
