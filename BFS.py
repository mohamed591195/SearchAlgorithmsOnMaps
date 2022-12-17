import os

base_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_path, "Real_distance_between_cities.txt")) as data:
    real_distances = eval(data.read())

with open(os.path.join(base_path, "Coordinates.txt")) as data:
    coordinates = eval(data.read())


# start city -> end city
def Bfs(start, goal):
    queue = [[start]]
    visited = []

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            return path
        else:
            adjacent_nodes = real_distances.get(node, [])
            for node2 in adjacent_nodes:
                new_path = path.copy()
                new_path.append(node2)
                queue.append(new_path)



