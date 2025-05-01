class Sort():
	"""
    Base class for all sorting algorithms.

    Attributes:
    - master: An instance of the `solver` class that manages the sorting visualization.
    """

	def __init__(self, master):
		"""
        Initialize the Sort class.

        Input:
        - master: An instance of the `solver` class that manages the sorting visualization.
        """
		self.master= master



class Selection_sort(Sort):
	"""
    Implements the Selection Sort algorithm.
    """

	def sort(self):
		"""
        Perform the Selection Sort algorithm.

        Output:
        - Sorts the `master.to_sort` list in ascending order while updating the visualization.
        """
		for i in range(self.master.number_of_elements):
			swap= False
			temp_min= i
			for j in range(i, self.master.number_of_elements):
				if self.master.comparison(self.master.to_sort[temp_min], self.master.to_sort[j]):
					# Find the minimum element in the unsorted part
					temp_min= j
					swap= True
			if swap:
				# Swap the minimum element with the first unsorted element
				self.master.swap(i, temp_min)



class Selection_sort_double_selection(Sort):
	"""
    Implements the Double Selection Sort algorithm.
    """
	def sort(self):
		"""
        Perform the Double Selection Sort algorithm.

        Output:
        - Sorts the `master.to_sort` list in ascending order while updating the visualization.
        """
		for i in range(int(self.master.number_of_elements)):
			swap_min= False
			swap_max= False 
			temp_min= i
			temp_max= (self.master.number_of_elements-1)-i
			
			for j in range(i, self.master.number_of_elements-i):
				if self.master.comparison(self.master.to_sort[temp_min], self.master.to_sort[j]):
					# Find the minimum element
					temp_min= j
					swap_min= True
				if self.master.comparison(self.master.to_sort[j], self.master.to_sort[temp_max]):
					# Find the maximum element
					temp_max= j
					swap_max= True
				to_swap= j
			
			if swap_min:
				if temp_max== i:
					# Adjust the maximum index if it overlaps with the minimum index
					temp_max= temp_min
					if temp_min == to_swap:
						swap_max= False
				
				# Swap the minimum element
				self.master.swap(i, temp_min)		

			if swap_max:
				# Swap the maximum element
				self.master.swap(to_swap, temp_max)



class Bubble_sort(Sort):
	"""
    Implements the Bubble Sort algorithm.
    """

	def sort(self):
		"""
        Perform the Bubble Sort algorithm.

        Output:
        - Sorts the `master.to_sort` list in ascending order while updating the visualization.
        """
		for i in range(self.master.number_of_elements):
			for j in range(self.master.number_of_elements-1-i):
				if self.master.comparison(self.master.to_sort[j], self.master.to_sort[j+1]):
					# Swap adjacent elements if they are in the wrong order
					self.master.swap(j, j+1)



class Bubble_sort_optimised(Sort):
	"""
    Implements an optimized version of the Bubble Sort algorithm.
    """
	def sort(self):
		"""
        Perform the optimized Bubble Sort algorithm.

        Output:
        - Sorts the `master.to_sort` list in ascending order while updating the visualization.
        """
		n = self.master.number_of_elements
		while n>= 1:
			nw= 0
			for j in range(n-1):
				if self.master.comparison(self.master.to_sort[j], self.master.to_sort[j+1]):
					# Swap adjacent elements if they are in the wrong order
					self.master.swap(j, j+1)
					nw= j+1
			n= nw



class Cocktail_shaker_sort(Sort):
	"""
    Implements the Cocktail Shaker Sort algorithm.
    """
	def sort(self):
		"""
        Perform the Cocktail Shaker Sort algorithm.

        Output:
        - Sorts the `master.to_sort` list in ascending order while updating the visualization.
        """
		swap= True
		sorted_on_left= 0
		sorted_on_right= 0
		
		while swap:
			swap= False
			for i in range(self.master.number_of_elements-1-sorted_on_left):
				if self.master.comparison(self.master.to_sort[i], self.master.to_sort[i+1]):
					# Swap adjacent elements if they are in the wrong order
					self.master.swap(i, i+1)
					swap= True
			sorted_on_left +=1
			if not swap:
				break
			swap= False

			for i in range(self.master.number_of_elements -2, 0+ sorted_on_right, -1):
				if self.master.comparison(self.master.to_sort[i], self.master.to_sort[i+1]):
					# Swap adjacent elements if they are in the wrong order
					self.master.swap(i, i+1)
					swap= True
			sorted_on_right += 1



