class Vendedor:
    
    def __init__(self, run, nombre, apellido, seccion, comision=0, empleado_de_mes=0, ventas = 0): 
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion= seccion
        self.__comision=comision
        self.empleado_del_mes=empleado_de_mes
        self.ventas = ventas

    def setComision(self,venta):
        self.__comision+=venta*0.05/100
        print(f"Comision por la compra realizada de {venta*0.5/100}")
        print(f"Usted lleva acumulado {self.__comision}.")
        return self.__comision
    
    def add_ventas(self):
        self.ventas += 1

    def vender(self, prod, cli):      
        var2 = int(prod.valor_neto+(prod.valor_neto*1.19/100))  #   valor a pagar x el cliente
        var = int(prod.valor_neto*0.5/100)  #comisión que se lleva el vendedor
        if prod.stock >= 1 and cli._Cliente__saldo >= var2:
            print(f"Compra Autorizada\nUsted venderá 1 unidad de {prod.stock} del producto {prod.nombre}")
            prod.stock -= 1
            print(f"El nuevo stock de {prod.nombre} es de {prod.stock} unidad(es).")            
            print(f"Comision por la compra realizada de ${var}")
            self.__comision += var
            self.add_ventas()
            print(f"Usted lleva acumulado ${self.__comision} en {self.ventas} ventas.")
            cli._Cliente__saldo -= var2 #se hace el descuento del saldo
        else: 
            print("Compra Rechazada")

    def __str__(self):
        return "{:<15}{:15}{:15}{:11}{:8}{:10}".format(self.run, self.nombre.capitalize(), self.apellido.capitalize(), self.seccion.capitalize(), self.ventas, self.__comision)