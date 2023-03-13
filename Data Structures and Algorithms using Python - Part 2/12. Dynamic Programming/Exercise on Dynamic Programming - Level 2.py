
def max_sum_is(num_list):
    #Remove pass and write your logic here
    n = len(num_list)
    new_list=num_list[:]
    for i in range(1, n):
        for j in range(i):
            if (num_list[j] < num_list[i] and new_list[i] < new_list[j] + num_list[i]):
                new_list[i] = new_list[j] + num_list[i]
    print(new_list)
    m=max(new_list) 
    return m

#Pass different values to the function and test your program
num_list=[1, 101, 2, 3, 100, 4, 5]
print("Sum of the maximum sum increasing subsequence is :" ,max_sum_is(num_list))
