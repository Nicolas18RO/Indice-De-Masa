opcion = ""
while opcion != "2":
    print("---Clasificacion OMS---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    peso = input("Ingrese el peso: ")
    altura = input("Ingrese la altura: ")
    ClasificacionOMS = ""
    indice = float(peso)/(float(altura)*float(altura))

    if indice < 25:
        ClasificacionOMS = "Riesgo Bajo"
    elif indice >= 25 and indice <35:
        ClasificacionOMS = "Riesgo Medio"
    else: 
        ClasificacionOMS = "Riesgo Alto"

    print(f"Excelente! {nombre} {apellido}\nSu índice de masa es: {indice:.2f}\nSu riesgo es: {ClasificacionOMS}")
    opcion = input("Selecciona: \n1. Ingresar otra persona \n2. Salir \n->")