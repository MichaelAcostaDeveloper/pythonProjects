import math
def alertasAlgebraicasRadicaion(a):
    while a<0:
        print("El valor ingresado no debe ser negativo")
        a=float(input("Ingrese el valor nuevamente: "))
    raiz=pow(a,0.5)
    return print("El resultado: "+str(raiz)+".")

def alertasAlgebraicasDivision(a,b):
    while b==0:
        print("EL segundo valor debe ser distinto de cero")
        b=float(input("Ingrese el segundo valor nuevamente: "))
    division=a/b
    return print("El cociente es: "+str(division)+".")

def alertasAlgebraicasLogaritmos(base,argumento):
    while (float(base)<=0 or float(base)==1):
        print('El valor de la base debe ser diferente de 1 o menor o igual a 0, cambiela ahora!!!')
        base=float(input("Ingrese el valor nuevamente: "))
    while (float(argumento)<=0):
        print('El valor del argumento debe ser siempre mayor que cero, cambielo ahora!!!')
        argumento=float(input("Ingrese el valor nuevamente: "))
    respuesta=math.log(argumento,base)
    return print("El resultado: "+str(respuesta)+".")

def alertasAlgebraicasExponentes(base,exponente):
    while (float(base)<=0 or float(base)==1):
        print('El valor de la base debe ser diferente de 1 o menor o igual a 0, cambiela ahora!!!')
        base=float(input("Ingrese el valor nuevamente: "))
    respuesta=pow(base,exponente)
    return print("El resultado: "+str(respuesta)+".")

def ejecucionPotencia(a,b): 
    respuesta=pow(a,b)
    return print("La potencia es: "+str(respuesta)+".")

def ejecucionTrigonometria(a):
    definicion=int(input('''Seleccione la funcion trigonometrica a calcular:
                            1. Seno
                            2. Coseno
                            3. Tangente
                            -> '''))
    if definicion==1:
        resultado=math.sin(float(a))
        print("El seno del valor ingresado es: "+str(resultado) + '.')
    elif definicion==2:
        resultado=math.cos(float(a))
        return print("El coseno del valor ingresado es: "+str(resultado) + '.')
    else:
        if a==0:
            return print("La tangente de este valor esta indefinida.")
        else:
            resultado=math.tan(float(a))
        return print("La tangente del valor ingresado es: "+str(resultado) + '.')




def conteo_letras_palabra():
    pass
def inversion_palabras():
    pass
def operaciones_basicas(val1,val2):
    operacion=int(input("""Seleccione la operacion que desea: 
    1. suma
    2. resta
    3. producto
    4. division
    5. raiz cuadrada
    6. potenciacion
    7. logaritmo
    8. exponencial
    9. trigonometrica
    -> """))

    if operacion==1:
        suma=val1+val2
        return print("La suma es: "+str(suma)+".")
    elif operacion==2:
        resta=val1-val2
        return print("La resta es: "+str(resta)+".")
    elif operacion==3:
        producto=val1*val2
        return print("El producto es: "+str(producto)+".")
    elif operacion==4:
        alertasAlgebraicasDivision(val1,val2)

    elif operacion==5:
        pregunta=int(input('''Que valor ingresado desea que sea el radicando:
                            Digite 1 para el valor ''' + str(val1) + '''
                            Digite 2 para el valor ''' + str(val2) + '''
                            -> '''))
        if pregunta==1:
            alertasAlgebraicasRadicaion(val1)
        else:
            alertasAlgebraicasRadicaion(val2)
    elif operacion==6:
        pregunta=int(input('''Que valor ingresado desea que sea la base:
                            Digite 1 para el valor ''' + str(val1) + '''
                            Digite 2 para el valor ''' + str(val2) + '''
                            -> '''))
        if pregunta==1:
            ejecucionPotencia(val1,val2)
        else:
            ejecucionPotencia(val2,val1)
    elif operacion==7:
        pregunta=int(input('''Que valor ingresado desea que sea la base:
                            Digite 1 para el valor ''' + str(val1) + '''
                            Digite 2 para el valor ''' + str(val2) + '''
                            -> '''))
        if pregunta==1:
            alertasAlgebraicasLogaritmos(val1,val2)
        else:
            alertasAlgebraicasLogaritmos(val2,val1)
    elif operacion==8:
        pregunta=int(input('''Que valor ingresado desea que sea la base:
                            Digite 1 para el valor ''' + str(val1) + '''
                            Digite 2 para el valor ''' + str(val2) + '''
                            -> '''))
        if pregunta==1:
            alertasAlgebraicasExponentes(val1,val2)
        else:
            alertasAlgebraicasExponentes(val2,val1)
    elif operacion==9:
        pregunta=int(input('''Que valor ingresado desea que sea el argumento de la funcion trigonometrica:
                            Digite 1 para el valor ''' + str(val1) + '''
                            Digite 2 para el valor ''' + str(val2) + '''
                            -> '''))
        if pregunta==1:
            ejecucionTrigonometria(val1)
        else:
            ejecucionTrigonometria(val2)
    else:
        print("No existe esa operacion!")

def run():
    opcion=int(input("""Selecciona un opcion:
    1. Operaciones básicas
    2. Conteo de letras de una palabra
    -> """))
    if opcion==1:
        val1=float(input("Ingrese el primer valor: "))
        val2=float(input("Ingrese el segundo valor: "))
        operaciones_basicas(val1,val2)
    elif opcion==2:
        palabra=str("Ingrese una palabra:")
        conteo_letras_palabra(palabra)
    else:
        print('Por favor seleccione una opcion')

if __name__=='__main__':
    run()

