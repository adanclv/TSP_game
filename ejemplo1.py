from itertools import permutations
import math

# Matriz de adyacencia ponderada
'''cost = [
    # A   B    C     D     E     F
    [0, 4, 5, 9999, 9999, 9999],  # A
    [4, 0, 11, 9, 7, 9999],  # B
    [5, 11, 0, 9999, 3, 9999],  # C
    [9999, 9, 9999, 0, 13, 2],  # D
    [9999, 7, 3, 13, 0, 6],  # E
    [9999, 9999, 9999, 2, 6, 0]  # F
]'''


cost = [
    [0, 15, 18, 9999, 22, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 24], # Urano
    [15, 0, 9999, 12, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 22], # Neptuno
    [18, 9999, 0, 12, 9999, 9999, 13, 9999, 9999, 9999, 9999, 12, 9999, 9999], # Tierra
    [9999, 12, 12, 0, 9999, 10, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999], # Venus
    [22, 9999, 9999, 9999, 0, 17, 9999, 21, 19, 9999, 9999, 9999, 9999, 9999], # Jupiter
    [9999, 9999, 9999, 10, 17, 0, 10, 12, 34, 36, 9999, 9999, 9999, 9999], # Mercurio
    [9999, 9999, 13, 9999, 9999, 10, 0, 18, 9999, 9999, 9999, 9999, 9999, 9999], #Marte
    [9999, 9999, 9999, 9999, 21, 12, 18, 0, 29, 9999, 31, 9999, 9999, 9999], #Saturno
    [9999, 9999, 9999, 9999, 19, 9999, 9999, 29, 0, 26, 9999, 9999, 9999, 33], # 9
    [9999, 9999, 9999, 9999, 9999, 36, 9999, 9999, 26, 0, 15, 9999, 9999, 9999], # 10
    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 31, 9999, 15, 0, 21, 9999, 9999], # 11
    [9999, 9999, 12, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 21, 0, 20, 9999], # 12
    [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 20, 0, 19], # 13
    [24, 22, 9999, 9999, 9999, 9999, 9999, 9999, 33, 9999, 9999, 9999, 19, 0] # 14
]

# Nombres de los nodos
nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'SS9', 'SS10', 'SS11', 'SS12', 'SS13', 'SS14']


# Función para calcular el costo de una ruta
def calcular_costo(ruta):
    costo_total = 0
    for i in range(len(ruta) - 1):
        nodo_actual = ruta[i]
        nodo_siguiente = ruta[i + 1]
        costo_arista = cost[nodos.index(nodo_actual)][nodos.index(nodo_siguiente)]
        if costo_arista == 9999:
            return math.inf  # Ruta inválida
        costo_total += costo_arista
    # Regresar al nodo de inicio
    costo_arista_final = cost[nodos.index(ruta[-1])][nodos.index(ruta[0])]
    if costo_arista_final == 9999:
        return math.inf  # Ruta inválida
    costo_total += costo_arista_final
    return costo_total


# Función para resolver el TSP comenzando por un nodo específico
def tsp_fuerza_bruta(nodos, inicio):
    nodos_restantes = [nodo for nodo in nodos if nodo != inicio]  # Excluir el nodo de inicio
    mejor_ruta = None
    rutas = list()
    menor_costo = float('inf')

    for perm in permutations(nodos_restantes):
        ruta = [inicio] + list(perm) + [inicio] # Comenzar y terminar en el nodo de inicio
        costo = calcular_costo(ruta)
        if costo != math.inf:
            rutas.append(ruta)

        if costo < menor_costo:
            menor_costo = costo
            mejor_ruta = ruta

    return mejor_ruta, menor_costo, rutas

def are_adjacent(i, j):
    """Verifica si hay una línea de adyacencia entre los nodos i y j."""
    if cost[i][j] != 9999:  # Si el costo no es 9999, hay una conexión directa.
        return True
    return False

def dijkstra(inicio, destino):
    n = len(cost)  # Número de nodos
    distancias = [9999] * n  # Distancias iniciales (infinito)
    distancias[inicio] = 0  # La distancia al nodo de inicio es 0
    visitados = [False] * n  # Nodos visitados
    previo = [-1] * n  # Nodos previos para reconstruir la ruta

    for _ in range(n):
        # Encontrar el nodo no visitado con la distancia mínima
        u = -1
        for i in range(n):
            if not visitados[i] and (u == -1 or distancias[i] < distancias[u]):
                u = i

        # Si no se encuentra un nodo válido, terminar
        if distancias[u] == 9999:
            break

        visitados[u] = True

        # Actualizar las distancias de los nodos adyacentes
        for v in range(n):
            if cost[u][v] != 9999 and not visitados[v]:
                nueva_distancia = distancias[u] + cost[u][v]
                if nueva_distancia < distancias[v]:
                    distancias[v] = nueva_distancia
                    previo[v] = u

    # Reconstruir la ruta desde el destino hasta el inicio
    ruta = []
    u = destino
    while u != -1:
        ruta.append(u)
        u = previo[u]
    ruta.reverse()
    print(ruta)

    return ruta, distancias[destino]

def get_cost(i, j):
    costo = cost[i][j]
    return costo

if __name__ == '__main__':
    # Resolver el TSP comenzando por el nodo E
    inicio = 'C'
    destino = 'F'
    mejor_ruta, menor_costo, rutas = tsp_fuerza_bruta(nodos, inicio)
    ruta, costo = dijkstra(nodos.index(inicio), nodos.index(destino))

    if ruta:
        print(f"Ruta más corta de A a E: {ruta}")
        print(f"Costo total: {costo}")
    else:
        print("No existe una ruta válida de A a E.")

    if mejor_ruta:
        print("Rutas:", rutas)
        print(f"Mejor ruta comenzando por {inicio}: {mejor_ruta}")
        print(f"Costo mínimo: {menor_costo}")
    else:
        print("No existe una ruta válida que visite todos los nodos.")