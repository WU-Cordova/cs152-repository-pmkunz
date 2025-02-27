
# #Added in class:
# from datastructures.bag import Bag
# # command + . on mac, highlighitng Bag?

# def main():
    
#     print("Hello, World!")

#     # # Code added in class:
#     # bag = Bag()
#     # bag.add("apple")
#     # bag.add("pear")
#     # items = bag.distinct_items()
#     # print(f"Distinct_items: {items}")

###################################################

from datastructures.bag import Bag
from tests.car import Car

def main():

    data_type = Car
    rows_len, cols_len = 3, 2
    sequence = [[data_type() for _ in range(cols_len)] for _ in range(rows_len)]

    return Array2D(starting_sequence=sequence, data_type=data_type)

    #...
    
if __name__ == '__main__':
    main()
