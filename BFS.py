import os

base_path = os.path.dirname(os.path.abspath(_file_))

with open(os.path.join(base_path, "Real_distance_between_cities.txt")) as data:
    real_distances=eval(data.read())

with open(os.path.join(base_path, "Coordinates.txt")) as data:
    coordinates=eval(data.read())   

# start city to  end city
def Bfs(start, goal):
    queue=[[start]]#aqueue of lists
    visited=[]#list of the visited elements
#loop while the queue is not empty
    while queue:
        
        #the path equal the last list in the queue
        path = queue.pop(0)
        node = path[-1]#node equal the last element in the path
   
        if node  in visited:
            continue

        visited.append(node)

        if node==goal :
            return path
        else:
            
            #all the adjacents of the last node
            adjacent_nodes = real_distances.get(node,[])
            
            for node2 in adjacent_nodes:
                #add every adjacent to the path and push the path to the queue
                new_path = path.copy()
                new_path.append(node2)
                queue.append(new_path)

