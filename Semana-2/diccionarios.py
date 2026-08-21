materia = {
"nombre": "Eduardo",
"maestro": "Juan",
"materia": "Matemáticas"
}

print (materia["nombre"])
print (materia["maestro"])
print (materia["materia"])
materia["nombre"] = "Pedro"
materia["horario"] = "7-9"
for clave, valor in materia.items():
    print(f"{clave}: {valor}")
