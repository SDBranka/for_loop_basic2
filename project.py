#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".   Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
print("---Biggie Size---")

# def biggie_size(a_list):
#     for val in a_list:
#         if(int(val) > -1):
#             val = "big"
#     return a_list

def biggie_size(a_list):
    for x in range(len(a_list)):
        if(a_list[x] > -1):
            a_list[x] = "big"
    return a_list

x = [-1, 3, 5, -5]
y = biggie_size(x)
print(y)
    
    
#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).   Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
print("\n\n---Count Positives---")

def count_positives(a_list):
    count = 0
    for x in range(len(a_list)):
        if(a_list[x] > 0):
            count += 1
    a_list[x] = count
    return a_list

x = [-1,1,1,1]
y = count_positives(x)
print(y)

    
#Sum Total - Create a function that takes a list and returns the sum of all the values in the array.    Example: sum_total([1,2,3,4]) should return 10  Example: sum_total([6,3,-2]) should return 7
print("\n\n---Sum Total---")

def sum_total(a_list):
    sum = 0
    for val in a_list:
        sum += val

    return sum

x = [1,2,3,4]
y = sum_total(x)
print(y)

#Average - Create a function that takes a list and returns the average of all the values.   Example: average([1,2,3,4]) should return 2.5
print("\n\n---Average---")

def average(a_list):
    sum = 0
    
    for val in a_list:
        sum += val
    
    return sum / len(a_list)

x = [1,2,3,4]
y = average(x)
print(y)
    
    
#Length - Create a function that takes a list and returns the length of the list.    Example: length([37,2,1,-9]) should return 4   Example: length([]) should return 0
print("\n\n---Length---")

def length(a_list):
    return len(a_list)

# x = [37,2,1,-9]
x = []
y = length(x)
print(y)


#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.   Example: minimum([37,2,1,-9]) should return -9  Example: minimum([]) should return False
print("\n\n---Minimum---")

def minimum(a_list):
    if(len(a_list) == 0):
        return False
    
    min = a_list[0]
    
    for val in a_list:
        if(val < min):
            min = val

    return min

x = [37,2,1,-9, 24]
# x = []
y = minimum(x)
print(y)


#Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.     Example: maximum([37,2,1,-9]) should return 37     Example: maximum([]) should return False
print("\n\n---Maximum")

def maximum(a_list):
    if(len(a_list) == 0):
        return False
    
    max = a_list[0]

    for val in a_list:
        if(val > max):
            max = val

    return max

x = [37,2,1,-9]
# x = []
y = maximum(x)
print(y)


#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.   Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
print("\n\n---Ultimate Analysis---")

def ultimate_analysis(a_list):

    
    
x = [37,2,1,-9]
y = ultimate_analysis(x)
print(y)

#Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)  Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
