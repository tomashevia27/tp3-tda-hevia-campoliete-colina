
IDX_HAB = 1

def greedy2(maestros, k, estan_ordenados):

    maestros_ord = sorted(maestros, key=lambda maestro: maestro[IDX_HAB], reverse=True)
    grupos = [set() for _ in range(k)]
    
    for maestro in maestros_ord:
        grupo_menor_cantidad=min(grupos, key=lambda grupo: len(grupo))
        grupo_menor_cantidad.add(maestro)
        
    return sum(sum(hab for _, hab in grupo) ** 2 for grupo in grupos), grupos