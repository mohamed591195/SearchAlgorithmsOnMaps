import os

# get file distance
base_path = os.path.dirname(os.path.abspath(__file__))

# read distance as a graph (dictionary)
with open(os.path.join(base_path, 'Real_distance_between_cities.txt')) as data:
    cities_real_distance = eval(data.read())

# algo based on straight forward pass


def DFS(start, goal):
    stack = [[start]]
    visited = []

    while stack:
        path = stack.pop(-1)
        node = path[-1]

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            return path
        else:
            adjacent_nodes = cities_real_distance.get(node, [])
            for node2 in adjacent_nodes:
                new_path = path.copy()
                new_path.append(node2)
                stack.append(new_path)
