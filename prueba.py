class Implante:
    def __init__(self):
        self.__numeroSerie = 0
        self.__nombre = ""
        self.__paciente=""
        self.__fecha=""
        self.__medico=""
        self.__estadoImplante=""

    
    #setters
    def setNumeroSerie(self, numero):
        self.__numeroSerie = numero
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setPaciente(self,paciente):
        self.__paciente=paciente
    def setFecha(self,fecha):
        self.__fecha=fecha
    def setMedico(self,medico):
        self.__medico=medico
    def setEstado(self,estado):
        self.__estadoImplante=""
    
    
    #getters
    def getNumeroSerie(self):
        return self.__numeroSerie
    def getNombre(self):
        return self.__nombre
    def setNPaciente(self):
        return self.__paciente
    def getFecha(self):
        return self.__fecha
    def getMedico(self):
        return self.__medico
    def getEstado(self):
        return self.__estadoImplante

class Marcapasos(Implante):
    def __init__(self):
        super().__init__()
        self.__electrodos = 0
        self.__alambrico = ""
        self.__frecuencia_estimulacion = 0.0
    
    #setters
    def setElectrodos(self, electrodos):
        self.__electrodos = electrodos
    def setAlambrico(self, alambrico):
        self.__alambrico = alambrico
    def setFrecuencia(self, frecuencia):
        self.__frecuencia_estimulacion = frecuencia
    
    #getters
    def getElectrodos(self):
        return self.__electrodos
    def getAlambrico(self):
        return self.__alambrico
    def getFrecuencia(self):
        return self.__frecuencia_estimulacion

class Stend(Implante):
    def __init__(self):
        super().__init__()
        self.__longitud = 0.0
        self.__diametro = 0.0
        self.__material=""
    
    #setters
    def setLongitud(self, longitud):
        self.__longitud = longitud
    def setDiametro(self, diametro):
        self.__diametro = diametro
    def setMaterial(self, material):
        self.__material = material
    
    
    #getters
    def getLongitud(self):
        return self.__longitud
    def getDiametro(self):
        return self.__diametro
    def getMaterial(self):
        return self.__material

class ImplanteDental(Implante):
    def __init__(self):
        super().__init__()
        self.__forma = ""
        self.__sistemaFijacion = ""
        self.__material=""
        
    #setters
    def setForma(self, forma):
        self.__forma = forma
    def setSistemaF(self, sistema):
        self.__sistemaFijacion = sistema
    def setMaterial(self, material):
        self.__material = material
    
    #getters
    def getForma(self):
        return self.__forma
    def getSistemaFijacion(self):
        return self.__sistemaFijacion
    def getMaterial(self):
        return self.__material

class ImplanteRodillas(Implante):
    def __init__(self):
        super().__init__()
        self.__materiales = ""
        self.__tamaño = 0
        self.__tipoFijacion = ""

    #setters
    def setMateriales(self, material):
        self.__materiales = material
    def setTamaño(self, tamaño):
        self.__tamaño = tamaño
    def setTipoF(self, tipo):
        self.__tipoFijacion = tipo
    
    #getters
    def getMateriales(self):
        return self.__materiales
    def getTamaño(self):
        return self.__tamaño
    def getTipoF(self):
        return self.__tipoFijacion

class ImplanteCadera(Implante):
    def __init__(self):
        super().__init__()
        self.__materiales = ""
        self.__tamaño = 0
        self.__tipoFijacion = ""

    #setters
    def setMateriales(self, material):
        self.__materiales = material
    def setTamano(self, tamaño):
        self.__tamaño = tamaño
    def setTipoF(self, tipo):
        self.__tipoFijacion = tipo
    
    #getters
    def getMateriales(self):
        return self.__materiales
    def getTamaño(self):
        return self.__tamaño
    def getTipoF(self):
        return self.__tipoFijacion

