import os

base_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_path, 'Real_distance_between_cities.txt')) as data:
    cities_distance=eval(data.read())

def calc_path_cost(path):
    cost=0

    for index in range(len(path)-1):
        cost+= cities_distance [path[index]] [path[index+1]]
    return cost

def uniform_cost(start , goal):

    visited=[]
    queue=[]
    queue = [[start]]

    while(queue):


        current_path = queue.pop(0)
    # print(current_path)
        current_city = current_path[-1]
        visited.append(current_city)

        if current_city == goal :
            return current_path

        for next_city,real_distance  in cities_distance[current_city].items():

            if next_city not in visited:
                visited.append(next_city)
                next_path=current_path.copy()
                next_path.append(next_city)
                queue.append(next_path)

        queue.sort(key=calc_path_cost)
    # print(queue)

# start_end_path = uniform_cost('shebin','ashmun')
# print("The total path form stard to end \n",start_end_path)