from multiply import multi
from multiply import divisao
from soma_sub import soma
from soma_sub import subtracao

def evaluate(lista):
    while multi(lista):
        continue

    while subtracao(lista):
        continue

    while soma(lista):
        continue

    while divisao(lista):
        continue

    if len(lista)==1:
        return lista[0]
    else:
        return lista

