
class Alumno:
    nombre: str
    nota: int
    
    def __init__(self, nombre, nota): 
        self.nombre=nombre
        self.nota=nota
        
    def esAprobado(self) -> bool:
        if(self.nota>=5):
            return True
        else:
            return False
 
    def getDatos(self):
        aprobado: str = " y está suspendido"
        if(self.esAprobado()):
            aprobado = " y está aprobado"
            
        return "Alumno " + self.nombre + " con la nota " + str(self.nota) + aprobado



alumno = Alumno("Juanjo",3)
print(alumno.getDatos())
 
