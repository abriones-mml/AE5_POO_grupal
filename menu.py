from limpiarconsola import *
from bodega_class import BodegaPrincipal
from sucursal_class import Sucursal
from proveedor_class import Proveedor
from producto_class import Producto
from cliente_class import Cliente
from vendedor_class import Vendedor

######### INSTANCIAMIENTO DE OBJETOS ################
a={"1":1000,"2":1000,"3":1000, "4":1000, "5":1000}
b={
    "1":2,
    "2":2,
    "3":1, 
    "4":2, 
    "5":2
    }
bodega=BodegaPrincipal("Arlegui 400 Viña del Mar", 5000, a)
sucursal=Sucursal("1 Norte 1400 Viña del Mar", 1000, b)

prov1= Proveedor("72635988-7", "Danilo Mardones", "Adidas_SA", "Chile", "Juridica")
prov2= Proveedor("66359188-7", "Ricardo Gonzalez", "Foster_SA", "Chile", "Juridica")
prov3= Proveedor("75635988-8", "Vanesa Saldivar", "Phillips_sa", "Chile", "Juridica")
prov4= Proveedor("69635988-3", "Fernando Perez", "Costa", "Chile", "Juridica")
prov5= Proveedor("77635988-5", "Patricio Oliva", "Casillero del Diablo", "Chile", "Juridica")
#Creación de un diccionario con los objetos proveedores
proveedores={"1":prov1, "2":prov2, "3":prov3, "4":prov4, "5":prov5}

zapatillas= Producto(20221, "zapatillas", "calzado", proveedores["1"].razon_social, sucursal.stock["1"], 40000,"blancas")
jeans= Producto(20222, "jeans", "vestuario",proveedores["2"].razon_social , sucursal.stock["2"], 30000, "azules")
audifonos= Producto(20223, "audifonos", "electrónica", proveedores["3"].razon_social,sucursal.stock["3"], 30000,"negros")
chocolates= Producto(20224, "bombones de chocolate", "confitería", proveedores["4"].razon_social, sucursal.stock["4"], 15000,"oscuro")
vino= Producto(20225, "botella de vino 1.5L","licores", proveedores["5"].razon_social, sucursal.stock["5"], 20000, "tinto")
#Creación de un diccionario con los productos
productos= {"1": zapatillas, "2": jeans, "3": audifonos, "4": chocolates, "5": vino}

liliana= Cliente(1,"Liliana","Garmendia","liligc@gmail.com","10/02/2021", 80000)
clara=Cliente(2,"Clara", "Campos", "clara@gmail.com", "10/01/2019", 60000)
antonia=Cliente(3,"Antonia", "Garmendia", "anto@gmail.com", "10/01/2022", 100000)
valentina=Cliente(4,"Valentina", "Pasten", "vale@gmail.com", "20/01/2018", 50000)
constanza=Cliente(5,"Constanza", "Campos", "cony@gmail.com", "05/01/2020", 30000)
#Creación de un diccionario con los clientes
clientes={"1":liliana,"2":clara, "3":antonia, "4":valentina, "5":constanza}

vend1= Vendedor(186541239, "Diego", "Brando", "Juguetería")
vend2= Vendedor(186561239, "Dio", "Brando", "Calzado")
vend3= Vendedor(186571239, "Didier", "Brando", "Vestuario")
vend4= Vendedor(186581239, "Darío", "Brando", "Tecnología")
vend5= Vendedor(186591239, "Dior", "Brando", "Librería")

vendedores={"1":vend1,"2":vend2, "3":vend3, "4":vend4, "5":vend5}

#k = input("key: ")
#bodega.despachar_producto(k, 50, sucursal)

#'''

