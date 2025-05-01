import tkinter as tk
from tkinter import ttk
from logic import *

# Constants for GUI dimensions and number of elements
G_WIDTH = 1000
G_HEIGHT = 500
ELEMENTS = 500

# Initialize the main window
window = tk.Tk()
window.title("Sorting Visualizer")

# Function to shuffle the elements
def shuffle():
    button0.config(command=do_nothing)
    button1.config(command=do_nothing)
    data.shuffle()
    button0.config(command=shuffle)
    button1.config(command=sort)

# Function to set the sorting algorithm based on user selection
def set_sort(event):
    data.sorting_method = alg_selection.get()

# Function to sort the elements using the selected algorithm
def sort():
    button0.config(command=do_nothing)
    button1.config(command=do_nothing)
    data.sort()
    button0.config(command=shuffle)
    button1.config(command=sort)

# Placeholder function for disabled buttons
def do_nothing():
    pass

# Create the frame for the sorting visualization
graph_frame= tk.Frame(width= G_WIDTH,
					  height= G_HEIGHT,
					  borderwidth = 10,
					  relief= tk.RIDGE)

# Create the frame for controls and labels
frame = tk.Frame(master=window)

# Configure grid layout for the control frame
for i in range(3):
    frame.columnconfigure(i, weight=4, minsize=25)
for i in range(2):
    frame.rowconfigure(i, weight=4, minsize=5)

# Shuffle button
button0 = tk.Button(text="shuffle",
    				width=25,
    				height=5,
    				bg="blue",
    				fg="yellow",
    				command= shuffle,
    				master= frame)

# Sort button
button1= tk.Button(text="sort",
    			   width=25,
    			   height=5,
    			   bg="blue",
    			   fg="yellow",
    			   command= sort,
    			   master= frame)

# Labels for displaying the number of comparisons and swaps
label0= tk.Label(text="number of comparisons:  ",
    			 width= 25,
    			 height=5,
    			 bg="red",
    			 fg="yellow",
    			 master= frame)
label1= tk.Label(text="number of swaps:  ",
    			 width= 25,
    			 height=5,
    			 bg="red",
    			 fg="yellow",
    			 master= frame)

label2=tk.Label(text="0",
    			width=10,
    			height=5,
    			bg="blue",
    			fg="yellow",
    			master= frame)

label3=tk.Label(text="0",
    			width=10,
    			height=5,
    			bg="blue",
    			fg="yellow",
    			master= frame)

# Initialize the solver object for sorting
data= solver(number_of_elements= ELEMENTS,
			 graph_width= G_WIDTH,
			 graph_height= G_HEIGHT,
			 master= graph_frame,
			 interactive= [label2, label3])

# Create the frame for algorithm selection
selection_frame= tk.Frame(master= window)
selection_label= tk.Label(master= selection_frame,
                          width= 25,
                          height= 1,
                          text= "select a sorting algorithm:")

# Dropdown menu for selecting sorting algorithms
alg_selection= ttk.Combobox(master= selection_frame, 
							value= data.available_sorts,
							state= "readonly") 


# Bind the selection event to update the sorting method
alg_selection.bind("<<ComboboxSelected>>", set_sort)
selection_label.grid(row=0, column=0)
alg_selection.grid(row=0, column=1)

# Pack frames and widgets
selection_frame.pack()
graph_frame.pack()

button0.grid(row=0, column= 0)
button1.grid(row=1, column= 0)
label0.grid(row=0, column= 1)
label1.grid(row=1, column= 1)
label2.grid(row=0, column= 2)
label3.grid(row=1, column= 2)

frame.pack()

# Start the Tkinter main loop
window.mainloop()