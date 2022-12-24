import tkinter
import tkintermapview
import os
from BFS import Bfs
from A_star import A_star
from DFS import DFS
from Uniform_Cost import uniform_cost
import webbrowser
base_path = os.path.dirname(os.path.abspath(__file__))

# root widget
root = tkinter.Tk()

# creating window's title
root.title("Find Path with different Algorithms")

# setting a default window size
root.geometry("900x800")

# opening coordinates files and storing them as dictionary {'city': [lat, long]}
with open(os.path.join(base_path, "Coordinates.txt")) as data:
    coordinates = eval(data.read())

# creating map_widget and adding to the root window
map_widget = tkintermapview.TkinterMapView(width=900, height=600, corner_radius=30)
map_widget.pack(padx=20, pady=10, expand=True, fill='both')

# setting map service to google maps server
map_widget.set_tile_server(
    "https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", 
    max_zoom=22
)

# setting initial position and zoom
map_widget.set_address('Cairo, Egypt')
map_widget.set_zoom(8.5)

# adding frame widget below map_widget on the root window
control_frame = tkinter.LabelFrame(root, text="Path controller")
control_frame.pack(fill='both', expand=True, padx=20, pady=5)

# creating a list of all available cities by names
cities = list(coordinates.keys())

# origin city option list
# creating label and adding it the frame control widget which created before
origin_label = tkinter.Label(control_frame, text="Origin City", padx=5)
origin_label.grid(row=0, column=0, padx=10, pady=5)

# creating combo box widget and adding it to frame control widget
origin_choice = tkinter.StringVar()
origin_city = tkinter.ttk.Combobox(control_frame, width=15, textvariable=origin_choice, state="readonly")
origin_city['values'] = cities
origin_city.grid(row=1, column=0, padx=10)
origin_city.current(0)

# destination city options list
# creating label and adding it the frame control widget which created before
dest_label = tkinter.Label(control_frame, text="Destination City", padx=5)
dest_label.grid(row=0, column=1, padx=10, pady=5)

# creating combo box widget and adding it to frame control widget
dest_choice = tkinter.StringVar()
destination_city = tkinter.ttk.Combobox(
    control_frame, 
    width=15, 
    textvariable=dest_choice, 
    state="readonly"
)
destination_city['values'] = cities
destination_city.grid(row=1, column=1, padx=10)
destination_city.current(1)

# Algorithm choice options list
# creating label and adding it the frame control widget which created before
algo_label = tkinter.Label(control_frame, text="Algorithm Choice", padx=5)
algo_label.grid(row=0, column=2, padx=10, pady=5)

# creating combo box widget and adding it to frame control widget
algo_choice = tkinter.StringVar()
algorithm_choice = tkinter.ttk.Combobox(
    control_frame, 
    width=15, 
    textvariable=algo_choice, 
    state="readonly"
)

algorithm_choice['values'] = ['BFS', 'DFS', 'A*', 'Uniform-Cost']
algorithm_choice.grid(row=1, column=2, padx=5)
algorithm_choice.current(1)

# creating a global path and markers_list to be checked in get_path function
# every time it's executed
path = None
markers_list = []


def clear_map():
    if path:
        # clearing every mark on the map
        for marker in markers_list:
            marker.delete()
        # deleting the old path
        path.delete()

def get_path():
    # declaring that we want to use and access them as a global variables
    global path
    global markers_list

    # checking if there is a created path from previous operation
    if path:
        # clearing every mark on the map
        for marker in markers_list:
            marker.delete()
        # deleting the old path
        path.delete()

    # getting the resultant order of cities using our predefined functions
    # each one represent different searching algorithm depending on user's choice
    if algorithm_choice.get() == 'BFS':
        path_cities = Bfs(origin_city.get(), destination_city.get())

    elif algorithm_choice.get() == 'DFS':
        path_cities = DFS(origin_city.get(), destination_city.get())

    elif algorithm_choice.get() == 'Uniform-Cost':
        path_cities = uniform_cost(origin_city.get(), destination_city.get())

    elif algorithm_choice.get() == 'A*':
        path_cities = A_star(origin_city.get(), destination_city.get())
        path_cities = [city[0] for city in path_cities]

    # if the choice not correct for any reason we terminate the function
    else:
        return

    # path_coordinates is used to hold the coordinates of every city in the path
    # to be used later in creating the path
    path_coordinates = []

    for city in path_cities:
        # we get the coordinates of every city from our data, creating a marker from it
        marker = map_widget.set_marker(
            coordinates[city][0], coordinates[city][1], text=city, text_color='red')
        # we add every marker to out markers_list to keep track of them
        # and to be cleared later for new operations
        markers_list.append(marker)
        # adding every marker's (city) coordinates to the path_coordinates list
        path_coordinates.append(marker.position)

    # drawing the path on the map
    path = map_widget.set_path(path_coordinates, width=7)


# creating and adding the Get Path button to appear on the control frame
action_btn = tkinter.Button(control_frame, text="Get Path", command=get_path, bg="#66b032")
action_btn.grid(row=1, column=3, padx=5)

# clear map from markers
clear_map = tkinter.Button(control_frame, text="Clear", command=clear_map, bg="#ff3800")
clear_map.grid(row=1, column=5, padx=5)


root.mainloop()