###############################################################################
while True:
    limpiar()
    print("<<<<<< Menú Principal >>>>>>\n")
    print("[1] Bodegas.")
    print("[2] Ventas.")
    print("[3] Clientes.")
    print("[4] Salir.")
    
    op = int(input("\nSeleccione opción: "))
    
    if op == 1:
        
        while True:
            limpiar()
            print("<<<<<< Bodegas >>>>>>\n")
            print("[1] Gestión de Bodega Principal.")
            print("[2] Gestión de Sucursal.")
            print("[3] Ver Proveedores.")
            print("[4] Ver Productos.")
            print("[5] Volver al Menú Principal.")
        
            op1 = int(input("\nSeleccione opción: "))
        
            # 1.1 Bodega principal
            if op1 == 1:
                limpiar()
                print("<<<<<< Bodega Principal >>>>>>\n")
                print("[1] Ver Bodega Principal.")
                print("[2] Despachar productos a Sucursal.")
                print("[3] Abastecer productos.")
                print("[4] Volver al Menú de Bodegas.")
        
                op11 = int(input("\nSeleccione opción: "))
                
                # 1.1.1 Estado Bodega Principal
                if op11 == 1:
                    limpiar()
                    listprod = [0]*len(productos)
                    for i in range(len(productos)):
                        listprod[i] = productos[str(i+1)].nombre.capitalize()
                    print("       >>> Bodega Principal <<<")
                    print("{:<5}{:25}{:6}".format("ID", "Producto", "Stock"))
                    print("="*40)
                    bodega.mostrar_stock(listprod)
                    input()
                
                # 1.1.2 Despachar a sucursal
                if op11 == 2:
                    limpiar()
                    print("Productos a despachar:\n")
                    for key in productos:
                        print(f"[{key}]\t{productos[key].nombre.capitalize()}")
                    p = input("\nSeleccione producto: ")
                    n = int(input(f"\nIngrese número de unidades de {productos[p].nombre.capitalize()} (Stock: {productos[p].stock}) a despachar: "))
                
                    bodega.despachar_producto(p, n, sucursal)
                    productos[p].stock = sucursal.stock[p]
                    input()

                # 1.1.3 Abastecer bodega
                if op11 == 3:
                    limpiar()
                    print("Productos a abastecer:\n")
                    for key in productos:
                        print(f"[{key}]\t{productos[key].nombre.capitalize()}")
                    p = input("\nSeleccione producto: ")
                    n = int(input(f"\nIngrese número de unidades de {productos[p].nombre.capitalize()} a abastecer: "))
                
                    bodega.recepcionar_producto(p, n)
                    input()
        
                if op11 == 4:
                    break
            
            # 1.2 Sucursal   
            elif op1 == 2:
                limpiar()
                print("<<<<<< Sucursal >>>>>>\n")
                print("[1] Ver Sucursal.")
                print("[2] Despachar productos a Bodega Principal.")
                print("[3] Reponer stock.")
                print("[4] Volver al Menú de Bodegas.")
            
                op12 = int(input("\nSeleccione opción: "))
                
                # 1.2.1 Ver Sucursal == Ver stock productos
                if op12 == 1:
                    limpiar()
                    listprod = [0]*len(productos)
                    for i in range(len(productos)):
                        listprod[i] = productos[str(i+1)].nombre.capitalize()
                    print("       >>> Sucursal <<<")
                    print("{:<5}{:25}{:6}".format("ID", "Producto", "Stock"))
                    print("="*40)
                    sucursal.mostrar_stock(listprod)
                    input()
                
                # 1.2.2 Despachar a Bodega   
                if op12 == 2:
                    limpiar()
                    print("Productos a despachar:\n")
                    for key in productos:
                        print(f"[{key}]\t{productos[key].nombre.capitalize()}")
                    p = input("\nSeleccione producto: ")
                    n = int(input(f"\nIngrese número de unidades de {productos[p].nombre.capitalize()} a despachar: "))
                
                    sucursal.despachar_producto(p, n, bodega)
                    productos[p].stock = sucursal.stock[p]
                    input()
                
                # 1.2.3 Reponer stock
                if op12 == 3:
                    limpiar()
                    print("Productos para añadir stock de unidades:\n")
                    for key in productos:
                        print(f"[{key}]\t{productos[key].nombre.capitalize()}")
                    p = input("\nSeleccione producto: ")
                    n = int(input(f"\nIngrese número de unidades de {productos[p].nombre.capitalize()} a abastecer: "))
                
                    bodega.despachar_producto(p, n, sucursal)
                    productos[p].stock = sucursal.stock[p]
                    input()
                
                if op12 == 4:
                    break

            # 1.3 Ver proveedores
            elif op1 == 3:
                limpiar()
                print("Nuestros proveedores:\n")
                print("{:15}{:25}{:25}{:15}{:15}".format("RUN", "Nombre", "Razón Social", "País", "Personalidad"))
                print("="*93)
                for key in proveedores:
                    print(proveedores[key])
                input("\n")
            
            # 1.4 Ver info de productos    
            elif op1 == 4:
                limpiar()
                print("Nuestros productos:\n")
                print('{:15}{:25}{:18}{:11}{:15}'.format("SKU", "Nombre", "Categoría", "Stock", "Valor neto (CLP)"))
                print("="*90)
                for key in productos:
                    print(productos[key])
                input("\n")
                
            elif op1 == 5:
                break
        
    if op == 2:
        
        while True:
            limpiar()
            print("<<<<<< Ventas >>>>>>\n")
            print("[1] Ver Vendedores.")
            print("[2] Realizar Venta.")
            print("[3] Volver al Menú Principal.")
        
            op2 = int(input("\nSeleccione opción: "))

            if op2 == 1:
                limpiar()
                print("Equipo de vendedores:\n")
                print("{:<15}{:15}{:15}{:15}{:8}{:15}".format("RUN", "Nombre", "Apellido", "Sección", "Ventas", "Comisión (CLP)"))
                print("="*85)
                for key in vendedores:
                    print(vendedores[key])
                input("\n")
            
            elif op2 == 2:
                limpiar()
                print("Vendedores:\n")
                for key in vendedores:
                    print(f"[{key}]\t{vendedores[key].nombre} {vendedores[key].apellido}")
                v = input("\nSeleccione Vendedor: ")
                
                limpiar()
                print("Cliente:\n")
                for key in clientes:
                    print(f"[{key}]\t{clientes[key].nombre} {clientes[key].apellido}")
                c = input("\nSeleccione Cliente para venta: ")
                
                limpiar()
                print("Productos:\n")
                for key in productos:
                    print(f"[{key}]\t{productos[key].nombre.capitalize()}")
                p = input("\nSeleccione producto para venta: ")

                limpiar()
                vendedores[v].vender(productos[p], clientes[c])
                input()
                
            elif op2 == 3:
                break
            
    if op == 3:
        
        while True:
            limpiar()
            print("<<<<<< Clientes >>>>>>\n")
            print("[1] Ver Clientes.")
            print("[2] Volver al Menú Principal.")

            op3 = int(input("\nSeleccione opción: "))

            if op3 == 1:
                limpiar()
                print("Clientes registrados:\n")
                print("{:4}{:15}{:18}{:16}{:19}{:15}".format("ID", "Nombre", "Apellido", "E-Mail", "Fecha Registro", "Saldo [CLP]"))
                print("="*90)
                for key in clientes:
                    print(clientes[key])
                input("\n")
                
            elif op3 == 2:
                break

    if op == 4:
        break
limpiar()
print("Que tenga una buena jornada!.\n")
#'''