from evaluate import *

def parenthesis(lista):
    left = False
    right = False
    for idx in enumerate(lista):
        if idx[1]=="(":
            left=idx[0]

        elif idx[1]==")":
            right=idx[0]


        if right:
            lista[left]=lista[left+1:right]
            lista[left]=evaluate(lista[left])
            del lista[left+1:right+1]
            return True

    return False




