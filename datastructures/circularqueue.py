from typing import Any

from datastructures.array import Array
from datastructures.iqueue import IQueue, T

class CircularQueue(IQueue[T]):
    """ Represents a fixed-size circular queue. The queue
        is circular in the sense that the front and rear pointers wrap around the
        array when they reach the end. The queue is full when the rear pointer is
        one position behind the front pointer. The queue is empty when the front
        and rear pointers are equal. This implementation uses a fixed-size array.
    """

    def __init__(self, maxsize: int = 0, data_type=object) -> None:
        ''' Initializes the CircularQueue object with a maxsize and data_type.
        
            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.maxsize
                5
                >>> q.empty
                True
                >>> q.full
                False
                >>> q.front
                IndexError('Queue is empty')
                >>> q.rear
                IndexError('Queue is empty')

            Arguments:
                maxsize: The maximum size of the queue
                data_type: The type of the elements in the queue
        '''

        if maxsize <= 0:    # Checks that the maxsize value is valid 
            raise ValueError("Maxsize must be a positive integer")

        self._maxsize = maxsize
        self.data_type = data_type

        self.front_index = 0
        self.rear_index = 0
        self._size = 0

        self.circularqueue = Array([data_type()]*maxsize, data_type)    # Initialize an empty array


    def enqueue(self, item: T) -> None:
        ''' Adds an item to the rear of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.front
                1
                >>> q.rear
                3
                >>> q.enqueue(4)
                >>> q.enqueue(5)
                >>> q.full
                True
                >>> q.enqueue(6)
                IndexError('Queue is full')
            
            Arguments:
                item: The item to add to the queue
                
            Raises:
                IndexError: If the queue is full
        '''

        if self.full:
            raise IndexError("Queue is full!")

        self.circularqueue[self.rear_index] = item
        self.rear_index = (self.rear_index + 1) % self._maxsize
        self._size += 1

        
    def dequeue(self) -> T:
        ''' Removes and returns the item at the front of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.dequeue()
                1
                >>> q.dequeue()
                2
                >>> q.dequeue()
                3
                >>> q.dequeue()
                IndexError('Queue is empty')
                >>> q.dequeue()
                IndexError('Queue is empty')

            Returns:
                The item at the front of the queue

            Raises:
                IndexError: If the queue is empty
        '''
        
        if self.empty:
            raise IndexError("Queue is empty.")

        item = self.circularqueue[self.front_index]
        self.front_index = (self.front_index + 1) % self._maxsize
        self._size -= 1
        return item


    ### i added
    def __iter__(self):
        idx = self.front_index
        count = 0
        while count < self._size:
            yield self.circularqueue[idx]
            idx = (idx + 1) % self._maxsize
            count += 1
    ####


    def clear(self) -> None:
        ''' Removes all items from the queue 
        
            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.clear()
                >>> q.empty
                True
                >>> q.front
                IndexError('Queue is empty')
                >>> q.rear
                IndexError('Queue is empty')
        '''
        #self.circularqueue = [None] * self._maxsize
        self.circularqueue = Array([data_type()]*maxsize, data_type)    # Reset array
        self.front_index = 0
        self.rear_index = 0
        self._size = 0

    @property
    def front(self) -> T:
        ''' Returns the item at the front of the queue without removing it

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.front
                1
                >>> q.dequeue()
                1
                >>> q.front
                2
                >>> q.dequeue()
                2
                >>> q.front
                3
                >>> q.dequeue()
                3
                >>> q.front
                IndexError('Queue is empty')

            Returns:
                The item at the front of the queue

            Raises:
                IndexError: If the queue is empty
        '''
        if self.empty:
            raise IndexError("Queue is empty.")
        return self.circularqueue[self.front_index]

    @property
    def full(self) -> bool:
        ''' Returns True if the queue is full, False otherwise 

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.full
                False
                >>> q.enqueue(1)
                >>> q.full
                False
                >>> q.enqueue(2)
                >>> q.full
                False
                >>> q.enqueue(3)
                >>> q.full
                False
                >>> q.enqueue(4)
                >>> q.full
                False
                >>> q.enqueue(5)
                >>> q.full
                True
                >>> q.dequeue()
                1
                >>> q.full
                False
                >>> q.dequeue()
                2
                >>> q.full
                False
                >>> q.dequeue()
                3
                >>> q.full
                False
                >>> q.dequeue()
                4
                >>> q.full
                False
                >>> q.dequeue()
                5
                >>> q.full
                False
        
            Returns:
                True if the queue is full, False otherwise
        '''
        return self._size == self._maxsize

    @property
    def empty(self) -> bool:
        ''' Returns True if the queue is empty, False otherwise

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.empty
                True
                >>> q.enqueue(1)
                >>> q.empty
                False
                >>> q.enqueue(2)
                >>> q.empty
                False
                >>> q.enqueue(3)
                >>> q.empty
                False
                >>> q.enqueue(4)
                >>> q.empty
                False
                >>> q.enqueue(5)
                >>> q.empty
                False
                >>> q.dequeue()
                1
                >>> q.empty
                False
                >>> q.dequeue()
                2
                >>> q.empty
                False
                >>> q.dequeue()
                3
                >>> q.empty
                False
                >>> q.dequeue()
                4
                >>> q.empty
                False
                >>> q.dequeue()
                5
                >>> q.empty
        
            Returns:
                True if the queue is empty, False otherwise
        '''
        return self._size == 0
    
    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.maxsize
                5

            Returns:
                The maximum size of the queue
        '''
        return self._maxsize

    def __eq__(self, other: object) -> bool:
        ''' Returns True if this CircularQueue is equal to another object, False otherwise
        
            Equality is defined as:
                - The element values at the front and rear pointers are equal
                - The element values between the front and rear pointers are equal
                - The maxsize of the queue is equal
                - The data_type of the queue is equal
                - Two queues are equal if they have the same elements in the same order, regardless of the index
                  of the front and rear pointers.

            Examples:
                >>> q1 = CircularQueue(maxsize=5, data_type=int)
                >>> q2 = CircularQueue(maxsize=5, data_type=int)
                >>> q1 == q2
                True
                >>> for i in range(5): q1.enqueue(i)
                >>> for i in range(5): q2.enqueue(i)
                >>> q1 == q2
                True
                >>> q1.dequeue()
                0
                >>> q1 == q2
                False
                
            Arguments:
                other: The object to compare this CircularQueue to
                
            Returns:
                True if this CircularQueue is equal to another object, False otherwise
        '''

        if not isinstance(other, CircularQueue):    # Checks that other object is an instance of CircularQueue
            return False

        if self._size != other._size or self.data_type != other.data_type:  # Checks that the size and data_type are the same in both
            return False

        if self._size != other._size: # Chcecks that the queue sizes are the same
            return False

        i = self.front_index
        j = other.front_index
        for _ in range(self._size):
            if self.circularqueue[i] != other.circularqueue[j]:     # Checks that each element is the same
                return False
            # Use the modulo operator to wrap around, moving to the next index to check
            i = (i + 1) % self._maxsize
            j = (j + 1) % self._maxsize
        return True # if you reach this point, then all the indices were the same, so they are equal
    
    def __len__(self) -> int:
        ''' Returns the number of items in the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> len(q)
                0
                >>> q.enqueue(1)
                >>> len(q)
                1
                >>> q.enqueue(2)
                >>> len(q)
                2
                >>> q.enqueue(3)
                >>> len(q)
                3
                >>> q.dequeue()
                1
                >>> len(q)
                2
                >>> q.dequeue()
                2
                >>> len(q)
                1
                >>> q.dequeue()
                3
                >>> len(q)
                0
        
            Returns:
                The number of items in the queue
        '''
        return self._size

    def __str__(self) -> str:
        ''' Returns a string representation of the CircularQueue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> print(q)
                [1, 2, 3]
        
            Returns:
                A string representation of the queue
        '''
        return str(self.circularqueue)

    def __repr__(self) -> str:
        ''' Returns a developer string representation of the CircularQueue object

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> repr(q)
                'ArrayQueue([1, 2, 3])'
        
            Returns:
                A string representation of the CircularQueue object
        '''
        return f'ArrayQueue({repr(self.circularqueue)})'
                                  
