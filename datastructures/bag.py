from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        
        self.contents = {}  # Initialize the internal data structure to store the items and their counts
        
        for item in items:
            if item is not None:                # Check the item is not None
                if item in self.contents:       
                    self.contents[item] += 1    # Add to the count
                else:                           # Else, meaning item is not in self.contents
                   self.contents[item] = 1      # Make the count 1 because it is the first one being added
            else:                               # Else, meaning item is None
                raise TypeError 

    def add(self, item: T) -> None:
        if item is not None:                    # Check the item is not None
            if item in self.contents:       
                self.contents[item] += 1        # Add to the count
            else:                               # Else, meaning item is not in self.contents
                self.contents[item] = 1         # Make the count 1 because it is the first one being added
        else:                                   # Else, meaning item is None
            raise TypeError 

    def remove(self, item: T) -> None:    
        if item is not None:                    # Check the item is not None
            if item in self.contents:   
                self.contents[item] -= 1        # Subtract from the count
            else:                               # Else, meaning item is not in self.contents       
                raise ValueError 
        else:                                   # Else, meaning item is None
            raise TypeError 

    def count(self, item: T) -> int:
        return self.contents.get(item,0)        # Return the count, or if there is none then return 0 by default

    def __len__(self) -> int:
        return sum(self.contents.values())      # Returns total number of items (includes duplicates)
    
    def distinct_items(self) -> int:
        return self.contents.keys()             # Returns the keys, the distinct items

    def __contains__(self, item) -> bool:
        return item in self.contents            # Check if the item exists in the bag

    def clear(self) -> None:
        self.contents.clear()                   # Clear all items in the bag