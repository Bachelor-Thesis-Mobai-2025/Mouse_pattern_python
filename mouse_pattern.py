# Program to use file s stored by mouse tracking program and make graphic representation of mouse mvement.

import matplotlib.pyplot as plt
import json

def draw_line(movements):
    x_vals, y_vals = zip(*movements)  # Unpack x and y coordinates
    
    plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='b', markersize=8)
     
    # Optional annotate each point with its coordinates
    #for (x, y) in movements:
    #    plt.text(x, y, f'({x},{y})', fontsize=12, ha='right', va='bottom', color='red')
    
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Line Plot with Marked Coordinates")
    plt.grid(True)
    
    plt.show()

# Read coordinates from JSON file
def read_coordinates_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data["movements"]

# Use file name to create graph
file_path = "mouse_movement_log_5.json"
movements = read_coordinates_from_json(file_path)
draw_line(movements)
