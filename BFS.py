import os

base_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_path, "Real_distance_between_cities.txt")) as data:
    real_distances = eval(data.read())

with open(os.path.join(base_path, "Coordinates.txt")) as data:
    coordinates = eval(data.read())


# start city -> end city
def Bfs(start, goal):
    # we want to travers city level by level, so we use stack based on (first in first out)
    # paths
    queue = [[start]]

    # make it to check when city is visited or not
    visited = []

    while queue:
        # find first path we constructed and remove it from queue
        path = queue.pop(0)

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
        adjacent_nodes = real_distances.get(node, [])
        for node2 in adjacent_nodes:
            # construct new path by copying path and add to it neighbor nodes
            new_path = path.copy()
            new_path.append(node2)
            # add new path to the top of queue
            queue.append(new_path)
