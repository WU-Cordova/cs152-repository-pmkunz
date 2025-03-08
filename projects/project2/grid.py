import random
from datastructures.array2d import Array2D
from projects.project2.cell import Cell
import os

class Grid:
	def __init__(self, width: int, height: int) -> None:

		# Grid dimensions:
		self.width = width		# width = number of columns
		self.height = height	# height = number of rows

		cells: List[List[Cell]] = []

		for row in range(height):
			cells.append([])
			for col in range(width):
				is_alive = random.choice([True, False])
				cells[row].append(Cell(is_alive=is_alive))

		self.grid: Array2D = Array2D(starting_sequence = cells, data_type = Cell)       # check?

		self.history = [] # stores grid history

	def display(self):
		""" Displays the current grid """
		
		#print(self.grid)

		os.system('cls' if os.name == 'nt' else 'clear')

		print("+" +"----+" * self.width)

		for row in range(self.height):
			row_display = "|"
			for col in range(self.width):
				if self.grid[row][col].is_alive:
					row_display +=" 🦠 "
				else:
					row_display += " ⬛️ "
				row_display += "|"
					
				# if col < self.width -1:
				# 	row_display += " "

			print(row_display)

			print("+" + "----+" * (self.width))

	def count_neighbors(self, row: int, col: int) -> int:
		""" Counts how many alive neighbors there are for a cell """

		# for a given cell position (row, col)
		# Positions of the neighboring cells:
		neighbor_positions = [(-1, -1), (-1, 0), (-1,1),
							  (0, -1), (0,1),
							  (1,-1), (1,0), (1,1)]

		alive_neighbors = 0		# tracks how many neighbors are alive

		for row_offset, col_offset in neighbor_positions:
			neighbor_row, neighbor_col = row + row_offset, col + col_offset		#calculates the actual row and column it's at

			if 0 <= neighbor_row < self.height and 0 <= neighbor_col < self.width:	#check we are within the grid bounds
				if self.grid[neighbor_row][neighbor_col].is_alive:
					alive_neighbors += 1

		return alive_neighbors

	def next_generation(self) -> None:
		""" computes next generation of the grid """
		#?
		new_grid: Array2D = Array2D(starting_sequence=[[Cell(is_alive=False) for _ in range(self.width)] for _ in range(self.height)], data_type = Cell)

		for row in range(self.height):
			for col in range(self.width):
				cell = self.grid[row][col]							# current cell in the iteration
				alive_neighbors = self.count_neighbors(row, col)	# takes that cell and sees how many alive neighbors there are
				if cell.is_alive:
					if alive_neighbors < 2 or alive_neighbors > 3:
						new_grid[row][col].set_dead()  				# death of cell by underpopulation or overpopulation
					else:
						new_grid[row][col].set_alive()  			# cell survives, stays alive
				else: #(the cell is not alive)
					if alive_neighbors == 3:
						new_grid[row][col].set_alive()  			# Cell becomes alive by reproduction

        # Add the current grid to history
		self.history.append(self.grid)
		if len(self.history) > 5:
			self.history.pop(0)

		self.grid = new_grid

	def is_stable(self) -> bool:
		""" checks if the grid has become stable """
		
		if len(self.history) < 3:
			return False

		if self.grid == self.history[-1]:
			return True

			# if self.grid == self.history[-2]:
			# 	etc
		#?

		# for past_grid in self.history:
		# 	if self.grid == past.grid:
		# 		continue
		# 	else:
		# 		break
		# return True 