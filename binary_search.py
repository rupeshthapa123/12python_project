import random
import time

def naive_search(l, target):
    """
    It loops through the list, and if it finds the target, it returns the index. If it doesn't find the
    target, it returns -1
    
    :param l: the list to search
    :param target: the value we're looking for
    :return: The index of the target value.
    """
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low=None, high=None):
    """
    If the target is in the list, return its index. Otherwise, return -1.
    
    :param l: the list to search
    :param target: the value we're looking for
    :param low: the lowest index of the list to search
    :param high: the index of the last element in the list
    :return: The index of the target value in the list.
    """
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    
    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)
    
# The above code is generating a list of random numbers and then searching for each number in the list
# using both naive search and binary search.
if __name__=='__main__':
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    # Timing how long it takes to run the naive search algorithm.
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive Search time: ", (end - start)/length, "seconds")

    # Timing how long it takes to run the binary search algorithm.
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds")



