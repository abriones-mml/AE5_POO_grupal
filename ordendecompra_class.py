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
        print(f"Orden de compra Nº: {self.id_ordencompra}\n")
        print(f"Cliente: {cliente.nombre} {cliente.apellido}\n")
        print(f"Vendedor: {vendedor.nombre} {vendedor.apellido} \n")
        print("Detalles de Compra:\n")
        print("{:17}{:25}{:10}{:22}{:10}".format("Código Producto", "Detalle", "Unidades", "Precio Unitario", "Total"))
        print("="*80)
        print("{:<17}{:28}{:<11}{:<13}{:10}".format(producto.sku, producto.nombre, 1, producto.valor_neto, producto.valor_neto))
        print("_"*80)
        print("{:>69}{:10}".format("Subtotal:", producto.valor_neto))
        print("{:>69}{:10}".format("Despacho:", envio))
        print("{:>69}{:10}".format("IVA:", impuesto))
        print("{:>80}".format("_"*21))
        print("{:>69}{:10}".format("TOTAL:", total))