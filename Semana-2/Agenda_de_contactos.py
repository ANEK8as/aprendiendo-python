contactos = []  
while True:
    opcion = input("ingresa una opción (agregar, buscar, listar o salir): ")
    if opcion == "agregar":
          while True:
              nombre = input("Ingresa un nuevo contacto (o fin para finalizar):")   
              if nombre == "fin":
               break
              contacto_nuevo = {   
              "nombre": "",
              "telefono": "",
              "correo": "",
}
              contacto_nuevo["nombre"] = nombre
              contacto_nuevo["telefono"] = input("Ingresa el teléfono del contacto: ")
              contacto_nuevo["correo"] = input("Ingresa el correo del contacto: ")
              contactos.append(contacto_nuevo)
              print(f"Contacto agregado: {contacto_nuevo}")
    elif opcion == "buscar":
        buscador = input("ingresa el nombre del contacto a buscar;")
        for contacto in contactos:
         if buscador == contacto["nombre"]:
            print(f"contacto encontrado: {contacto}")
            break
        else:
            print("contacto no encontrado")
    elif opcion == "listar":
       for contacto in contactos:
          print(contacto)
    if opcion == "salir":
      print(contactos)
      break