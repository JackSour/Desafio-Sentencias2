
# Bienvenida
print("Programa interactivo de primeros auxilios para casos de emergencia.")
print("Se te solicitara ingresar Si/No para guiarte en cada paso")

respuesta = input("¿Deseas comenzar? (s/n):")

if respuesta.lower() != "s":
    print("¡Hasta luego!")
    
else:
    # Paso 1
    print("¿Responde a Estimulos?")
    respuesta = input("(s/n):")
    
    if respuesta.lower() != "n":
        print("Valorar la necesidad de llevarlo al hospital mas cercano")
        print("¡Hasta luego!")
        
    else:
        # Paso 2
        print("Abrir la via Aerea")
        print("¿Respira?")
        respuesta = input("(s/n):")
            
        if respuesta.lower() != "n":
            print("Permitirle posicion de suficiente ventilacion")
            print("¡Hasta luego!")
                
        else:
            # Paso 3
            ambulancia = "n"
            while ambulancia == "n":
                print("Administrar 5 Ventilaciones y llamar a Ambulancia")
                print("¿Signos de Vida?")
                respuesta = input("(s/n):")

                if respuesta.lower() != "n":
                    print("Reevaluar a la espera de la Ambulancia")
                    print("¿Llego la Ambulancia?")
                    respuesta = input("(s/n):")
                    
                    if respuesta.lower() != "n":
                        print("¡Hasta luego!")
                        break

                else:
                    # Paso 4 
                    print("Administrar Compresiones Toracicas hasta que llegue Ambulancia")
                    print("¿Llego la Ambulancia?")
                    respuesta = input("(s/n):")
                                        
                    if respuesta.lower() != "n":
                        print("¡Hasta luego!")
                        break
                    
                    else:
                        continue  # Volver al Paso #3 si la respuesta es "NO" para "llegó la ambulancia"
                    
                    