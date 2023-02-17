import random

class Sudoku():
	
	def __init__(self):
		self.grid = [[random.randint(1,9) for i in range(9)] for j in range(9)]
	
	def print_grid(self):
		"""Prints the grid"""
		for i, row in enumerate(self.grid, 1):
			# Create a space and | delimited string for the row
			res = ""
			for j, cell in enumerate(row, 1):
				if j == 1:
					res += f"{i} | {cell} "
				elif j % 3 == 0:
					res += f" {cell} | "
				else:
					res += f" {cell} "
			
			# Print column numbers and starting dashes
			if i == 1:
				print(" " * 4 + '1  2  3    4  5  6    7  8  9  ')
				print(" " * 2 + (len(res) - 3) * "-")
			
			print(res)
			
			# Print dashes after every block
			if i % 3 == 0:
				print(" " * 2 + (len(res) - 3) * "-")
	
	def get_box(self, box_num):
		"""Returns box_num box. Boxes are numbered from the top left (box 1) 
		to the bottom right (box 9). box_num should be an integer between 
		1-9."""
		if not (1 <= box_num <= 9):
			raise Exception("box_num should be an integer between 1 to 9.")
		else:			
			box = []
			
			# Calculate starting row and col for required box
			index = box_num % 3 if box_num % 3 != 0 else 3
			start_row = box_num - index 
			start_col = index  + 2 * (index - 1) - 1
			
			for row_num in range(start_row, start_row + 3):
				for col_num in range(start_col, start_col + 3):
					box.append(self.grid[row_num][col_num])
			
			print(box)
				
	def get_col(self, col_num):
		"""Returns col_num column. col_num should be an integer between 1-9."""
		if not (1 <= col_num <= 9):
			raise Exception("col_num should be an integer between 1 to 9.")
		else:
			col = [row[col_num - 1] for row in self.grid]
			return col 
	
	def get_row(self, row_num):
		"""Returns row_num row. row_num should be an integer between 1-9."""
		if not (1 <= row_num <= 9):
			raise Exception("row_num should be an integer between 1 to 9.")
		else:
			return self.grid[row_num - 1] 
		
s = Sudoku()
s.print_grid()
s.get_box(2)
