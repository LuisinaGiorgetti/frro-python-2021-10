"""Type, Comprensión de Listas, Sorted y Filter."""


from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    num = []
    letras = []

    for elemento in lista:
        if type(elemento) == str:
            letras.append(elemento)
        else:
            num.append(elemento)
    letras.extend(num)
    return letras


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN

###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""

    num = [elemento for elemento in lista if type(elemento) != str]
    letras = [elemento for elemento in lista if type(elemento) == str]
    letras.extend(num)
    return letras

# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """
    return sorted(lista, key=lambda x: type(x) != str)

# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """
    return list(filter(lambda x: type(x) == str, lista)) + list(filter(lambda x: type(x) != str, lista))


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""

    # CASO BASE
    if len(lista) == 1:
        return lista

    # CASO RECURSIVO

    if type(lista[0]) == str:
        return list(lista[0]) + numeros_al_final_recursivo(lista[1:])
    elif type(lista[-1]) != str:
        numeros = lista[-1:]
        return list(numeros_al_final_recursivo(lista[:-1])) + numeros
    else:
        for x in list(reversed(lista)):
            if type(x) != str:
                i = lista.index(x)
                lista.append(x)
                lista.remove(x)
                break
        return numeros_al_final_recursivo(lista)


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
