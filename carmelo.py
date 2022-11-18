# class Cliente:
#     def __init__ (self) -> None:
#         self.nombre=input('dime el nombre del cliente: ')
#         self.ciudad=input('dime la ciudad del cliente: ')
#         self.facturacion=input('dime la facturacion del cliente: ')
#     def confirmarRegistro(self):
#         print(f'Se ha guardado: {self.nombre}')



class Trabajador:
    def __init__(self) -> None:
        self.nombre=input('dime el nombre del trabajador: ')
        self.ciudad=input('dime la ciudad del trabajador: ')
        self.nss=input('dime el número de seguridad social del trabajador: ')
    def confirmarTrabajador(self):
        print(f'Se ha guardado la ficha de: {self.nombre} -(nss): {self.nss} / {self.ciudad}')
    def calcularNeto(self):
        self.bruto=float(input('Dime tu salario: '))
        self.pagas=float(input('Dime el número de pagas: '))
        neto=(self.bruto * 0.8)/self.pagas
        print(f'El trabajador {self.nombre} tendrá un salario neto de: {neto}')
# cliente1=Cliente()
# cliente1.confirmarRegistro()


# #dar alta 3 clientes
# cliente10=Cliente()
# cliente11=Cliente()
# cliente12=Cliente()j

##los clientes estan en el programa, memoria
#solucion: persistencia de datos: insert tabla clientes


#clientes habituales : tabla de clientes
# clientesh=[cliente1,cliente10,cliente11,cliente12]
# for cliente in clientesh:
#     cliente.confirmarRegistro()

#tu equipo de trabajo tendrá 4 trabajadores
#los das de alta y muestra su nombre y nss
trabajador1=Trabajador()
# trabajador10=Trabajador()
# trabajador11=Trabajador()
# trabajador12=Trabajador()

empresa=[trabajador1]#trabajador10,trabajador11,trabajador12]
for trabajador in empresa:
    trabajador.confirmarTrabajador()

    
#nuestra aplicación va a tener una funcionalidad para que el trabajador pueda calcular su salario.
#Le vamos a pedir sólamente el salario bruto y el número de pagas  
#con eso le mostramos el salario neto mensual.
#el cálculo (me lo invento) sería : bruto-20% bruto / 12 o 14 pagas
empresa=[trabajador1]#trabajador10,trabajador11,trabajador12]
for trabajador in empresa:
    trabajador.calcularNeto()