
IDX_HAB = 1

def greedy(maestros, k, estan_ordenados):
    maestros_ord = maestros
    if not estan_ordenados:
        maestros_ord = sorted(maestros, key=lambda maestro: maestro[IDX_HAB], reverse=True)
    grupos = [set() for _ in range(k)]

    i = 0
    while i < k:
        grupos[i].add(maestros_ord[i])
        i += 1

    while i < len(maestros_ord):
        grupo_min = min(grupos, key=lambda grupo: sum(hab for (_, hab) in grupo) ** 2)
        grupo_min.add(maestros_ord[i])
        i += 1

    return sum(sum(hab for (_, hab) in grupo) ** 2 for grupo in grupos), grupos