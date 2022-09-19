#Crear una lista de estudiante
"""
Create
Read
Update
Delete
"""
#cout<<"";
#public class
#pow.(5,2)
#using namespace std:
#std:: ""
class Estudiante:

    def __init__(self, cod, nom, ape, car, bec):
        self.Codigo = cod
        self.Nombres = nom
        self.Apellidos = ape
        self.Carrera = car
        self.Becado = bec #Becado sera un valor booleano
    
    def __str__(self):
        return f"""Codigo: {self.Codigo}
Nombres: {self.Nombres}
Apellidos: {self.Apellidos}
Carrera: {self.Carrera}
Beca: {self.Becado}
"""

class ListadoEst:

    def __init__(self):
        self.lista =[]
    
    def agregarElemento(self, dato):
        try:
            self.lista.append(dato)
        except Exception as ex:
            print("Ocurrio un error al agregar: ", str(ex))
        
    def editarElemento(self, dato, pos):
        try:
            self.lista[pos]=dato
        except Exception as ex:
             print("Ocurrio un erro al editar:", str(ex))
    
    def eliminarElemento(self, pos):
        try:
            self.lista.remove(pos)
        except Exception as ex:
            print("Error al eliminar:", str(ex))
    
    def buscarElementos(self, nom):
        try:
            pos = 0
            for est in self.lista:
                
                if est.Nombres == nom:
                    print("Estudiante encontrado...")
                    return est, pos
            else:
                print("No se encontro...")
            pos+=1
        except Exception as ex:
            print("Error al buscar elemento:", str(ex))

    def buscarElemento(self, ape):
        try:
            pos = 0
            for est in self.lista:
                
                if est.Apellidos == ape:
                    print("Estudiante encontrado...")
                    return est, pos
            else:
                print("No se encontro...")
            pos+=1
        except Exception as ex:
            print("Error al buscar elemento:", str(ex))

    def buscarElementoss(self, car):
        try:
            pos = 0
            for est in self.lista:
                
                if est.Carrera == car:
                    print("Estudiante encontrado...")
                    return est, pos
            else:
                print("No se encontro...")
            pos+=1
        except Exception as ex:
            print("Error al buscar elemento:", str(ex))

