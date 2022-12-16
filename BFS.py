import os

base_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_path, "Real_distance_between_cities.txt")) as data:
    real_distances=eval(data.read())

with open(os.path.join(base_path, "Coordinates.txt")) as data:
    coordinates=eval(data.read())   


def Bfs(start, goal):
    path=[]
    queue=[]
    visited=[]

    queue.append(start)

    while queue:
        current_node=queue.pop(0)

        if current_node  in visited:
            continue

        path.append(current_node)
        visited.append(current_node)

        if current_node==goal :
            return path
        else:
            for next_node in real_distances[current_node]:
                queue.append(next_node)




