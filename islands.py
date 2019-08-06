# 0 = sea
# 1 = land
# count islands in the matrix

#01
#10 

#0 0 0 0 0 0 0
#0 1 1 0 0 0 0
#0 1 0 0 1 0 0
#0 1 1 0 1 1 1
#0 0 0 0 1 1 0
#0 0 0 0 0 0 0

LAND = 1
existing_island = 0

islands = {}

def generate_adjacent_neighbors(x, y):
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 and j != 0:
                neighbours.append([x + i, y + j])
            
    return neighbours
    
def get_all_in_island(matrix, x, y, nodes=()):
    neighbours = generate_adjacent_neighbors(x, y)
    
    for n in neighbours:
        if n not in nodes and matrix[n[0], n[1]] == LAND:
            nodes.append(get_all_in_island(matrix, x, y))
    
    return nodes
    
def count_islands(matrix):
    for i in range(0, matrix):
        for j in range(0, matrix[i]):
            if matrix[i][j] == LAND:
                collect_adjacent_land(matrix, i, j)
    
def collect_adjacent_land(matrix, x, y):
    if str([x, y]) in islands:
        return

    nodes = get_all_in_island(x, y)
    add_to_existing = False
    
    for n in nodes:
        if not n in islands:
            islands[str(n)] = 1
            add_to_existing = True
    
    if add_to_existing:
        existing_islands += 1
        