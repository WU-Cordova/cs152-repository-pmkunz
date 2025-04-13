from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.count = 0
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.data_type = data_type

    @staticmethod   # does not have access to the self data
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        
        llist: LinkedList[T] = LinkedList(data_type = data_type)
        for item in sequence:
            if not isinstance(item, data_type): # check that all the items in sequence are of the same data type
                raise TypeError(f"Item {item} is not of data type {data_type}")
            llist.append(item)
        return llist

    def append(self, item: T) -> None:

        if not isinstance(item, self.data_type): # check that item is the same type (data_type)
            raise TypeError(f"Item {item} is not of data type {self.data_type}")
        
        node = LinkedList.Node(data=item)

        if self.empty:
            self.head = self.tail = node
        
        else: # not empty 
            node.previous = self.tail # set node's previous to the current tail
            if self.tail: 
                    self.tail.next = node # set tail's next to the new node
            self.tail = node # set tail to new node 

        self.count += 1

    def prepend(self, item: T) -> None:
        
        if not isinstance(item, self.data_type): # check that item is the same type (data_type)
            raise TypeError(f"Item {item} is not of data type {self.data_type}")
        
        new_node = LinkedList.Node(data=item) # create new node
        new_node.next = self.head # set new node's next to head
        if self.head:
            self.head.previous= new_node # set head's previous to new node
        self.head = new_node # set head to new node

        #
        if self.tail is None:   # if the list was empty before, where head = None and tail = None
            self.tail = new_node # then tail also needs to be set to new_node, or else hte tail will still be None
        #

        self.count += 1

    def insert_before(self, target: T, item: T) -> None:

        if not isinstance(target,self.data_type): # Raise TypeError  if the target is not the right type
            raise TypeError(f"Item {item} is not of data type {self.data_type}")

        if not isinstance(item,self.data_type): # Raise TypeError if the item is not the right type
            raise TypeError(f"Item {item} is not of data type {self.data_type}")

        # Traverse the list to find the taget node:
        travel = self.head
        while travel: # (while travel is not None)
            if travel.data == target:
                break
            travel = travel.next

        if travel is None: # Raise ValueError if the target does not exist
            raise ValueError(f"The target value {target} was not found in the linked list.")

        if travel is self.head:
            self.prepend(item)
            return

        new_node = LinkedList.Node(data=item) # create the node
        travel.previous.next = new_node
        new_node.next = travel
        new_node.previous = travel.previous
        travel.previous = new_node

        self.count +=1  # increment the count


    def insert_after(self, target: T, item: T) -> None:
        
        if not isinstance(target, self.data_type): # Raise TypeError  if the target is not the right type
            raise TypeError(f"Item {item} is not of data type {self.data_type}")

        if not isinstance(item, self.data_type): # Raise TypeError if the item is not the right type
            raise TypeError(f"Item {item} is not of data type {self.data_type}")

        # Traverse the list to find the taget node:
        travel = self.head
        while travel: # (while travel is not None)
            if travel.data == target:
                break
            travel = travel.next

        if travel is None: # Raise ValueError if the target does not exist
            raise ValueError(f"The target value {target} was not found in the linked list.")

        if travel is self.tail:
            self.append(item)
            return

        new_node = LinkedList.Node(data=item) # create the node
        if travel.next:     # ensure travel.previous exists
            travel.next.previous = new_node
        new_node.next = travel.next
        travel.next = new_node
        new_node.previous = travel

        self.count +=1  # increment the count


    def remove(self, item: T) -> None:

        if not isinstance(item, self.data_type): # Raise TypeError if the item is not the right type
            raise TypeError(f"Item {item} is not of data type {self.data_type}")
        
        travel = self.head
        while travel:
            if travel.data == item:
                break
            travel = travel.next

        if travel is None: # Raise ValueError if the item does not exist
            raise ValueError(f"The item value {item} was not found in the linked list.")

        if travel is self.head:
            self.head = travel.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = None
        elif travel is self.tail:
            self.tail = travel.previous
            if self.tail:
                self.tail.next = None
        else:
            if travel.previous:
                travel.previous.next = travel.next
            if travel.next:
                travel.next.previous = travel.previous
        
        self.count -= 1

    def remove_all(self, item: T) -> None:

        if not isinstance(item, self.data_type): # Raise TypeError if the item is not the right type
            raise TypeError(f"Item {item} is not of data type {self.data_type}")
        
        travel = self.head
        while travel:
            next_node = travel.next
            if travel.data == item:
                if travel is self.head:
                    self.head = travel.next
                    if self.head:
                        self.head.previous = None
                elif travel is self.tail:
                    self.tail = travel.previous
                    if self.tail:
                        self.tail.next = None
                else:
                    if travel.previous:
                        travel.previous.next = travel.next
                    if travel.next:
                        travel.next.previous = travel.previous

                self.count -= 1
            travel = next_node


    def pop(self) -> T:

        if self.empty:
            raise IndexError("Cannot pop from an empty linked list.")

        data = self.tail.data

        self.tail = self.tail.previous
        if self.tail:
            self.tail.next = None
        else:
            self.head = None 

        self.count -= 1
        return data

    def pop_front(self) -> T:
        
        if self.empty:
            raise IndexError("Cannot pop from an empty linked list.")

        data = self.head.data

        self.head = self.head.next
        if self.head:
            self.head.previous = None
        else:
            self.tail = None 

        self.count -= 1
        return data

    @property
    def front(self) -> T:
        
        if self.empty:
            raise IndexError("Linked list is empty; no front element.")
        return self.head.data

    @property
    def back(self) -> T:
        
        if self.empty:
            raise IndexError("Linked list is empty; no back element.")
        return self.tail.data

    @property
    def empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0
        
    def __contains__(self, item: T) -> bool:
        if not isinstance(item, self.data_type):
            raise TypeError(f"Item {item} is not of data type {self.data_type}")

        travel = self.head
        while travel:
            if travel.data == item:
                return True
            travel = travel.next
        return False
        
    #def __iter__(self) -> ILinkedList[T]:  # original version given in file
    def __iter__(self) -> Iterator[T]:      # changed version from class (change in ilinkedlist.py too!!)
        self.travel_node = self.head
        return self                     # returning our current instance of the linked list back

    def __next__(self) -> T:
        
        if self.travel_node is None:
            raise StopIteration
        
        data = self.travel_node.data
        self.travel_node = self.travel_node.next    # Advances the node
        return data

        #Explanation written on board:
        #linked_list = LinkedList.from_sequence([1,2,3], int)  # next would go through each [1, 2, 3]
        #print(next(linked_list)) -> 1      
        #for item in linked_list:
            #print(item)

    def __reversed__(self) -> ILinkedList[T]:
        travel = self.tail  # Start from the end of the list
        while travel:
            yield travel.data
            travel = travel.previous
            
    def __eq__(self, other: object) -> bool:
        
        if not isinstance(other, LinkedList):
            return False

        if self.count != other.count:
            return False

        travel_self = self.head
        travel_other = other.head

        while travel_self:
            if travel_self.data != travel_other.data:
                return False
            travel_self = travel_self.next
            travel_other = travel_other.next

        return True

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
