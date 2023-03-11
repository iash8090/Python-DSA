
def find_decreasing_start(list1,start,end):
    #Remove pass and write your logic here
    while start < end:
        if list1[start] > list1[start+1]:
                return start+1
                break
        start+=1

#Use different values for list1 and test your program
list1=[1,4,7,8,9,5,4]
start=0
end=len(list1)-1
result=find_decreasing_start(list1,start,end)
print("The index position at which the increasing array starts decreasing is:",result)