class Sistema(Marcapasos, Stend, ImplanteDental, ImplanteRodillas, ImplanteCadera):
    def __init__(self):
        super().__init__()
        self.__diccImplantes = {}

    def setDiccImplantes(self, diccionario):
        self.__diccImplantes = diccionario

    def getDiccImplantes(self):
        return self.__diccImplantes

    def verificacion(self, numero):
        if self.__diccImplantes.get(numero) is not None:
            return True
        else:
            print("El numero de serie ingresado no esta asociado a ningun implante en el sistema")
            return False  

    def agregarImplante(self, numero_serie, implante):
        self.__diccImplantes[numero_serie] = implante

    def eliminarImplante(self, numero_serie):
        if self.verificacion(numero_serie):
            del self.__diccImplantes[numero_serie]
            return print(f"Se elimino correctamente el implante con numero de serie {numero_serie}")
        else:
            return print(f"No se pudo eliminar el implante con el numero de serie {numero_serie}")

    def editar_inf(self, numero_serie, implante):
        r = int(input("Ingrese si desea cambiar:\n1-Registros del paciente y asigancion y datos de implantes\n2.Datos del implante y Caracteristicas espacificas del implante "))

        if r == 1:
            d = int(input("Ingrese la instancia del implante que desea editar:\n1-Numero de serie\n2-nombre\n3-Paciente\n4-Fecha\n5-Medico\n6-Estado del implante"))
            if d == 1:
                valor = self.__diccImplantes.pop(numero_serie)
                a = int(input("Ingresar el nuevo numero de serie: "))
                self.__diccImplantes[a] = valor
            elif d == 2:
                a = input("Ingrese el nuevo nombre del implante: ")
                implante.setNombre(a)
            elif d == 3:
                a = input("Ingrese el nuevo nombre del paciente: ")
                implante.setPaciente(a)
            elif d == 4:
                a = input("Ingrese la fecha nueva de ingreso: ")
                implante.setFecha(a)
            elif d == 5:
                a = input("Ingresar el nombre del nuevo medico:")
                implante.setMedico(a)
            elif d == 6:
                a = input("Ingresar nuevo estado del implante: ")
                implante.setEstado(a)

        elif r == 2:
            if implante.getNombre() == "Marcapasos":
                o = int(input("Ingrese la opcion de cambio:\n1-#Electrodos\n2-Alambrico o inalambrico\n3-Frecuencia de estimulacion"))
                if o == 1:
                    a = int(input("Ingrese nuevo numero del electrodos: "))
                    implante.setElectrodos(a)
                elif o == 2:
                    a = input("Ingrese si es alambrico o inalambrico: ")
                    implante.setAlambrico(a)
                elif o == 3:
                    a = float(input("Ingrese el numero de frecuencia: "))
                    implante.setFrecuencia(a)

            elif implante.getNombre() == "Stend Coronario":
                f = int(input("Ingrese la caracteritica que desea editar:\n1-Longitud\n2-Diametro\n3-Material"))
                if f == 1:
                    a = float(input("Ingrese la nueva longitud: "))
                    implante.setLongitud(a)
                elif f == 2:
                    a = float(input("Ingrese el nuevo diametro: "))
                    implante.setDiametro(a)
                elif f == 3:
                    a = input("Ingrese el nuevo material : ")
                    implante.setMaterial(a)

            elif implante.getNombre() == "Implante Dental":
                f = int(input("Ingrese la caracteristica que desea editar:\n1-Forma\n2-Sistema de fijacion\n3-Material"))
                if f == 1:
                    a = input("Ingrese la nueva forma: ")
                    implante.setForma(a)
                elif f == 2:
                    a = input("Ingrese el nuevo sistema de fijacion: ")
                    implante.setSistemaF(a)
                elif f == 3:
                    a = input("Ingresar el nuevo material: ")
                    implante.setMaterial(a)

            elif implante.getNombre() == "Implante Rodilla" or implante.getNombre() == "Implante Cadera":
                f = int(input("Ingrese la caracteristica que desea editar:\n1-Materiales\n2-Tamaño\n3-Tipo de fijacion "))
                if f == 1:
                    a = input("Ingrese el nuevo material: ")
                    implante.setMateriales(a)
                elif f == 2:
                    a = int(input("Ingresar el nuevo tamaño: "))
                    implante.setTamaño(a)
                elif f == 3:
                    a = input("Ingrese el tipo de fijacion:")
                    implante.setTipoF(a)


