from clase5 import PlanAhorro
import csv 

def CargarListaDesdeArchi():
    lista=[]
    with open("untitled1.csv","r")as archivo:   
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            objeto=PlanAhorro(int(fila[0]),fila[1],fila[2],int(fila[3]))
            lista.append(objeto)
    return lista

def actualiza(p):
    for i in p:
        i.getInfo()
        nuevo=input("ingrese el nuevo valor para actualizar el anterior")
        i.setValor(nuevo)
        i.getInfo()
        
def BusquedaValorCuota(p):
    i=0
    valor=int(input("ingrese un valor para analizar"))
    while valor > p[i].valorCuota() and i<len(p):
        i+=1
    if i==len(p):
        print("no se encontro una cuota menor al ingresado")
    else:
        return p[i].getInfo()
    
def MostrarMontosLicitados(p):
    for auto in p:
        print("info del vehiculo: \n")
        auto.getInfo()
        print(f"monto a lisitar para el vehiculo es de {auto.MontoLicitar()}")
    
def ModificaCantCuotas(p):
    codigo=int(input("ingrese el codigo del plan a buscar"))
    i=0
    while codigo != p[i].getCodigo() and i<len(p):
        i+=1
        if i==len(p):
            print("no se encontro el codigo")
        else:
            cant=int(input("ingrese la cantidad de cuotas para modificar la anterior"))
            p[i].setCantCuotas(cant)
            p[i].getCantCuotas



def Menu(p):
    menuu=int(input("1. Actualizar el valor del vehículo de cada plan.  2. Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.\n 3. Mostrar el monto que se debe haber pagado para licitar el vehículo \n 3. o el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar.\n 4.Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar.\n0. Salir"))
    while menuu != 0:
        if menuu ==1:
            actualiza(p)
        elif menuu==2:
            BusquedaValorCuota(p)
        elif menuu==3:
            MostrarMontosLicitados(p)
        elif menuu==4:
            ModificaCantCuotas(p)
        else:
            print("codigo erroneo volver a ingresar")
            menuu=int(input("1. Actualizar el valor del vehículo de cada plan.  2. Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.\n 3. Mostrar el monto que se debe haber pagado para licitar el vehículo \n 3. o el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar.\n 4.Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar.\n0. Salir"))
        menuu=int(input("1. Actualizar el valor del vehículo de cada plan.  2. Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.\n 3. Mostrar el monto que se debe haber pagado para licitar el vehículo \n 3. o el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar.\n 4.Dado el código de un plan, modificar la cantidad cuotas que debe tener pagas para licitar.\n0. Salir"))
    
