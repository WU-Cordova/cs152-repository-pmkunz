
#Added in class:
from datastructures.bag import Bag
# command + . on mac, highlighitng Bag?

def main():
    
    #print("Hello, World!")

    # Code added in class:
    bag = Bag()
    bag.add("apple")
    bag.add("pear")
    items = bag.distinct_items()
    print(f"Distinct_items: {items}")
    #######

if __name__ == '__main__':
    main()
