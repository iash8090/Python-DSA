#DSA-Tryout

import random
from timeit import default_timer as timer

def find_it_linear(num,element_list):
    #remove pass and copy the code written earlier for linear search
    count = 0
    for i in element_list:
        count+=1
        if num == i:
            break
    return count

# Method 1
# Binary search only works on Sorted list of elements
def find_it_binary(num,element_list):
    first= 0
    last= len(element_list) -1
    print("No. to be guessed- ", num)
    print("last index value- ", last)
    count = 0
    while True:
        mid = (first + last) // 2
        print("mid index value- ",mid)
        count += 1
        if num == element_list[mid]:
            break
        if num < element_list[mid]:
            last= mid -1
        elif num >= element_list[mid]:
            first= mid +1
    return count

# Initializes a list with values 1 to n in ascending order and returns it
# Binary search only works on Sorted list of elements
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1,n+1):
        list_of_elements.append(i)
    return list_of_elements

def play(n):
#    list_of_elements=initialize_list_of_elements(n)
    list_of_elements=[i for i in range(4000)]
    rand_index=random.randrange(0,len(list_of_elements))
    rand_num=list_of_elements[rand_index]
    print("Number to be guessed:",rand_num)
    start=timer()
    print("No. of guesses made using linear search:",find_it_linear(rand_num,list_of_elements))
    end=timer()
    print("Linear Search:Execution time in seconds:{0:.5f}".format( (end-start)))
    print("Linear Search:Execution time in seconds: ", (end-start))
    start1=timer()
    print("No. of guesses made using binary search:",find_it_binary(rand_num,list_of_elements))
#    for Method 2
#    print("No. found at index position :",binary_search_recursive(rand_num,list_of_elements,0,len(list_of_elements)-1))
    end1=timer()
    print("Binary Search:Execution time in seconds:{0:.5f}".format( (end1-start1)))
    print("Binary Search:Execution time in seconds: %.5f" %(end1 - start1))
#Pass different values to play() and observe the output
play(40000)

'''
# Time Complexity for Linear Search
# Best      Average     Worst  
# Ω(1)      θ(n)        O(n)

# Time Complexity for Binary Search
# Best      Average     Worst  
# Ω(1)      θ(logn)        O(logn)
'''

# Method 2
# Binary search using Recursion
'''
    
def binary_search_recursive(num,element_list,first,last):
    if last < first:
        return -1

    print("No. to be guessed- ", num)
    print("last index value- ", last)
    count = 0
    mid = (first + last) // 2
    print("mid index value- ", mid)
    count += 1
    if num == element_list[mid]:
        return mid
    if num < element_list[mid]:
        last = mid - 1
    elif num >= element_list[mid]:
        first = mid + 1
    return binary_search_recursive(num,element_list,first,last)
'''