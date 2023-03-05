
#  Algoritmo para establecer la lista de cuadrados perfectos inferiores a un límite dado


def cuadrados_perfectos(limite):
    cuadrados = []
    num_impar = 1
    suma = 0
    while suma < limite:
        cuadrados.append(suma)
        num_impar += 2
        suma += num_impar
    return cuadrados


#  Algoritmo para calcular la raíz cuadrada entera de un número entero

def raiz_entera(n):
    if n == 0:
        return 0
    r = 1
    while r*r <= n:
        r += 1
    return r-1

def main():
    limite = 2000
    cuadrados = cuadrados_perfectos(limite)
    print("Cuadrados perfectos inferiores a", limite, ":", cuadrados)
    for n in cuadrados:
        raiz = raiz_entera(n)
        print("La raíz cuadrada entera de", n, "es", raiz)

main()



