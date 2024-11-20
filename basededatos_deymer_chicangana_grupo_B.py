def validar_entrada(tipo, mensaje):
    while True:
        entrada = input(mensaje)
        if tipo == 'int':
            try:
                return int(entrada)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif tipo == 'str':
            if entrada.strip() == "":
                print("Este campo no puede estar vacío.")
            else:
                return entrada
        elif tipo == 'gmail':
            if "@" in entrada and "." in entrada:
                return entrada
            else:
                print("Por favor, ingrese un correo electrónico válido.")

def registrar_persona():
    return [
        validar_entrada('str', "Ingrese su nombre completo: "),
        validar_entrada('str', "Ingrese su número de identificación profesional si es enfermera sino ingrese su numero de documento: "),
        validar_entrada('int', "Ingrese su edad: "),
        validar_entrada('str', "Ingrese su número de contacto: "),
        validar_entrada('gmail', "Ingrese su correo electrónico: "),
        validar_entrada('str', "Ingrese su dirección: ")
    ]

def registrar_enfermera():
    return registrar_persona() + [
        validar_entrada('str', "Ingrese la especialidad: "),
        validar_entrada('int', "Ingrese los años de experiencia: "),
        validar_entrada('str', "Ingrese la disponibilidad horaria: ")
    ]

def registrar_paciente():
    return registrar_persona() + [
        validar_entrada('str', "Ingrese el género: "),
        validar_entrada('str', "Ingrese la enfermedad o condición médica principal: "),
        validar_entrada('str', "Ingrese el nombre y número de contacto de una persona en caso de emergencia: "),
        validar_entrada('str', "Ingrese alergias y medicamentos actuales: ")
    ]

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def buscar_por_identificacion(lista, identificacion):
    for persona in lista:
        if persona[1] == identificacion:
            return persona
    return None

# Implementación del algoritmo de Burbuja
def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparación por el nombre (posición 0 en cada lista)
            if lista[j][0].lower() > lista[j + 1][0].lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def registrar_usuario():
    enfermeras = []  # Matriz de enfermeras
    pacientes = []   # Matriz de pacientes

    while True:
        usuario = input("¿Es usted enfermera o paciente? (enfermera/paciente): ").strip().lower()
        if usuario == 'enfermera':
            enfermeras.append(registrar_enfermera())
            print("Datos de la enfermera registrados exitosamente.")
        elif usuario == 'paciente':
            pacientes.append(registrar_paciente())
            print("Datos del paciente registrados exitosamente.")
        else:
            print("Opción no válida, intente de nuevo.")

        continuar = input("¿Desea registrar a otra persona? (si/no): ").strip().lower()
        if continuar != 'si':
            print("Proceso de registro finalizado.")
            break

    # Ordenar las listas usando Burbuja
    ordenar_burbuja(enfermeras)
    ordenar_burbuja(pacientes)

    # Mostrar los registros ordenados
    print("\nEnfermeras Registradas:")
    mostrar_matriz(enfermeras)

    print("\nPacientes Registrados:")
    mostrar_matriz(pacientes)

    # Búsqueda por identificación
    identificacion = input("\nIngrese una identificación para buscar: ")
    resultado = buscar_por_identificacion(enfermeras + pacientes, identificacion)
    if resultado:
        print("Persona encontrada:", resultado)
    else:
        print("No se encontró ninguna persona con esa identificación.")

registrar_usuario()



