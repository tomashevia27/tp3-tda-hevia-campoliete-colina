
def leer_archivo(nombre_archivo):
    
    with open(nombre_archivo,"r") as file:
        file.readline()
        k=int(file.readline().rstrip())
        maestros=[]
        for linea in file:
            nombre_maestro, habilidad = linea.rstrip().split(', ')
            maestros.append((nombre_maestro, int(habilidad)))
    
    return maestros,k
