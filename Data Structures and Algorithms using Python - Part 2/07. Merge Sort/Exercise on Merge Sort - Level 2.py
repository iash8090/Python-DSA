
def merge_sort(num_list):
    # Remove pass and write the logic here to return the sorted list
    low=0
    high=len(num_list)-1
    if low==high:
        return num_list
    else:
        mid=len(num_list)//2
#        mid=low+(high-low)//2   # another method to find middle value
        print('mid index , value ', mid, num_list[mid])
        left_list=num_list[:mid]
        right_list=num_list[mid:]
        print('left list ', left_list)
        print('right list ', right_list)
        list1=merge_sort(left_list)
        list2=merge_sort(right_list)
        sorted_list= merge(list1,list2)
        print('Sorted lst ', sorted_list)
        print(" ")
        return sorted_list

def merge(left_list,right_list):
    # Remove pass and write the logic to merge the elements in the left_list and right_list and return the sorted list
    i,j=0,0
    sorted_list=[]
    print('left list ',left_list)
    print('right list ', right_list)
    while(i<len(left_list) and j<len(right_list)):
        if left_list[i]<right_list[j]:
            sorted_list.append(left_list[i])
            i+=1
        else:
            sorted_list.append(right_list[j])
            j+=1
    if i<len(left_list):
        sorted_list.extend(left_list[i::])
    if j<len(right_list):
        sorted_list.extend(right_list[j::])
    return sorted_list

num_list=[34, 67, 8, 19, 2, 23, 1, 91]
print("Before sorting:",num_list)
sorted_list = merge_sort(num_list)
print("After sorting:",sorted_list)
