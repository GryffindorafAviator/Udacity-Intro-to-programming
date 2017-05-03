# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    max = 0
    list_len = len(list_of_numbers)
    i = 0
    while i < list_len:
        if list_of_numbers[i] > max:
            max = list_of_numbers[i]
        i += 1
    return max




print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0
