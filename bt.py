
IDX_HAB = 1

def bt(maestros,k,estan_ordenados,minimo_greedy=float('inf')):
    maestros_ord = maestros
    if not estan_ordenados:
        maestros_ord=sorted(maestros,key=lambda maestro: maestro[IDX_HAB],reverse=True)
    grupos_aux = [set() for _ in range(k)]
    grupos_sol = [set() for _ in range(k)]
    suma_grupos = [0 for _ in range(k)]
    minimo = [minimo_greedy]

    _bt(maestros_ord,k,0,grupos_aux,grupos_sol,suma_grupos,minimo,0)
    return minimo[0],grupos_sol

def actualizar(grupos_sol, grupos_aux):
    for i in range(len(grupos_aux)):
        grupos_sol[i].clear()
        grupos_sol[i].update(grupos_aux[i])

def _bt(maestros,k,i,grupos_aux,grupos_sol,suma_grupos,minimo,cuadrados):
    if i == len(maestros):
        if cuadrados <= minimo[0]:
            minimo[0] = cuadrados
            actualizar(grupos_sol,grupos_aux)
        return

    if cuadrados >= minimo[0] or suma_grupos.count(0)>len(maestros)-i:
        return

    for j in range(k):
        grupos_aux[j].add(maestros[i])
        nueva_suma_grupo = suma_grupos[j] + maestros[i][IDX_HAB]
        nuevos_cuadrados = cuadrados - (suma_grupos[j] ** 2) + (nueva_suma_grupo ** 2)
        suma_grupos[j] = nueva_suma_grupo
        _bt(maestros,k,i+1,grupos_aux,grupos_sol,suma_grupos,minimo,nuevos_cuadrados)
        grupos_aux[j].remove(maestros[i])
        suma_grupos[j] -= maestros[i][IDX_HAB]
        if suma_grupos[j] == 0:
            return