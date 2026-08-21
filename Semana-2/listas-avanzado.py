materias = []
while True:
    materia = input("ingresa una materia (o fin para finalizar): ")
    if materia == "fin":
        break
    materias.append(materia)
print(materias [0])
print(materias [-1])
print(materias [:3])

materias[2] = "matematicas"
print(materias)
materias.remove ("matematicas")
print(materias)