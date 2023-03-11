
# Method 1

def last_instance( num_list,  start,  end,  key):
    #Remove pass and write your logic here
    count=0
    index=0
    if key in num_list:
        index=num_list.index(key)
    if index:
        count=num_list.count(key)
    if index == None:
        return -1
    return index+count-1


num_list=[1,1,2,2,3,4,5,5,5,5]
start=0
end=len(num_list)-1
key=5 #Number to be searched
#Pass different values for num_list, start,end and key and test your program
result=last_instance(num_list, start,end,key)

if(result!=-1):
    print("The index position of the last occurrence of the number:",result)
else:
    print("Number not found")
    

# Method 2
'''
def last_instance( num_list,  start,  end,  key):
    #Remove pass and write your logic here
    index=0
    for i in range(start,end+1):
        if key==num_list[i]:
            index = i
    if index > 0:
        return index
    return -1
'''