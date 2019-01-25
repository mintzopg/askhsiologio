import operator
from functools import reduce

def organizingContainers(container):
    n = len(container)
    container_tot_balls = []
    type_tot_balls = []
    for c in container:
        container_tot_balls.append(reduce(operator.add, c))

    ts = 0
    for y in range(n):
        for x in range(n):
          ts += container[x][y]
        type_tot_balls.append(ts)
        ts = 0

    container_tot_balls.sort()
    type_tot_balls.sort()

    for a, b in zip(container_tot_balls, type_tot_balls):
        if a != b:
            return "Impossible"
    return "Possible"


if __name__ == "__main__":
    # container = [[1, 3, 1], [2, 1, 2], [3, 3, 3]]
    container = [[0, 2, 1], [1, 1, 1], [2, 0, 0]]
    print(organizingContainers(container))
