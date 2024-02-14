# Montes Barajas Leonardo Daniel
# 21590293
# Metodos numericos - Metodo Bisección
# Encontrar las raíces de una función polinomial

import random
import math

continuar = "True"

x = 0
a = random.randint(-1000, 1000)
b = random.randint(-1000, 1000)
fa = (a**3)-2*math.sin(a)
fb = (b**3)-2*math.sin(b)
Fx = x

while (continuar == "True"):
    print("Limite inferior del intervalo: "+str(a))
    print("Limite superior del intervalo: "+str(b))
    # Significa q si un valor esta en el lado opuesto de la grafica se esta multiplicando un numero negativo
    if (fa*fb >= 0):
        print("No hay raíz entre el intervalo.")
        seguir = int(input("Desea continuar\nIngrese: 1 = Si ó 2 = No:\n"))
        if seguir == 1:
            continuar = "True"
            print("Ingrese nuevos valores")
        else:
            continuar = "False"
            print("Hasta pronto :D")
            break
    else:
        fc = 100
        while (abs(fc) > 10**(-12)):
            c = (a+b)/2
            fc = (c**3)-2*math.sin(c)
            if ((fa*fc) < 0):
                b = c
            elif ((fc*fb) < 0):
                a = c
    print("La raíz se ubica en x = "+str(c))
    print("f(c)="+str(fc))
    break
