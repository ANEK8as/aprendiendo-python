palabras = []
while True:
    palabra = input("ingresa una palabra (o fin para finalizar): ")
    if palabra == "fin":
        break
    palabras.append(palabra)
def contadorpalabras(palabras):
    return len(palabras)
numpalabras = contadorpalabras(palabras)
print(f"número de palabras: {numpalabras}")
print(palabras)
if numpalabras > 5:
    print("Lista larga")
else:
    print("Lista corta")