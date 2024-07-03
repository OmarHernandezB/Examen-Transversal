import csv
import random
      
def agregar_producto(productos):
    nom = input("Ingrese el nombre del producto: ")
    des = input("Ingrese la descripción del producto: ")
    pre = round(random.uniform(10,100),2)
    producto = {"nombre":nom,"descripcion":des,"precio":pre}
    productos.append(producto)
    print(f"Producto {nom} agregado con el precio {pre}")

def calcular_suma_precios(productos):
    suma = sum(producto["precio"]for producto in productos)
    print(f"la suma de todos los precios es {suma}")
        
def calcular_promedio_productos(productos):
    if productos:
        prom = sum(producto["precio"]for producto in productos)/ len(productos)
        print(f"El promedio de valor entre los productos es {prom}")      
    else:
        print("No hay productos para sumarse")

def guardar_productos_csv(productos,filename='productos.csv'):
    if productos:
        keys = productos[0].keys()
        with open(filename,'w', newline ='') as outpout_file:
            archivo = csv.DictWriter(outpout_file, fieldnames=keys)
            archivo.writeheader()
            archivo.writerows(productos)
        print(f"productos guardados en el archivo {filename}")
    else:
        print("No hay productos para guardarse")


