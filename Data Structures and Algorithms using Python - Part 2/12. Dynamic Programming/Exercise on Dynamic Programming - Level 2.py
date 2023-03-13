
def max_sum_is(num_list):
    #Remove pass and write your logic here
    n = len(num_list)
    max = 0
    msis = [0 for x in range(n)]
 
    for i in range(n):
        msis[i] = num_list[i]
 
    for i in range(1, n):
        for j in range(i):
            if (num_list[i] > num_list[j] and
                msis[i] < msis[j] + num_list[i]):
                msis[i] = msis[j] + num_list[i]
    print(msis)

    for i in range(n):
        if max < msis[i]:
            max = msis[i]
 
    return max


#Pass different values to the function and test your program
num_list=[1, 101, 2, 3, 100, 4, 5]
print("Sum of the maximum sum increasing subsequence is :" ,max_sum_is(num_list))
