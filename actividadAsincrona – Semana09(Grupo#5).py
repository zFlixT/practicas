#Actividad Asincrona_S.09.
print("Bienvenido al programa correspondiente a la actividad asíncrona número nueve.")
print("")

#DATOS DEL USUARIO:
print("Para iniciar, favor llenar la siguiente información con tus datos personales.")
nombres = input("Ingresa tus nombres: ")
apellidos = input("Ingresa tus apellidos: ")
edad = int(input("Ingresa tu edad: "))
sexo = input("""Ingresa tu sexo. 
             Para ello, digita la palabra 'Femenino' o 'Masculino', o:
             Si tu sexo es 'Femenino', favor digitar 'F'.
             Si tu sexo es 'Masculino', favor digitar 'M'""")
print("")

#MUESTRA DE LOS DATOS DEL USUARIO OBTENIDOS AL INICIO DEL PROGRAMA:
print("Su nombre completo es: ", nombres, apellidos)
print("Su edad es de: ", edad)
print("Y su sexo es: ", sexo)
print("")

#DATOS SEGUN LA EDAD Y SEXO DEL USUARIO:
if sexo == "F" or sexo == "f" or sexo == "Femenino" or sexo == "femenino":
    if edad <= 2:
        print("Etapa: Niña")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Bebé.")
    if edad >= 3 and edad == 5:
        print("Etapa: Niña")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Infancia.")
    elif edad >= 6 and edad <= 11:
        print("Etapa: Niña")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Niñez.")
    elif edad >= 12 and edad <= 18:
        print("Etapa: Chica")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Adolescencia.")
    elif edad >= 19 and edad <= 26:
        print("Etapa: Chica")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Juventud.")
    elif edad >= 27 and edad <= 40:
        print("Etapa: Mujer")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Adultez Jóven.")
    elif edad >= 41 and edad <= 55:
        print("Etapa: Señora")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Adultez.")
    elif edad >= 56 and edad == 65:
        print("Etapa: Señora")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Persona Mayor.")
    elif edad >= 66 and edad == 90:
        print("Etapa: Abuela")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Vejez.")
    else:
        print("Etapa: Abuela")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Grandes Ancianos.")
        
elif sexo == "M" or sexo == "m" or sexo == "Masculino" or sexo == "masculino":
    if edad <= 2:
        print("Etapa: Niño")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Bebé.")
    if edad >= 3 and edad == 5:
        print("Etapa: Niño")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Infancia.")
    elif edad >= 6 and edad <= 11:
        print("Etapa: Niño")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Niñez.")
    elif edad >= 12 and edad <= 18:
        print("Etapa: Chico")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Adolescencia.")
    elif edad >= 19 and edad <= 26:
        print("Etapa: Chico")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Juventud.")
    elif edad >= 27 and edad <= 40:
        print("Etapa: Hombre")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Adultez Jóven.")
    elif edad >= 41 and edad <= 55:
        print("Etapa: Señor")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Adultez.")
    elif edad >= 56 and edad == 65:
        print("Etapa: Señor")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Persona Mayor.")
    elif edad >= 66 and edad == 90:
        print("Etapa: Abuelo")
        print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Vejez.")
else:
    print("Etapa: Abuelo")
    print(nombres, apellidos, ", en este momento usted se encuentra en la etapa de: Grandes Ancianos.")
print("")

#DETERMINACION DE LA EDAD; Par o Impar:
print("A continuación se determinará si tu edad es 'par' o 'impar'")
nume = int(input("Por favor, digita nuevamente tu edad: "))
if nume %2 == 0:
    print("Tu edad es ", nume, " y es un número par.")
else:
    print("Tu edad es ", nume, " y es un número impar.")
print("")
print("FIN DEL PROGRAMA.")