class Insertion_sort(Sort):
	"""
    Implements the Insertion Sort algorithm.
    """

	def sort(self):
		"""
        Perform the Insertion Sort algorithm.

        Output:
        - Sorts the `master.to_sort` list in ascending order while updating the visualization.
        """
		for i in range(1, self.master.number_of_elements):
			for j in range(i, 0, -1):
				if self.master.comparison(self.master.to_sort[j], self.master.to_sort[j-1]):
					# Stop if the current element is in the correct position
					break
				# Swap the current element with the previous one
				self.master.swap(j, j-1)



class Insertion_sort_opt(Sort):
	"""
    Implements an optimized version of the Insertion Sort algorithm.
    """

	def sort(self):
		"""
        Perform the optimized Insertion Sort algorithm.

        Output:
        - Sorts the `master.to_sort` list in ascending order while updating the visualization.
        """
		i = 1
		while i< self.master.number_of_elements:
			temp= self.master.to_sort[i]
			j= i-1
			while j>= 0:
				if self.master.comparison(temp, self.master.to_sort[j]):
					# Stop if the current element is in the correct position
					break
				self.master.to_sort[j+1]= self.master.to_sort[j]
				temp_frame= self.master.create_one_rectangle(self.master.to_sort[j+1])
				self.master.place_frame(temp_frame, j+1)
				j -= 1
			self.master.to_sort[j+1]= temp
			temp_frame= self.master.create_one_rectangle(temp)
			self.master.place_frame(temp_frame, j+1)
			i += 1



class Insertion_sort_binary(Sort):
	"""
    Implements the Binary Insertion Sort algorithm.
    """

	def Binary_seach(self, value, start, end):
		"""
        Perform a binary search to find the correct position for the value.

        Inputs:
        - value: The value to insert.
        - start: The starting index of the search range.
        - end: The ending index of the search range.

        Output:
        - The index where the value should be inserted.
        """
		if start== end:
			if self.master.comparison(self.master.to_sort[start], value):
				return start
			else:
				return start+1
		if self.master.comparison(start, end): 
			return start

		middle= (start+ end)//2
		if self.master.comparison(value, self.master.to_sort[middle]):
			return self.Binary_seach(value, middle+1, end)
		elif self.master.comparison(self.master.to_sort[middle],value):
			return self.Binary_seach(value, start, middle-1)

		else:
			return middle

	def sort(self):
		"""
        Perform the Binary Insertion Sort algorithm.

        Output:
        - Sorts the `master.to_sort` list in ascending order while updating the visualization.
        """
		for i in range(1, self.master.number_of_elements):
			value= self.master.to_sort[i]
			j= self.Binary_seach(value, 0, i-1)
			self.master.to_sort= self.master.to_sort[:j]+ [value]+ self.master.to_sort[j:i]+ self.master.to_sort[i+1: ]
			for to_update in range(j, i+1):
				temp=  self.master.to_sort[to_update]
				temp_frame= self.master.create_one_rectangle(temp)
				self.master.place_frame(temp_frame, to_update)


class Shellsort(Sort):
	"""
    Implements the Shell Sort algorithm.
    """

	def sort(self):
		"""
        Perform the Shell Sort algorithm.

        Output:
        - Sorts the `master.to_sort` list in ascending order while updating the visualization.
        """
		gaps= [701, 301, 132, 57, 23, 10, 4, 1]
		for gap in gaps:
			for i in range(gap, self.master.number_of_elements):
				temp= self.master.to_sort[i]
				j= i
				while  j >= gap:
					if not self.master.comparison(self.master.to_sort[j-gap], temp):
						break
					self.master.to_sort[j] = self.master.to_sort[j-gap]
					temp_frame= self.master.create_one_rectangle(self.master.to_sort[j])
					self.master.place_frame(temp_frame, j)
					j -= gap
				self.master.to_sort[j] = temp
				temp_frame= self.master.create_one_rectangle(temp)
				self.master.place_frame(temp_frame, j)



