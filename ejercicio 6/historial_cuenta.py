from functools import *
from itertools import *


'''
Ejercicio 6: 
Se quiere conservar el historial de los movimientos mensuales en una cuenta corriente.

1. Modificar el tipo CUENTA definido en el capítulo «Estructuras elementales» para conservar el rastro de los movimientos en una cuenta durante un mes.

2. Establecer el saldo a final de mes de una cuenta dada.

El saldo ya no es un atributo de la cuenta. Se obtiene recorriendo el historial mensual y anual que registra el importe del saldo de la cuenta para cada mes.

3. Rehacer las definiciones anteriores.

Una tabla clientes contiene las cuentas corrientes de un conjunto de clientes.

4. Determinar los clientes para los que la media de los importes de los movimientos es superior a una suma dada.

El ejercicio siguiente se resolverá por completo en el capítulo «Edición de un número».
'''

abrir_cuenta = input('¿Desea abrir una cuenta? (S/N): ')
movimientos = 0
saldo = 0
fecha = input('Introduzca la fecha: ')
cliente = input('Introduzca el nombre del cliente: ')


def operacion_cuenta():
    operacion = input('¿Desea ingresar o retirar dinero? (I/R): ')
    global movimientos, saldo
    if operacion == 'I':
        movimientos += 1
        ingreso = int(input('¿Cuanto dinero desea ingresar? '))
        saldo += ingreso
        print('Ingresando dinero... \n Ingreso realizado con éxito, el saldo actual es de: {} €'.format(saldo))
        return
    
    elif operacion == 'R': 
        movimientos += 1
        retiro = int(input('¿Cuanto dinero desea retirar? '))
        saldo -= retiro
        print('Retirando dinero... \n Retiro realizado con éxito, el saldo actual es de: {} €'.format(saldo))
        print('Retirando dinero...')
        return
    
    else:
        print('Opción no válida')
        return


def abrir_cuenta_corriente():
    if abrir_cuenta == 'S':
        print('Abriendo cuenta...\n')
        print('Cuenta abierta con éxito\n')
        operacion_cuenta()
        return

    elif abrir_cuenta == 'N':
        print('Cerrando programa...\n')
        print('Programa cerrado con éxito')
        return
    
        
    
    else:
        print('Opción no válida')
        return


#  hago una funcion que guarde el historial de los movimientos mensuales realizados en una cuenta corriente y que me devuelva el saldo a final de mes
#  en un nuevo archivo creado  con el nombre del cliente y el mes en el que se realizó el movimiento 

def historial_cuenta():
    historial = open('historial.txt', 'w')
    historial.write('Movimientos realizados en la cuenta: \n')
    historial.write('Cliente: {} \n'.format(cliente))
    historial.write('Fecha: {} \n'.format(fecha))
    historial.write('Movimiento: {} \n'.format(movimientos))
    historial.write('Saldo: {} \n'.format(saldo))
    historial.close()
    return


def main():
    abrir_cuenta_corriente()
    historial_cuenta()

main()
