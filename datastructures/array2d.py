from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T

# before running, enter this into the terminal:
# export PYTHONPATH=/Users/pkmckenna/Documents/GitHub/cs152-repository-pmkunz:$PYTHONPATH


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type: type) -> None:
            self.row_index = row_index
            self.array = array
            self.num_columns = num_columns
            self.data_type = data_type

        def __getitem__(self, column_index: int) -> T:
            
            if column_index < 0 or column_index >= self.num_columns:
                raise IndexError("Index out of bounds")

            index = self.row_index * self.num_columns + column_index
            return self.array[index]
        
        def __setitem__(self, column_index: int, value: T) -> None:
            
            if column_index < 0 or column_index >= self.num_columns:
                raise IndexError("Index out of bounds")

            index = self.row_index * self.num_columns + column_index
            self.array[index] = value

        def map_index(self, row_index: int, column_index:int) -> int:
           return row_index * self.num_columns + column_index
        
        def __iter__(self) -> Iterator[T]:
            for column_index in range(self.num_columns):
                yield self[column_index]
        
        def __reversed__(self) -> Iterator[T]:
            raise NotImplementedError('Row.__reversed__ not implemented.')

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        
        if not isinstance(starting_sequence, (list, tuple)) or not all(isinstance(row, (list, tuple)) for row in starting_sequence):
            raise ValueError("starting_sequence must be a sequence of sequences")   # Starting_sequence must be a sequence of sequences
         
        for row in starting_sequence:
            if not all(isinstance(element, data_type) for element in row):
                raise ValueError(f"All elements must be of type {data_type}")       # There cannot be mixed types in rows
                
        row_len = len(starting_sequence[0])
        for row in starting_sequence:
            if len(row) != row_len:
                raise ValueError("All rows must have the same length")              # Row lengths must be consistent
        
        #initialize
        self.data_type = data_type
        self.row_len = len(starting_sequence)
        self.column_len = len(starting_sequence[0])

        self.array2d = Array([data_type() for item in range(self.row_len * self.column_len)], data_type = data_type)
        
        index=0
        for row_index in range(self.row_len):
            for column_index in range(self.column_len):
                self.array2d[index] = starting_sequence[row_index][column_index]
                index += 1

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        starting_sequence: List[List[T]] = []

        for row in range(rows):
            starting_sequence.append([])
            for col in range(cols):
                starting_sequence[row].append(data_type())

        return Array2D(starting_sequence=starting_sequence, data_type=data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        return Array2D.Row(row_index, self.array2d, self.column_len, self.data_type)
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        """ Allows for iteration over the rows of the 2DArray. Returns each row. """
        for row_index in range(self.row_len):
            yield self[row_index]
    
    def __reversed__(self):
        """ Iterates over the rows in reverse order"""
        for row_index in range(self.row_len -1, -1, -1):
            yield self[row_index]
    
    def __len__(self): 
        """ Return the number of rows in the 2D Array"""
        return self.row_len
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
        #return f'[{", ".join(f"{str(self[row_index])}" for row_index in range(self.row_len))}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.row_len} Rows x {self.column_len} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')