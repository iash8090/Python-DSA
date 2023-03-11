

def merge_list(list1, list2):
    merged_data=""
    list2.reverse()
    for i in range(len(list1)):
        if list1[i] is None:
            merged_data += list2[i]+ " "
        elif list2[i] is None:
            merged_data += list1[i]+ " "
        else:
            merged_data += list1[i]+list2[i]+ " "
    return merged_data[:-1]   # Removing Last element, that is space

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)

print('-----------------')
# Additional
# Sorting List According to length
print("Sorting list1 according to length of characters")
list1.sort(key=lambda x: len(x))
# Reversing the list
list1 = list1[::-1]     # Method 1
#list1.reverse()         # Method 2
print(list1)



# Method 2
'''
    for i in list1:
        for j in list2[::-1]:
            if i is None:
                i=''
            elif j is None:
                j=''
            merged_data+=i+j+' '
            list2.pop(-1)
            break
    return merged_data[:-1]
'''

# Method 3
'''
    for x, y in zip(list1, list2[::-1]):
        if y and x:
            s += x + y
        elif x:
            s += x
        elif y:
            s += y
        s += ' '
    return s[:-1]
'''

# Method 4
'''
    merged_data=""
    j=len(list1)-1
    for i in range(len(list1)):
        str1=str2=""
        if list1[i]:
            str1 = list1[i]
        if list2[j]:
            str2 = list2[j]
        j-=1
        merged_data+=str1+str2
        if i<len(list1)-1:
            merged_data+=" "
    return merged_data
'''
