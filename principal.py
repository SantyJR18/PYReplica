from clases import Estudiante as est, ListadoEst as lst

listaEst = lst()

def menu():
    print("1. Agregar Registro")
    print("2. Editar Registro")
    print("3. Eliminar Registro")
    print("4. Buscar por Nombre")
    print("5. Buscar por apellidos")
    print("6. Buscar por Carrera")
    print("7. Mostrar Registros")
    print("8. Mostrar becados y no becados")
    print("10. Salir")
    op = int(input("Escriba su opción: "))
    return op

def agregarRegistro():
    print("Agregar Datos del Estudiante")
    codigo = input("Código: ")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    carrera = input("Carrera: ")
    resp = input("Posee beca? SI -NO: ")
    if(resp.upper() == "SI"): beca = True
    
    else: beca = False
    estudiante = est(codigo, nombres, apellidos, carrera, beca)
    print(estudiante)
    listaEst.agregarElemento(estudiante)

def modificarRegistro():
    print("Editar Registro ")
    cod = input("Código: ")
    est, pos = listaEst.buscarElemento(cod)
    print(f"""Nombres Actual: {est.Nombres}
Apellidos actual: {est.Apellidos}
Carrera: {est.Carrera}
Beca: {est.Beca}""")
    print("Nuevos Datos")
    nuevoNombre = input("Nombres: ")
    nuevoApellidos = input("Apellidos: ")
    nuevaCarrera = input("Carrera: ")
    resp = input("Posee beca? SI -NO: ")
    if(resp.upper() == "SI"): nuevaBeca = True
    else: nuevaBeca = False
    newEst = est(cod, nuevoNombre, nuevoApellidos, nuevaCarrera, nuevaBeca)
    listaEst.editarElemento(newEst, pos)

def eliminarRegistro():
    print("Eliminar Registro")
    cod = input("Código: ")
    est, pos = listaEst.buscarElemento(cod)
    print(f"""Realmente desea eliminar el registro {est}""")
    resp = input("SI - NO")
    if resp.upper()=="SI":
        listaEst.eliminarElemento(pos)
    else:
        print("Operación cancelada")

def buscarRegistros():
    print("Buscar Registro")
    nom = input("Nombre: ")
    try:
        est, pos = listaEst.buscarElementos(nom)
 
        if est.Codigo != None:
            print(est)
    except:
        print("Todo bien segui adelante")

def buscarRegistro():
    print("Buscar Registro")
    ape = input("Apellido: ")
    try:
        est, pos = listaEst.buscarElemento(ape)
 
        if est.Codigo != None:
            print(est)
    except:
        print("Todo bien segui adelante")
        #num=num2
        #num!=num2
        #num<num2

def buscarRegistross():
    print("Buscar Registro")
    car = input("Carrera: ")
    try:
        est, pos = listaEst.buscarElementoss(car)
 
        if est.Codigo != None:
            print(est)
    except:
        print("Todo bien segui adelante")
def buscandoBecados():
    sys("cls")
    if lst.lista==[]:
        print("no hay estudiante registrado")
        sleep(1)
    else:
        becados=0
        nBecados=0
    for est in lst.lista:
     if est.beca==True:
        becados+=1
    else:
        nBecados +=1

        print(f"La cantidad de personas becadas es:",becados)
        print(f"La cantidad de personas no becadas es: ",nBecados)


"""def buscandoBecados():
    aprobado=0
for h in lista[]:
    if h>10:
        aprobado=aprobado+1
        print(aprobado)
    reprobado=0
for k in lista[]:
    if k<11:
        reprobado=reprobado+1
        print(reprobado)"""
def mostrarRegistros():
    for estudiante in listaEst.lista:
        print(estudiante)
        print("="*30)
def main():
    op = 0
    while(op!=10):
        op = menu()
        if op == 1: agregarRegistro()
        elif op == 2: modificarRegistro()
        elif op == 3: eliminarRegistro()
        elif op == 4: buscarRegistros()
        elif op == 5: buscarRegistro()
        elif op == 6: buscarRegistross()
        elif op == 7: mostrarRegistros()
        elif op == 8: buscandoBecados()
        elif op == 10: print("Ciao, ciao")
        else: print("Opcion no valida")

main()