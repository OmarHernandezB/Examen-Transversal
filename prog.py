from func import *

op = 0
productos = []

while True:
    print("""1)Agregar producto
2)Calcular la suma de los precios de los productos
3)Calcular el promedio de los precios de los productos
4)Salir""")
    
    op = int(input("Ingrese la opción que necesite: "))
    try:
        if op == 1:
            agregar_producto(productos)
        elif op == 2:
            calcular_suma_precios(productos)
        elif op == 3:
            calcular_promedio_productos(productos)
        elif op == 4:
            guardar_productos_csv(productos)
            print("Hasta luego")
            break
    except ValueError:
        print("Favor ingrese un valor numérico")    


    