class cuenta:
    def __init__(self, nombre, numero_cuenta, saldo ):
        self.nombre_titular = nombre
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def deposito(self,cant_deposito):
        self.saldo=self.saldo+cant_deposito
        return self.saldo
    
    def retirar(self, cantidad_retiro):
        if self.saldo >= cantidad_retiro:
            self.saldo= self.saldo-cantidad_retiro
            return self.saldo
        
        else:
            print("no hay dinero para ese retiro")
            return -1
    def consultar(self):
        return self.saldo
    
#programa principal 
lista_cuentas =[]

print("bienvenido al banco")
while True:
    print("ingrese la opcion deseada")
    print("1. crear cuenta")
    print("2. depositar")
    print("3. retirar")
    print("4. consultar saldo ")
    print("0. salir")
    
    opcion=int(input())
    if opcion== 1:
        nombre =input("ingrese su nombre")
        numero_cuenta = int(input())
        nueva_cuenta = cuenta(nombre, numero_cuenta)
        lista_cuentas.append(nueva_cuenta)
        print("cuenta creada exitosamente")

    elif opcion ==2:
        numero_cuenta= int(input("ingrese nuemro de cuenta "))
        for cuenta in lista_cuentas:
            if cuenta.numero_cuenta== numero_cuenta:
                cantidad= float(input("ingrese la cantidad a depositar"))
                nuevo_saldo= cuenta.depositar(cantidad)
                print("el nuevo saldo es", nuevo_saldo)
        if existe == False:
            print("cuenta no existe ")

    elif opcion ==3:
        numero_cuenta=int(input("ingrese numero de cuenta"))
        existe= False
        for cuenta in lista_cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                existe = True
                cantidad = float(input("ingrese la cantidad de retiro "))
                nuevo_saldo = cuenta.retirar(cantidad)

            if nuevo_saldo >=0:
                print("retiro exitoso. Su nuevo saldo es ", nuevo_saldo)
        if existe == False:
            print("cuenta no existente")

    elif opcion ==4:
        numero_cuenta = int(input("ingrese numero de cuenta"))
        existe = False
        for cuenta in lista_cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                existe = True
                print("su saldo es ", cuenta.consultar())

            if existe == False:
                print(" cuenta no existe")

    elif opcion ==0:
        print("hasta luego")
        break
    else:
        print("obcion ivalida")


         

    
            


