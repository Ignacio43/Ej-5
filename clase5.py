

class PlanAhorro:
    __cantCuotas=12
    __cantCuotasPagas=6
    def __init__(self,codigo:int,modelo,version,valor:int):
        self.__codigo=codigo
        self.__modelo=modelo
        self.__version=version
        self.__valor=valor
        
    @classmethod
    def getCantCuotas(cls):
        return cls.__cantCuotas
    
    @classmethod
    def getCantCuotasPagas(cls):
        return cls.__cantCuotasPagas

    @classmethod
    def setCantCuotas(cls,cant):
        cls.__cantCuotasPagas=cant
        
    def getInfo (self):
       return print(f"{self.__codigo} {self.__modelo} {self.__version} {self.__valor}")
   
    def setValor(self,valor):
        self.__valor=valor
    
    def getCodigo(self):
        return self.__codigo
    
    def valorCuota(self):
        return ((self.__valor/self.__cantCuotas + self.__valor * 0,10))
        
    def MontoALicitar(self):
        return self.__cantCuotasPagas*self.valorCuota