import os

# get file distance
base_path = os.path.dirname(os.path.abspath(__file__))

# read distance as a graph (dictionary)
with open(os.path.join(base_path, 'Real_distance_between_cities.txt')) as data:
    cities_real_distance = eval(data.read())

# algorithm based on straight forward path

# start city -> end city
def DFS(start, goal):
    # we want to travers nodes as we can, so we use stack based on (last in first out)
    # paths
    stack = [[start]]
    visited = []

    while stack:
        # find last path we constructed and remove it from stack
        path = stack.pop(-1)

        # find last node in path
        node = path[-1]

        # check last node is visited or not
        if node in visited:
            continue

        # add node to visited list
        visited.append(node)

        # check if node is goal or not
        if node == goal:
            return path

        # find neighbors cities from last node
        adjacent_nodes = cities_real_distance.get(node, [])
        for node2 in adjacent_nodes:
            # construct new path by copying path and add to it neighbor nodes
            new_path = path.copy()
            new_path.append(node2)
            # add new path to the top of stack
            stack.append(new_path)
