import sys
sys.path.append('../')
from lector_archivos import leer_archivo
from bt import bt
from pl import pl
from greedy import greedy
from greedy2 import greedy2
from time import time

LIM_INF_K=4
LIM_SUP_K=19
LIM_INF_N=2
LIM_SUP_N=11

def generar_mediciones():
    nombre_archivo,nombre_funcion,nombre_de_caso = sys.argv[1],sys.argv[2],sys.argv[3]

    if nombre_de_caso == "K":
        lim_inf, lim_sup = LIM_INF_K, LIM_SUP_K
    elif nombre_de_caso == "N":
        lim_inf, lim_sup = LIM_INF_N, LIM_SUP_N
    
    with open(nombre_archivo,'w') as file:
        file.write("Cantidad_de_elementos,Media_de_tiempo_de_ejecucion,Resultado_minimo_encontrado\n")

        for i in range(lim_inf,lim_sup):
            suma_de_tiempos=0
            
            if nombre_de_caso == "K":
                maestros,k=leer_archivo("../MAS_TESTS/K-Fijo/"+str(i)+"_4.txt")
            elif nombre_de_caso == "N":
                maestros,k=leer_archivo("../MAS_TESTS/N-Fijo/17_"+str(i)+".txt")

            if nombre_funcion == "bt":
                for j in range(3):    
                    minimo_greedy,_=greedy(maestros,k,estan_ordenados=False)                
                    inicio=time()
                    minimo,_ = bt(maestros,k,False,minimo_greedy)
                    fin=time()
                    suma_de_tiempos+=(fin-inicio)*1000
                file.write(str(i)+","+str(suma_de_tiempos/3)+","+str(minimo)+"\n")

            elif nombre_funcion == "greedy":
                for j in range(5):
                    inicio=time()
                    minimo,_ = greedy(maestros,k,estan_ordenados=False)
                    fin=time()
                    suma_de_tiempos+=(fin-inicio)*1000
                file.write(str(i)+","+str(suma_de_tiempos/5)+","+str(minimo)+"\n")
                
            elif nombre_funcion == "greedy2":
                for j in range(5):
                    inicio=time()
                    minimo,_ = greedy2(maestros,k,estan_ordenados=False)
                    fin=time()
                    suma_de_tiempos+=(fin-inicio)*1000
                file.write(str(i)+","+str(suma_de_tiempos/5)+","+str(minimo)+"\n")

            elif nombre_funcion == "pl":
                for j in range(3):
                    inicio=time()
                    minimo,_ = pl(maestros,k)
                    fin=time()
                    suma_de_tiempos+=(fin-inicio)*1000
                file.write(str(i)+","+str(suma_de_tiempos/3)+","+str(minimo)+"\n")

generar_mediciones()