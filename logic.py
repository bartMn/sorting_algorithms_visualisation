import tkinter as tk
from math import pi, cos
import random
import sorts

class solver():
	"""
    Solver class to manage sorting algorithms and visualization.

    Attributes:
    - number_of_elements: Number of elements to sort.
    - graph_width: Width of the visualization area.
    - graph_height: Height of the visualization area.
    - master: Tkinter frame for the visualization.
    - interactive: List of labels for displaying comparisons and swaps.
    """

	def __init__(self,number_of_elements, graph_width, graph_height, master, interactive):
		"""
        Initialize the solver with visualization parameters and sorting algorithms.

        Inputs:
        - number_of_elements: Number of elements to sort.
        - graph_width: Width of the visualization area.
        - graph_height: Height of the visualization area.
        - master: Tkinter frame for the visualization.
        - interactive: List of Tkinter labels for displaying comparisons and swaps.

        Outputs:
        - Initializes the solver object with default values and sorting algorithms.
        """
		self.number_of_elements= number_of_elements
		self.graph_height= graph_height
		self.graph_width= graph_width
		self.master= master

		self.frames= []
		self.interactive= interactive
		self.number_of_swaps= 0
		self.number_of_comparisons= 0
		self.to_sort= self.create_rectangles()
		self.available_sorts= ["selection sort",
							    "selection sort double selection",
								"bubble sort",
								"cocktail shaker sort",
								"insertion sort",
								#"insertion sort opt",
								#"insertion sort binary",
								"Shellsort",
								"merge sort",
								"LSD radix sort",
								"quick sort"]
		self.sorting_method= None
		

		self.sort_dict= {"selection sort": sorts.Selection_sort,
						 "selection sort double selection": sorts.Selection_sort_double_selection,
						 "bubble sort": sorts.Bubble_sort, 
						 "bubble sort (optimised[almost_no_improvement])": sorts.Bubble_sort_optimised,
						 "cocktail shaker sort": sorts.Cocktail_shaker_sort,
						 "insertion sort": sorts.Insertion_sort_opt,
						 #"insertion sort opt": sorts.Insertion_sort_opt,
						 #"insertion sort binary": sorts.Insertion_sort_binary,
						 "Shellsort": sorts.Shellsort,
						 "merge sort": sorts.Merge_sort,
						 "LSD radix sort": sorts.LSD_radix_sort,
						 "quick sort": sorts.Quick_sort}

	def create_rectangles(self):
		"""
        Create rectangles for visualization.

        Outputs:
        - A list of integers representing the elements to be sorted.
        """
		self.angle_grad= 5/6*pi/(self.number_of_elements)
		current_angle= 0
		to_sort= []
		self.minimum_pecentage= 0.1
		self.grad= (1- self.minimum_pecentage)/self.number_of_elements
		self.bar_width= (self.graph_width-1)/self.number_of_elements
		for i in range(self.number_of_elements):

			to_sort.append(i+1)
			frame= self.create_one_rectangle(to_sort[-1])
			self.frames.append(frame)
			
			frame.grid(row=0, column= i, sticky="nsew")
		
		resize_preventer= tk.Frame(master= self.master, width= 1, height= self.graph_height+1, bg= "white")
		resize_preventer.columnconfigure(0, weight=4, minsize= 1)
		resize_preventer.rowconfigure(0, weight=4, minsize= self.graph_height+1)
		resize_preventer.grid(row=0, column= i+1, sticky="nsew")

		return to_sort

	def create_one_rectangle(self, bar):
		"""
        Create a single rectangle with color based on its value.

        Input:
        - bar: The value of the element to be represented as a rectangle.

        Output:
        - A Tkinter frame representing the rectangle.
        """
		percentage= self.grad*bar+ self.minimum_pecentage
		angle= self.angle_grad*(bar)

		red= self.color_intensity(angle, 0)
		blue= self.color_intensity(angle, -2*pi/3)
		green= self.color_intensity(angle, +2*pi/3)
		col_in_rgb= '#'+ red+green+blue

		frame= tk.Frame(master= self.master)

		child1= tk.Frame(master= frame,
				bg= f'{col_in_rgb}')
		child0= tk.Frame(master= frame,
				bg= 'white')

		frame.columnconfigure(0, weight=4, minsize= self.bar_width)
		frame.rowconfigure(0, weight=4, minsize= self.graph_height-self.graph_height*percentage)
		frame.rowconfigure(1, weight=4, minsize= self.graph_height*percentage)
		child0.grid(row=0, column= 0, sticky="nsew")
		child1.grid(row=1, column= 0, sticky="nsew")
		
		return frame


	def hex_value(self, integer):
		"""
        Convert an integer to a two-character hexadecimal string.

        Input:
        - integer: An integer value between 0 and 255.

        Output:
        - A two-character hexadecimal string.
        """
		hex_value= str(hex(integer))
		hex_value= hex_value[2:]
		if len(hex_value)==1:
			hex_value += '0'
			hex_value= hex_value[::-1]
		return hex_value

	def color_intensity(self, angle, phase):
		"""
        Calculate color intensity based on angle and phase.

        Inputs:
        - angle: The angle used for color calculation.
        - phase: The phase shift for the color calculation.

        Output:
        - A two-character hexadecimal string representing the color intensity.
        """
		
		out= cos(angle+ phase)**2
		if out > 0.75:
			out= 0.75
		elif out < 0.25:
			out = 0.25

		out -= 0.25
		out *= 340
		out= int(out)
		return self.hex_value(out)

	def swap(self, position_0, position_1):
		"""
        Swap two elements and update their visualization.

        Inputs:
        - position_0: Index of the first element.
        - position_1: Index of the second element.

        Output:
        - Updates the positions of the elements in the visualization.
        """
		self.number_of_swaps += 1
		temp_bar= self.to_sort[position_0]
		self.to_sort[position_0]= self.to_sort[position_1]
		self.to_sort[position_1]= temp_bar
		t_frame0= self.create_one_rectangle(self.to_sort[position_0])
		t_frame1= self.create_one_rectangle(self.to_sort[position_1])
		
		self.place_frame(frame= t_frame1, place= position_1)
		self.place_frame(frame= t_frame0, place= position_0)
		

		
	def place_frame(self, frame, place):
		"""
        Place a frame at a specific position in the grid.

        Inputs:
        - frame: The Tkinter frame to be placed.
        - place: The index where the frame should be placed.

        Output:
        - Updates the grid layout with the new frame.
        """
		frame.grid(row=0, column= place, sticky="nsew")
		temp= self.frames[place]
		self.frames[place]= frame
		temp.destroy()
		self.update()


	def shuffle(self):
		"""
        Shuffle the elements randomly.

        Output:
        - Updates the visualization with shuffled elements.
        """
		self.number_of_swaps= 0
		self.number_of_comparisons= 0
		self.update()

		temp_to_sort= list(self.to_sort)
		free_places= [i for i in range(self.number_of_elements)]
		for i in range(self.number_of_elements):
			place= random.choice(free_places)
			free_places.remove(place)
			self.to_sort[place]= temp_to_sort[i]
			temp_frame= self.create_one_rectangle(temp_to_sort[i])
			self.place_frame(frame= temp_frame, place= place)

	def comparison(self, key0, key1):
		"""
        Compare two elements and count the comparison.

        Inputs:
        - key0: The first element to compare.
        - key1: The second element to compare.

        Output:
        - Returns True if key0 > key1, otherwise False.
        """
		self.number_of_comparisons += 1
		if key0> key1:
			return True
		return False


	def update(self):
		"""
        Update the GUI and interactive labels.

        Output:
        - Refreshes the GUI and updates the comparison and swap counters.
        """
		self.master.update()
		self.interactive[0]["text"]= self.number_of_comparisons
		self.interactive[1]["text"]= self.number_of_swaps


	def sort(self):
		"""
        Perform sorting using the selected algorithm.

        Output:
        - Executes the sorting algorithm and updates the visualization.
        """
		if self.sorting_method:
			sorting_method= self.sort_dict[self.sorting_method](self)
			sorting_method.sort()
