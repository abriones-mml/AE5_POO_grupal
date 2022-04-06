from bodega_class import BodegaPrincipal
from sucursal_class import Sucursal
from proveedor_class import Proveedor
from producto_class import Producto
from cliente_class import Cliente
from vendedor_class import Vendedor
from ordendecompra_class import OrdendeCompra

a={"1":1000,"2":1000,"3":1000, "4":1000, "5":1000}
b={"1":50, "2":50, "3":50, "4":50, "5":50}

bodega=BodegaPrincipal("Arlegui 400 Viña del Mar", 5000, a)
sucursal=Sucursal("1 Norte 1400 Viña del Mar", 1000, b)

# Proveedores
prov1= Proveedor("72635988-7", "Danilo Mardones", "Adidas_SA", "Chile", "Juridica")
prov2= Proveedor("66359188-7", "Ricardo Gonzalez", "Foster_SA", "Chile", "Juridica")
prov3= Proveedor("75635988-8", "Vanesa Saldivar", "Phillips_sa", "Chile", "Juridica")
prov4= Proveedor("69635988-3", "Fernando Perez", "Costa", "Chile", "Juridica")
prov5= Proveedor("77635988-5", "Patricio Oliva", "Casillero del Diablo", "Chile", "Juridica")

proveedores={"1":prov1, "2":prov2, "3":prov3, "4":prov4, "5":prov5}

# Productos
zapatillas= Producto(20221, "zapatillas", "calzado", proveedores["1"].razon_social, sucursal.stock["1"], 40000,"blancas")
jeans= Producto(20222, "jeans", "vestuario",proveedores["2"].razon_social , sucursal.stock["2"], 30000, "azules")
audifonos= Producto(20223, "audifonos", "electrónica", proveedores["3"].razon_social,sucursal.stock["3"], 30000,"negros")
chocolates= Producto(20224, "bombones de chocolate", "confitería", proveedores["4"].razon_social, sucursal.stock["4"], 15000,"oscuro")
vino= Producto(20225, "botella de vino 1.5L","licores", proveedores["5"].razon_social, sucursal.stock["5"], 20000, "tinto")

productos= {"1": zapatillas, "2": jeans, "3": audifonos, "4": chocolates, "5": vino}

# Clientes
liliana= Cliente(1,"Liliana","Garmendia","liligc@gmail.com","10/02/2021", 80000)
clara=Cliente(2,"Clara", "Campos", "clara@gmail.com", "10/01/2019", 60000)
antonia=Cliente(3,"Antonia", "Garmendia", "anto@gmail.com", "10/01/2022", 100000)
valentina=Cliente(4,"Valentina", "Pasten", "vale@gmail.com", "20/01/2018", 50000)
constanza=Cliente(5,"Constanza", "Campos", "cony@gmail.com", "05/01/2020", 30000)

clientes={"1":liliana,"2":clara, "3":antonia, "4":valentina, "5":constanza}

# Vendedores
vend1= Vendedor(186541239, "Diego", "Brando", "Juguetería")
vend2= Vendedor(186561239, "Dio", "Brando", "Calzado")
vend3= Vendedor(186571239, "Didier", "Brando", "Vestuario")
vend4= Vendedor(186581239, "Darío", "Brando", "Tecnología")
vend5= Vendedor(186591239, "Dior", "Brando", "Librería")

vendedores={"1":vend1,"2":vend2, "3":vend3, "4":vend4, "5":vend5}

ventas = 1

#k = input("key: ")
#bodega.despachar_producto(k, 50, sucursal)

#'''