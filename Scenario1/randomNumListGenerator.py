import argparse
import random

def genRandomList(num_range):
    """Summary: Generates list of numbers in a random order.

    Parameters:
    num_range (int): Range of number

    Returns:
    list:List of numbers
    """
    nums = []
    
    # will create a list of number
    for i in range(1,num_range+1):
        nums.append(str(i))

    # arranges the elements in the list randonmly
    random.shuffle(nums)
    
    return nums

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Random number generator')
    parser.add_argument("-r", "--Range",  default=10, type=int, help = "Specify range for generating a list,\
                                                            Default value is set 10 if no value is passed")
    args = parser.parse_args()
    print(" ".join(genRandomList(int(args.Range))))