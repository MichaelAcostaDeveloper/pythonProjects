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
        if val2==0:
            while val2==0:
                print("EL segundo valor debe ser distinto de cero: ")
                val2=float(input("Ingrese el segundo valor nuevamente: "))
            division=val1/val2
            return print("El cociente es: "+str(division)+".")
        else:
            division=val1/val2
            return print("El cociente es: "+str(division)+".")
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

