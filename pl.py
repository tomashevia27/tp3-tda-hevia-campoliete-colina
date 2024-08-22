
import pulp

IDX_HAB = 1

# Modelo de programación lineal:
# 
# Variables
# 
# . X𝑖,𝑗 el maestro 𝑖 está en el grupo 𝑗
#
# Restricciones
#
# . ∑𝑖 X𝑖,𝑗 = 1 ∀𝑖 (cada maestro debe estar asignado a un grupo y sólo un grupo)
# . ∑𝑗 X𝑖,𝑗 >= 1 ∀𝑗 (cada grupo debe tener al menos un maestro asignado, no puede haber grupos vacíos)
# . ∑𝑖 X𝑖,𝑗max * x𝑖 >= ∑𝑖 X𝑖,𝑗 * x𝑖 ∀𝑗!=𝑗max (hay un grupo Z cuya suma de habilidades es mayor)
# . ∑𝑖 X𝑖,𝑗min * x𝑖 <= ∑𝑖 X𝑖,𝑗 * x𝑖 ∀𝑗!=𝑗min (hay un grupo Y cuya suma de habilidades es menor)
# 
# Función objetivo a minimizar
# 
# . ∑𝑖 Z𝑖 - ∑𝑖 Y𝑖 = ∑𝑖 X𝑖,𝑗max * x𝑖 - ∑𝑖 X𝑖,𝑗min * x𝑖
# 

def pl(maestros, k):

    n = len(maestros)
    x_i = [maestro[IDX_HAB] for maestro in maestros]

    vars = []
    for i in range(n):
        fila_vars = []
        for j in range(k):
            nombre_var = "X" + str(i) + str(j)
            fila_vars.append(pulp.LpVariable(nombre_var, cat="Binary"))
        vars.append(fila_vars)

    problem = pulp.LpProblem("Problema_de_la_Tribu_del_Agua", pulp.LpMinimize)

    # ∑𝑖 X𝑖,𝑗 = 1 ∀𝑖 (cada maestro debe estar asignado a un grupo y sólo un grupo)
    for i in range(n):
        fila_vars = vars[i]
        problem += pulp.LpAffineExpression([(var, 1) for var in fila_vars]) == 1

    ecuaciones = []

    # ∑𝑗 X𝑖,𝑗 >= 1 ∀𝑗 (cada grupo debe tener al menos un maestro asignado, no puede haber grupos vacíos)
    for j in range(k):
        columna_vars = []
        for i in range(n):
            columna_vars.append(vars[i][j])
        problem += pulp.LpAffineExpression([(var, 1) for var in columna_vars]) >= 1
        ecuaciones.append(pulp.LpAffineExpression([(var, x_i[i]) for i, var in enumerate(columna_vars)]))

    i = 1
    while i < k:
        problem += ecuaciones[0] >= ecuaciones[i]
        i += 1
    i = 0
    while i < k - 1:
        problem += ecuaciones[k-1] <= ecuaciones[i]
        i += 1

    problem += (ecuaciones[0] - ecuaciones[k-1]) # Función objetivo
    
    problem.solve()

    values = []
    for i in range(n):
        values.append(list(map(lambda Xij: pulp.value(Xij), vars[i])))

    minimo = 0
    grupos = []
    for j in range(k):
        suma_grupo = 0
        grupo=set()
        for i in range(n):
            suma_grupo += values[i][j] * x_i[i]
            if values[i][j]:
                grupo.add(maestros[i])
        minimo += suma_grupo ** 2
        grupos.append(grupo)
    
    return int(minimo), grupos

    