def main():
    sistema = Sistema()  # Esto debería estar fuera del bucle while para evitar la re-creación en cada iteración
    marcapasos=Marcapasos()
    stend=Stend()
    implante_dental=ImplanteDental()
    implante_rodilla=ImplanteRodillas()
    implante_cadera=ImplanteCadera()
    sistema=Sistema()

    while True:
        menu = int(input("Ingrese la opcion que desea:\n1-Ingresar implante\n2-Eliminar\n3-Editar informacion\n4-Visualizar inventario completo\n"))

        if menu == 1:
            numero_serie=int(input("Ingresar numero de serie: "))
            n=int(input("Seleccione nombre del  implante: \n1-Marcapasos\n2-Stend coronario\n3-Implante dental\n4-Implante de rodilla\n5-Implante de cadera"))
            paciente=input("Ingresa nombre del paciente asociado al implante: ")
            fecha=input("Ingresar la fecha de ingreso: ")
            medico=input("Ingresar medico responsable: : ")
            estado=input("Ingresar el esatdo del implante: ")

            if n==1:   #Marcapasos
                nombre="Marcapasos"
                electrodos=int(input("Ingresar el numero de electrodos: "))
                alambrico=input("Ingresar si es alambrico o inalambrio: ")
                frecuencia_es=float(input("Ingresar frecuencia de estimulacion: "))
                
                #asignacion de atributos 
                marcapasos.setNumeroSerie(numero_serie)
                marcapasos.setNombre(nombre)
                marcapasos.setPaciente(paciente)
                marcapasos.setFecha(fecha)
                marcapasos.setMedico(medico)
                marcapasos.setEstado(estado)
                marcapasos.setElectrodos(electrodos)
                marcapasos.setAlambrico(alambrico)
                marcapasos.setFrecuencia(frecuencia_es)
                sistema.agregarImplante(numero_serie, marcapasos)
            
            elif n==2: #Stend coronario
                nombre="Stend Coronario"
                longitud=float(input("Ingresar la longitud del stend: "))
                diametro=float(input("Ingresar el diametro: "))
                material=input("Ingresar el material del stend: ")

                #Asignacion de atributos 

                stend.setNumeroSerie(numero_serie)
                stend.setNombre(nombre)
                stend.setPaciente(paciente)
                stend.setFecha(fecha)
                stend.setMedico(medico)
                stend.setEstado(estado)
                stend.setLongitud(longitud)
                stend.setDiametro(diametro)
                stend.setMaterial(material)
                sistema.agregarImplante(numero_serie, stend)
            
            elif n==3:  #Implante dental 
                nombre="Implante Dental"
                forma=input("Ingresar forma: ")
                sistema=input("Ingresar sistema de fijacion: ")
                material=input("Ingresar material: ")
                
                #Asignacion de atributos 
                implante_dental.setNumeroSerie(numero_serie)
                implante_dental.setNombre(nombre)
                implante_dental.setPaciente(paciente)
                implante_dental.setFecha(fecha)
                implante_dental.setMedico(medico)
                implante_dental.setEstado(estado)
                implante_dental.setForma(forma)
                implante_dental.setSistemaF(sistema)
                implante_dental.setMaterial(material)
                sistema.agregarImplante(numero_serie, implante_dental)
            
            elif n==4: #Implante Rodilla 
                nombre="Implante Rodilla"
                material=input("Ingresar material: ")
                tamaño=int(input("Ingresar tamaño: "))
                tipo=input("Ingresar tipo de fijacion: ")

                #Asignacion de atributos 
                implante_rodilla.setNumeroSerie(numero_serie)
                implante_rodilla.setNombre(nombre)
                implante_rodilla.setPaciente(paciente)
                implante_rodilla.setFecha(fecha)
                implante_rodilla.setMedico(medico)
                implante_rodilla.setEstado(estado)
                implante_rodilla.setMateriales(material)
                implante_rodilla.setTamaño(tamaño)
                implante_rodilla.setTipoF(tipo)
                sistema.agregarImplante(numero_serie,implante_rodilla)
            
            elif n==5: #Implante de cadera
                nombre="Implante Cadera"
                material=input("Ingresar material: ")
                tamaño=int(input("Ingresar tamaño: "))
                tipo=input("Ingresar tipo de fijacion: ")

                #Asignacion de atributos 
                implante_cadera.setNumeroSerie(numero_serie)
                implante_cadera.setNombre(nombre)
                implante_cadera.setPaciente(paciente)
                implante_cadera.setFecha(fecha)
                implante_cadera.setMedico(medico)
                implante_cadera.setEstado(estado)
                implante_cadera.setMateriales(material)
                implante_cadera.setTamaño(tamaño)
                implante_cadera.setTipoF(tipo)
                sistema.agregarImplante(numero_serie,implante_cadera)

        elif menu == 2:
            numero_serie = int(input("Ingrese el numero de serie del implante: "))
            sistema.eliminarImplante(numero_serie)

        elif menu == 3:
            numero_serie = int(input("Ingrese el numero de serie del implante: "))
            if sistema.verificacion(numero_serie):
                dispositivo = sistema.getDiccImplantes()
                objeto = dispositivo.pop(numero_serie)
                sistema.editar_inf(numero_serie, objeto)

        elif menu == 4:
            print("Inventario completo:", sistema.getDiccImplantes())


main()
