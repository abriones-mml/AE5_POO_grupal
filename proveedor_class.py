class Proveedor:
    
    def __init__(self, rut, nombre, razon, pais, juridica):
        self.rut=rut
        self.nombre_legal=nombre
        self.razon_social=razon
        self.pais=pais
        self.juridica=juridica
    
    # Método para obtener en pantalla un string con los datos del proveedor   
    def __str__(self):
        return "{:15}{:25}{:25}{:15}{:15}".format(self.rut, self.nombre_legal.title(), self.razon_social, self.pais, self.juridica)
        
    #def mostrar_proveedores():  #NO FUNCIONA
    #    for key in proveedores:
    #        print(proveedores[key])


"""
#Creacion de objetos de proveedores
prov1= Proveedor("72635988-7", "Danilo Mardones", "Adidas_SA", "Chile", "Juridica")
prov2= Proveedor("66359188-7", "Ricardo Gonzalez", "Foster_SA", "Chile", "Juridica")
prov3= Proveedor("75635988-8", "Vanesa Saldivar", "Phillips_sa", "Chile", "Juridica")
prov4= Proveedor("69635988-3", "Fernando Perez", "Costa", "Chile", "Juridica")
prov5= Proveedor("77635988-5", "Patricio Oliva", "Casillero del Diablo", "Chile", "Juridica")
#Creación de un diccionario con los objetos proveedores
proveedores={"1":prov1, "2":prov2, "3":prov3, "4":prov4, "5":prov5}




"""