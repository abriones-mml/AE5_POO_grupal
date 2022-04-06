class OrdendeCompra():
    
    def __init__(self, id_ordencompra, producto, despacho):
        self.id_ordencompra = id_ordencompra
        self.producto = producto
        self.despacho = despacho
        
    def mostrar_orden(self, producto, cliente, vendedor, impuesto):
        
        if self.despacho:
            envio = 5000
        else:
            envio = 0
        total = producto.valor_neto + impuesto + envio
        print(f"Orden de compra Nº Serie: {self.id_ordencompra}\n")
        print(f"Cliente: {cliente.nombre} {cliente.apellido}\n")
        print(f"Vendedor: {vendedor.nombre} {vendedor.apellido} \n")
        print("Detalles de Compra:\n")
        print("{:25}{:10}{:10}{:10}{:10}".format("Nombre Producto", "Precio Neto", "Impuesto", "Despacho", "Total a Pagar"))
        print("_"*80)
        print("{:25}{:10}{:10}{:10}{:10}".format(producto.nombre, producto.valor_neto, impuesto, envio, total))
        