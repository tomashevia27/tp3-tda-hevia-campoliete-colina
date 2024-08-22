def validador(maestros,k,grupos_sol,minimo,B):
    if len(grupos_sol) != k:
        return False

    if minimo > B:
        return False

    if len(maestros) != sum(len(grupo) for grupo in grupos_sol):
        return False

    for maestro in maestros:
        esta_en_sol = False
        for i in range(k):
            if maestro in grupos_sol[i]:
                esta_en_sol = True
                break
        if not esta_en_sol:
            return False

    return True
        

