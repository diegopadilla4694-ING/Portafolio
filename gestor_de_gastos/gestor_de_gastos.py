
class venta_del_mes:
    def __init__(self, Fecha, producto, precio):
        self.Fecha = Fecha
        self.producto = producto
        self.precio = precio

        self.tabla = [ Fecha, producto, precio]


Ventas = []
print("---------GESTOR DE CUENTAS---------")
while True:

     Fecha = input("Ingrese fecha (dd/mm/aaaa): ")
     producto = input("Ingrese producto: ")
     precio_string = (input("Ingrese precio: "))

     clase = venta_del_mes(Fecha, producto, precio)
     print(clase.tabla)
     Ventas.append(clase.tabla)

     if not Fecha:
        break
     
     if not producto:
        break
         
     if not precio_string:
        break
     
     try:
         precio = float(precio_string)
     
     except ValueError:
         print("ERROR EL NUMERO DEBE DE SER UN NUMERO ENTERO O DECIMAL")
     


print(Ventas)

