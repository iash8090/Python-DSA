
def swap(num_list, first_index, second_index):
    #Remove pass and write your logic here
    #As python lists are mutable, num_list need not be returned after swapping
    x=num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=x
    return num_list


#Pass different values to the function and test your program
num_list=[2,3,89,45,67]
print("List before swapping:",num_list)
swap(num_list, 1, 2)
print("List after swapping:",num_list)
