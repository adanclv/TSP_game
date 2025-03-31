# Python program to find the shortest possible route
# that visits every city exactly once and returns to
# the starting point

from itertools import permutations

def tsp(cost):
    best_solution = None
    # Number of nodes
    numNodes = len(cost)
    nodes = list(range(1, numNodes))

    minCost = float('inf')

    # Generate all permutations of the
    # remaining nodes
    for perm in permutations(nodes):
        currCost = 0
        currNode = 0

        # Calculate the cost of the current permutation
        for node in perm:
            currCost += cost[currNode][node]
            currNode = node

        # Add the cost to return to the starting node
        currCost += cost[currNode][0]

        # Update the minimum cost if the current cost
        # is lower
        if currCost < minCost:
            minCost = currCost
            best_solution = perm
        # minCost = min(minCost, currCost)

    return minCost, list(best_solution)


if __name__ == "__main__":

    cost = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    cost = [
        # A   B   C   D   E   F   G
        [0, 5, 0, 2, 0, 0, 0],  # A
        [5, 0, 3, 0, 1, 0, 0],  # B
        [0, 3, 0, 0, 0, 4, 0],  # C
        [2, 0, 0, 0, 6, 0, 3],  # D
        [0, 1, 0, 6, 0, 2, 1],  # E
        [0, 0, 4, 0, 2, 0, 5],  # F
        [0, 0, 0, 3, 1, 5, 0]  # G
    ]

    res, sol = tsp(cost)
    print(res, sol)
