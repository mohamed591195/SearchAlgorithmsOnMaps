import os

base_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_path, 'Real_distance_between_cities.txt')) as data:
    cities_real_distance=eval(data.read())

def DFS(start,goal):
    path=[]
    stack=[]
    visited=[]
    stack.append(start)

    while stack:
        current_node=stack.pop(-1)

        if current_node  in visited:
            continue

        path.append(current_node)
        visited.append(current_node)

        if current_node==goal :
            return path
        else:
            for next_node in cities_real_distance[current_node]:
                stack.append(next_node)