class Merge_sort(Sort):
	"""
    Implements the Merge Sort algorithm.
    """

	def sort(self):
		"""
        Perform the Merge Sort algorithm.

        Output:
        - Sorts the `master.to_sort` list in ascending order while updating the visualization.
        """
		self.master.to_sort= self.Mergesort(self.master.to_sort, 0)	
		self.master.update()

	def Merge(self, right_list, left_list, start):
		"""
        Merge two sorted sublists into a single sorted list.

        Inputs:
        - right_list: The right sublist.
        - left_list: The left sublist.
        - start: The starting index of the merge.

        Output:
        - Updates the `master.to_sort` list with the merged result.
        """
		result= []
		result_len= 0

		while right_list and left_list:
			if self.master.comparison(right_list[0], left_list[0]):
				result.append(left_list.pop(0))
			else:
				result.append(right_list.pop(0))

			temp_frame= self.master.create_one_rectangle(result[-1])
			
			self.master.place_frame(frame= temp_frame, place= result_len+start)
			result_len += 1

		while left_list:
			result.append(left_list.pop(0))
			temp_frame= self.master.create_one_rectangle(result[-1])
			self.master.place_frame(frame= temp_frame, place= result_len+start)				
			result_len += 1

		while right_list:
			result.append(right_list.pop(0))
			temp_frame= self.master.create_one_rectangle(result[-1])
			self.master.place_frame(frame= temp_frame, place= result_len+start)
			result_len += 1

		return result	


	def Mergesort(self, to_sort, start):
		if len(to_sort)<= 1:
			return to_sort
		half_point= len(to_sort)//2
		left_list= to_sort[half_point : ]
		right_list= to_sort[ : half_point]

		right_list= self.Mergesort(right_list, start)
		left_list= self.Mergesort(left_list, start+ half_point)

		return self.Merge(left_list, right_list, start)



class LSD_radix_sort(Sort):
	"""
	Implements the Least Significant Digit (LSD) Radix Sort algorithm.
	"""
	def sort(self):
		"""
		Perform the LSD Radix Sort algorithm.

		Output:
		- Sorts the `master.to_sort` list in ascending order while updating the visualization.
		"""

		radix= 10
		buckets= [[] for i in range(radix)]

		finished= False
		digit= 1
		while not finished:
			finished= True

			for i in self.master.to_sort:
				temp= i // digit
				buckets[temp %radix].append(i)
				if temp > radix-1:
					finished= False
			position= 0
			for bucket in buckets:
				for i in bucket:
					self.master.to_sort[position]= i
					temp_frame= self.master.create_one_rectangle(self.master.to_sort[position])
					self.master.place_frame(frame= temp_frame, place= position)
				
					position += 1
				bucket.clear()

			digit*= radix




class Quick_sort(Sort):
	"""
	Implements the Quick Sort algorithm.
	"""

	def sort(self):
		"""
		Perform the Quick Sort algorithm.

		Output:
		- Sorts the `master.to_sort` list in ascending order while updating the visualization.
		"""
		self.Quicksort(0, self.master.number_of_elements-1)

	def Quicksort(self, low, high):
		"""
		Perform the Quick Sort algorithm recursively.
		"""
		i= low
		j= high
		pivot= self.master.to_sort[(low+high)//2]
		while True:
			while self.master.comparison(pivot, self.master.to_sort[i]):
				i += 1
			while self.master.comparison(self.master.to_sort[j], pivot): 
				j -= 1
			if i<=j:
				self.master.swap(i, j)
				i += 1
				j -= 1
			if i>j:
				break
		if low< j:
			self.Quicksort(low, j)
		if i< high:
			self.Quicksort(i, high)
