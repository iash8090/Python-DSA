'''
The Rotary club has planned to organize several events on the Women’s day. The volunteers are given a list of activities and the starting time and ending time of those activities.
Write a python function which accepts the activity list, start_time list and finish_time list. The function should find out and return the list of maximum number of activities that can be performed by a single person.
Assume that a person can work only on a single activity at a time. If an activity performed by a person ends at x unit time then he/she can take up the next activity which is starting at any time greater than or equal to x+1.

Refer table below for sample input and expected output:
----------------------------------------------------------------------------
Sample Input                                                Expected Output
activity_list - [1, 2, 3, 4, 5, 6]
start_time_list = [1, 3, 0, 5, 8, 5]                        [1, 2, 4, 5]
finish_time_list = [2, 4, 6, 7, 9, 9]
----------------------------------------------------------------------------
activity_list - [1, 2, 3, 4, 5, 6]
start_time_list = [5, 4, 8, 2, 3, 1]                        [6, 1]
finish_time_list = [13, 6, 16, 7, 5, 4]
----------------------------------------------------------------------------

'''


def find_maximum_activities(activity_list, start_time_list, finish_time_list):
    # Remove pass and write your logic here
    activities=[]
    zipped = zip(activity_list,start_time_list,finish_time_list)
    mapped_list = list(zipped)
    mapped_list.sort(key= lambda x: x[1])
    print("after ",mapped_list)
    for i in range(len(mapped_list)):
        l=[mapped_list[i]]   # At Every iteration creating new list
        print(l)
        for index,activity in enumerate(mapped_list):
            if index>i:
                if activity[1]>l[len(l)-1][2]:
                    l.append(activity)
        activities.append(l)
    activities.sort(key=lambda x:len(x), reverse=True)
    print("these are activities ",activities)
    x=[]
    for i in activities[0]:
        x.append(i[0])
    return x



# Pass different values to the function and test your program
activity_list = [1, 2, 3, 4, 5, 6]
start_time_list = [1, 3, 0, 5, 8, 5]
finish_time_list = [2, 4, 6, 7, 9, 9]
print("Activities:", activity_list)
print("Start time of the activities:", start_time_list)
print("Finishing time of the activities:", finish_time_list)

result = find_maximum_activities(activity_list, start_time_list, finish_time_list)
print("The maximum set of activities that can be completed:", result)
