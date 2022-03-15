from asyncio import sleep
import math
from re import T
############FUNCIONES MATEMATICAS#############
#funcion de seleccion de elementos
def seleciona(a,b):
    pregunta=int(input('''Que valor ingresado desea que sea el argumento de la funcion seleccionada:
                    Digite 1 para el valor ''' + str(a) + '''
                    Digite 2 para el valor ''' + str(b) + '''
                    -> '''))
    if pregunta==1:
        return 1
    elif pregunta==2:
        return 2
    else:
        return seleciona(a,b)

#funcion de confirmacion de valores
def confirma(a,b):
    return print("-----------------------> Los numeros seleccionados son: "+str(a) +" y "+str(b))

#funcion suma
def suma(a,b):
    s=a+b
    return print("-----------------------> El resulado: "+str(s)+".")

#funcion resta
def resta(a,b):
    r=a-b
    return print("-----------------------> El resultado: "+str(r)+".")

#funcion producto
def producto(a,b):
    p=a*b
    return print("-----------------------> El resultado: "+str(p)+".")

#funcion radicacion
def alertasAlgebraicasRadicaion(a):
    while a<0:
        print("El valor ingresado no debe ser negativo")
        a=float(input("Ingrese el valor nuevamente: "))
    raiz=pow(a,0.5)
    return print("-----------------------> El resultado: "+str(raiz)+".")

#funcion division
def alertasAlgebraicasDivision(a,b):
    while b==0:
        print("EL segundo valor debe ser distinto de cero")
        b=float(input("Ingrese el segundo valor nuevamente: "))
    division=a/b
    return print("El cociente es: "+str(division)+".")

#funcion logaritmos
def alertasAlgebraicasLogaritmos(base,argumento):
    while (float(base)<=0 or float(base)==1):
        print('El valor de la base debe ser diferente de 1 o menor o igual a 0, cambiela ahora!!!')
        base=float(input("Ingrese el valor nuevamente: "))
    while (float(argumento)<=0):
        print('El valor del argumento debe ser siempre mayor que cero, cambielo ahora!!!')
        argumento=float(input("Ingrese el valor nuevamente: "))
    respuesta=math.log(argumento,base)
    return print("El resultado: "+str(respuesta)+".")

#funcion exponencial
def alertasAlgebraicasExponentes(base,exponente):
    while (float(base)<=0 or float(base)==1):
        print('El valor de la base debe ser diferente de 1 o menor o igual a 0, cambiela ahora!!!')
        base=float(input("Ingrese el valor nuevamente: "))
    respuesta=pow(base,exponente)
    return print("El resultado: "+str(respuesta)+".")

#funcion potenciacion
def ejecucionPotencia(a,b):
    respuesta=pow(a,b)
    return print("La potencia es: "+str(respuesta)+".")

#funcion trigonometrica
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
    elif definicion==3:
        if a==0:
            return print("La tangente de este valor esta indefinida.")
        else:
            resultado=math.tan(float(a))
        return print("La tangente del valor ingresado es: "+str(resultado) + '.')
    else:
        ejecucionTrigonometria(a)

#funcion de transformacion de radianes a grados
def tranf_rad_degree(a,b):
    a_1=math.degrees(a)
    b_1=math.degrees(b)
    return print('Los angulos pasados a grados son: '+str(a)+'rad = '+str(round(a_1,2))+'° y ' + str(b)+'rad = '+str(round(b_1,2))+'°')

######################################################################################################################################################################################
#menu del modulo de operaciones basicas
def operaciones_basicas(val1,val2):
    while True:
        operacion=int(input("""***Seleccione la operacion que desea:***
        1. suma
        2. resta
        3. producto
        4. division
        5. raiz cuadrada
        6. potenciacion
        7. logaritmo
        8. exponencial
        9. trigonometrica
        0. salir de este modulo
        -> """))
        if operacion==1:
            print('SUMA')
            confirma(val1,val2)
            suma(val1,val2)
        elif operacion==2:
            print('RESTA')
            resta(val1,val2)
            confirma(val1,val2)
        elif operacion==3:
            print('PRODUCTO')
            confirma(val1,val2)
            producto(val1,val2)
        elif operacion==4:
            print('DIVISION')
            confirma(val1,val2)
            alertasAlgebraicasDivision(val1,val2)
        elif operacion==5:
            print('RAIZ CUADRADA')
            confirma(val1,val2)
            if seleciona(val1,val2)==1:
                alertasAlgebraicasRadicaion(val1)
            else:
                alertasAlgebraicasRadicaion(val2)
        elif operacion==6:
            print('POTENCIACION')
            confirma(val1,val2)
            if seleciona(val1,val2)==1:
                ejecucionPotencia(val1,val2)
            else:
                ejecucionPotencia(val2,val1)
        elif operacion==7:
            print('LOGARITMOS')
            confirma(val1,val2)
            if seleciona(val1,val2)==1:
                alertasAlgebraicasLogaritmos(val1,val2)
            else:
                alertasAlgebraicasLogaritmos(val2,val1)
        elif operacion==8:
            print('EXPONENTES')
            confirma(val1,val2)
            if seleciona(val1,val2)==1:
                alertasAlgebraicasExponentes(val1,val2)
            else:
                alertasAlgebraicasExponentes(val2,val1)
        elif operacion==9:
            print('USO DE LA TRIGONOMETRIA')
            confirma(val1,val2)
            if seleciona(val1,val2)==1:
                ejecucionTrigonometria(val1)
                tranf_rad_degree(val1,val2)
            else:
                ejecucionTrigonometria(val2)
                tranf_rad_degree(val1,val2)
        elif operacion==0:
            run()
        else:
            print("No existe esa operacion!")

#MENU PRINCIPAL
def run():
    while True:
        opcion=int(input("""****BIENVENIDO AL PROYECTO****
        Selecciona una opcion:
        1. Operaciones básicas.
        2. Contando letras.
        3. Aplicación con datos.
        4. Salir
        -> """))
        if opcion==1:
            print('...BIENVENIDO AL MODULO DE OPERACIONES BASICAS...')
            val1=float(input("Ingrese el primer valor: "))
            val2=float(input("Ingrese el segundo valor: "))
            operaciones_basicas(val1,val2)
        elif opcion==2:
            print('...BIENVENIDO AL MODULO DE CONTEO DE LETRAS...')
            word1=input('Ingrese una palabra o frase para su analisis:')
        elif opcion==3:
            print('...BIENVENIDO AL MODULO DE APLICACION CON DATOS...')
        elif opcion==4:
            print('Un placer automatizar sus procesos!!!')
            exit()
        else:
            print('Ingrese una opcion valida!!!')

#INICIO DEL PROGRAMA
if __name__=='__main__':
    run()

