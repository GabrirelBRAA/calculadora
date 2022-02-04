


def multi(lista):
    calculo = []
    parent = []
    for (n, idx) in zip(lista, enumerate(lista)):
        if n == "*":
            before = lista[idx[0] - 1]
            after = lista[idx[0] + 1]

            if isinstance(before, list):
                lista[idx[0]] = [n * after for n in before]
                lista.pop(idx[0] - 1) and lista.pop(idx[0])

                return True

            elif isinstance(after, list):
                lista[idx[0]] = [n * before for n in after]
                lista.pop(idx[0] - 1) and lista.pop(idx[0])

                return True

            elif isinstance(before, int) and isinstance(after, int):
                lista[idx[0]] = before * after
                lista.pop(idx[0] - 1)
                lista.pop(idx[0])

                return True


    return False

def divisao(lista):
        calculo = []
        parent = []
        for (n, idx) in zip(lista, enumerate(lista)):
            if n == "/":
                before = lista[idx[0] - 1]
                after = lista[idx[0] + 1]

                if isinstance(before, list):
                    lista[idx[0]] = [n / after for n in before]
                    lista.pop(idx[0] - 1) and lista.pop(idx[0])

                    return True

                elif isinstance(after, list):
                    lista[idx[0]] = [n / before for n in after]
                    lista.pop(idx[0] - 1) and lista.pop(idx[0])

                    return True

                elif isinstance(before, int) and isinstance(after, int):
                    lista[idx[0]] = before / after
                    lista.pop(idx[0] - 1)
                    lista.pop(idx[0])

                    return True

        return False


