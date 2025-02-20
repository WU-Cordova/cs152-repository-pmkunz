# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        """ initializes the array using a Sequence Type"""

        if not isinstance(starting_sequence, Sequence):
            raise ValueError("Input must be a sequence")

        # Are the elements in starting_sequence of the expected data type?
        if not all(isinstance(item, data_type) for item in starting_sequence):
            raise TypeError(f"Elements should be type {data_type}")
        
        self.__data_type = data_type                        # Data type for elements of the array
        self.__logical_size = len(starting_sequence)        # Logical size: number of elements the array holds
        self.__physical_size = self.__logical_size          # Physical size: actual amount of space occupied by the data
                                                            # Initally, set these to be the same      
        self.array = np.array(starting_sequence, dtype=data_type)   # Starting sequnce is converted into a NumPy array


    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        """ Retrieves the item at the index given """
    
        if not isinstance(index, (int, slice)): #check that index is an integer or a slice
            raise TypeError("Index must be an integer or a slice.")

        if isinstance(index, slice):
            start, stop = index.start, index.stop
            # check if out of bounds:
            if start >= self.__logical_size or stop > self.__logical_size or start < 0 or stop < 0 or start >= stop:
                raise IndexError("Out of bounds")

            items_to_return = self.array[index].tolist()    #index is a slice of the array
            return Array(starting_sequence = items_to_return, data_type = self.__data_type)

        # for single integer index
        elif isinstance(index, int):
            if index < 0:                      # for negative indicies
                index += self.__logical_size                
            if index < 0 or index >= self.__logical_size:
                raise IndexError("Out of bounds")
            return self.array[index]
        
    def __setitem__(self, index: int, item: T) -> None:
        """ Sets the item at the index given to the given value """
        if not isinstance(item, self.__data_type):  # Check type
            raise TypeError(f"Item should be of type {self.__data_type}")
        if index < 0: # for negative indices
            index += self.__logical_size
        if index < 0 or index >= self.__logical_size: # Check if index is out of bounds
            raise IndexError("Out of bounds")
        self.array[index] = item

    def append(self, data: T) -> None:
        """ Appends an element at the end of the array """
        self.array = np.append(self.array, data)
        self.__logical_size += 1

    def append_front(self, data: T) -> None:
        """ Appends an element at the front of the array """
        self.array = np.insert(self.array, 0, data)     # 0 is the index where the new value, data, will be placed 
        self.__logical_size =+ 1

    def pop(self) -> None:
        """ slices off the last element.
        Shrinks array's physical size when logical size <= to ¼ of the physical size.  """
        if self.__logical_size == 0:    # if the array is empty
            raise IndexError("Cannot pop empty array")
        last_element = self.array[-1]
        self.array = self.array[:-1]    # slices off the last element
        self.__logical_size -= 1

        # does the array needs to be shrunk?
        if self.__logical_size <= self.__physical_size // 4:
            self.__physical_size = max(self.__logical_size * 2, 1)
            self.array = np.resize(self.array, self.__physical_size)

        return last_element
    
    def pop_front(self) -> None:
        """ Deletes an item at the end of the array.
        Shrinks array's physical size when logical size <= to ¼ of the physical size.  """
        if self.__logical_size == 0:    # if the array is empty
            raise IndexError("Cannot pop empty array")    
        first_element = self.array[0]
        self.array = self.array[1:]     # slices off the first element
        self.__logical_size -= 1

        # does the array needs to be shrunk?
        if self.__logical_size <= self.__physical_size // 4:
            self.__physical_size = max(self.__logical_size * 2, 1)
            self.array = np.resize(self.array, self.__physical_size)

        return first_element

    def __len__(self) -> int: 
        """ Delete an item from the front of the array """
        return self.__logical_size

    def __eq__(self, other: object) -> bool:
        """ Checks if two arrays are equal """
        if not isinstance(other, Array):    # check if object is an instance of the Array class
            return False

        if self.__logical_size != other.__logical_size: #check if logical size (number of elements) is the same
            return False
        
        return np.array_equal(self.array, other.array)  # Check if the elements are the same (will return True or False)
    
    def __iter__(self) -> Iterator[T]:
        """ Returns an independent iterator to the Array.
        (Allows for iteration over the Array) """
        return iter(self.array)

    def __reversed__(self) -> Iterator[T]:
        """ Returns an iterator that starts at the end of the array and steps backwards """
        return iter(self.array[::-1])

    def __delitem__(self, index: int) -> None:
        """ Deletes an item at a specific index
        Shrinks array's physical size when logical size <= to ¼ of the physical size. 
        """
        if index < 0:                                   # for negative indices
            index += self.__logical_size
        if index >= self.__logical_size or index < 0:   # check if out of bounds
            raise IndexError("Index out of bounds")
        self.array = np.delete(self.array, index)       # shifts elements to fill the gap
        self.__logical_size -= 1
        
        # does the array needs to be shrunk?
        if self.__logical_size <= self.__physical_size // 4:
            self.__physical_size = max(self.__logical_size * 2, 1)
            self.array = np.resize(self.array, self.__physical_size)

    def __contains__(self, item: Any) -> bool:
        """ Returns whether the item is in the array. """
        return item in self.array

    def clear(self) -> None:
        """ Removes all items from the array """
        self.array = np.array([], dtype=self.__data_type)  # creates an empty array of same the data type
        self.__logical_size = 0
        self.__physical_size = 0

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__logical_size}, Physical: {self.__physical_size}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')