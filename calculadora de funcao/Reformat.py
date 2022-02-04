

def reformat_code(x):
    lista_util = []
    lista_numero = []
    numero_inteiro = ""
    for letter in x:
        if letter == " ":
            pass

        elif letter.isdigit():
            lista_numero.append(letter)

        elif letter == "+":
            if lista_numero:

                for x in lista_numero:
                    numero_inteiro += x
                lista_util.append(int(numero_inteiro))

            lista_numero = []
            numero_inteiro = ""

            lista_util.append("+")

        elif letter == "-":
            if lista_numero:

                for x in lista_numero:
                    numero_inteiro += x
                lista_util.append(int(numero_inteiro))

            lista_numero = []
            numero_inteiro = ""

            lista_util.append("-")

        elif letter == "*":
            if lista_numero:

                for x in lista_numero:
                    numero_inteiro += x
                lista_util.append(int(numero_inteiro))

            lista_numero = []
            numero_inteiro = ""

            lista_util.append("*")


        elif letter == "x":
            if lista_numero:

                for x in lista_numero:
                    numero_inteiro += x
                lista_util.append(int(numero_inteiro))
                numero_inteiro = ""
                lista_numero = []
                lista_util.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

            else:
                lista_util.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        elif letter == "(":
            if lista_numero:

                for x in lista_numero:
                    numero_inteiro += x
                lista_util.append(int(numero_inteiro))

            lista_numero = []
            numero_inteiro = ""

            lista_util.append("(")

        elif letter == ")":
            if lista_numero:

                for x in lista_numero:
                    numero_inteiro += x
                lista_util.append(int(numero_inteiro))

            lista_numero = []
            numero_inteiro = ""

            lista_util.append(")")

        elif letter == "/":
            if lista_numero:

                for x in lista_numero:
                    numero_inteiro += x
                lista_util.append(int(numero_inteiro))

            lista_numero = []
            numero_inteiro = ""

            lista_util.append("/")

    if lista_numero:

        for x in lista_numero:
            numero_inteiro += x

        lista_util.append(int(numero_inteiro))

    return lista_util



















