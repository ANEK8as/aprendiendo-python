def calcular_promedio(lista_calificaciones):
    suma = sum(lista_calificaciones)
    cantidad = len(lista_calificaciones)
    return suma / cantidad
calificaciones =  []
while True:
    dato = input("ingresa un valor (o fin para finalizar) :")
    if dato == "fin":
         break
    numero = float(dato)
    calificaciones.append(numero)
   
print (f"el valor mas alto es {max(calificaciones)}")
print(f"el valor mas bajo es {min(calificaciones)}")
print(f"el promedio es {calcular_promedio(calificaciones)}")

promedio = calcular_promedio(calificaciones)
if promedio > 9.5:
    print("Excelente")
elif promedio >= 8:
    print("Bueno")
elif promedio >= 7:
    print("Aprobado")
else:
    print("reprobado")

    
    
