

def pedir_numero():
    while True:
        try:
            n = int(input("Ingrese un número entero: "))
            return n
        except ValueError:
            print("No ingresó un número entero. Intente nuevamente.")


def pedir_base():
    while True:
        try:
            B = int(input("Ingrese la base: "))
            if B < 2:
                print("La base debe ser mayor o igual a 2.")
            else:
                return B
        except ValueError:
            print("No ingresó un número entero. Intente nuevamente.")

            
def transformar_a_base(n, B):
    resultado = []
    if n == 0:
        resultado.append(0)
    while n > 0:
        resto = n % B
        resultado.insert(0, resto)
        n //= B
    return resultado

def main():
    n = pedir_numero()
    B = pedir_base()
    resultado = transformar_a_base(n, B)
    print("El número {} en base {} es {}".format(n, B, resultado))

main()
