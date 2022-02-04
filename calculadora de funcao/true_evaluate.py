from parenthesis import *

def true_evaluate(lista):

    while parenthesis(lista):
        continue

    while multi(lista):
        continue

    while subtracao(lista):
        continue

    while soma(lista):
        continue

    while divisao(lista):
        continue

    if len(lista) == 1:
        return lista[0]
    else:
        return lista