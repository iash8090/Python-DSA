
def swap(num_list, first_index, second_index):
    #Remove pass and copy the code written earlier for this function
    x = num_list[first_index]
    num_list[first_index] = num_list[second_index]
    num_list[second_index] = x
    return num_list


def find_next_min(num_list,start_index):
    #Remove pass and copy the code written earlier for this function
    minimum=start_index
    for i in range(start_index,len(num_list)):
        if num_list[i] < num_list[minimum]:   # Change the sign to '>', to get list in descending order
            minimum=i
    return minimum

def selection_sort(num_list):
    #Remove pass and implement the selection sort algorithm to sort the elements of num_list in ascending order
    for i in range(len(num_list)):
        minimum=find_next_min(num_list,i)
        new_list=swap(num_list,i,minimum)
    return new_list

#Pass different values to the function and test your program
num_list=[8,2,19,34,23, 67, 91]
print("Before sorting;",num_list)
selection_sort(num_list)
print("After sorting:",num_list)