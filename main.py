import random
abcedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

palabra = "Agente"

def generardesplazamiento():
    return random.randint(1, 10)

def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if letra in abcedario:
            indice = (abcedario.index(letra) + desplazamiento) % len(abcedario)
            resultado += abcedario[indice]
        else:
            resultado += letra
    return resultado




