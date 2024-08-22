
from bt import bt
from pl import pl
from greedy import greedy
from greedy2 import greedy2
from lector_archivos import leer_archivo
from sys import argv
from time import time

IDX_NOM = 0
IDX_HAB = 1
IDX_ARCHIVO = 1
IDX_TECNICA = 2
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

def imprimir(grupos_sol,minimo,fin,inicio):
    for i in range(1, len(grupos_sol) + 1):
        print(RED + BOLD + 'Grupo ' + str(i) + ': ' + END, end='')
        print(", ".join([maestro[IDX_NOM] for maestro in grupos_sol[i-1]]))

    print(RED + BOLD + "Coeficiente: " + END + f"{minimo}")
    print(RED + BOLD + "Tiempo de ejecución: " + END + f"{(fin-inicio) * 1000} milisegundos")
    
def main():
    
    maestros, k = leer_archivo(argv[IDX_ARCHIVO])
    maestros_ord = sorted(maestros, key=lambda maestro: maestro[IDX_HAB], reverse=True)

    tecnica = argv[IDX_TECNICA]
    if tecnica == "greedy":
        inicio = time()
        minimo, grupos_sol = greedy(maestros_ord, k,True)
        fin = time()
    elif tecnica == "greedy2":
        inicio = time()
        minimo, grupos_sol = greedy2(maestros_ord, k,True)
        fin = time()
    elif tecnica == "bt":
        minimo_greedy, _ = greedy(maestros_ord, k, True)
        inicio = time()
        minimo, grupos_sol = bt(maestros_ord, k,True,minimo_greedy)
        fin = time()
    elif tecnica == "pl":
        inicio = time()
        minimo, grupos_sol = pl(maestros_ord, k)
        fin = time()
    
    imprimir(grupos_sol,minimo,fin,inicio)
    
main()