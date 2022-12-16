from geopy.distance import geodesic
import os

base_path = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(base_path, 'Real_distance_between_cities.txt')) as data:

    cities_real_distance=eval(data.read())

with open(os.path.join(base_path, "Coordinates.txt")) as coordinates_data :
    cities_coordinate=eval(coordinates_data.read())

def calc_estimated(start, end):
    start=(cities_coordinate[start][0],cities_coordinate[start][1])
    end= (cities_coordinate[end][0],cities_coordinate[end][1])
    return geodesic(start,end).km


def A_star(start,goal):
    visited=[]
    queue=[[(start,0)]]

    def path_cost(path):

        g_cost = 0

        for (node, cost) in path:
            g_cost += cost

        last_node = path[-1][0]

        h_cost = calc_estimated(last_node, goal)
        f_cost = g_cost + h_cost

        return f_cost, last_node

    while queue:
        queue.sort(key=path_cost)
        path=queue.pop(0)
        node=path[-1][0]
        
        if node in visited:
            continue
        visited.append(node)

        if node==goal:
            return path
            
        else :
            adjacent_nodes=cities_real_distance[node]

            for node2 in adjacent_nodes:
                new_path=path.copy()
                new_path.append((node2,adjacent_nodes[node2]))
                queue.append(new_path)

# path=[]

# print(A_star)
# for node in A_star(start, goal):
#    path.append(node[0])

# print(path)