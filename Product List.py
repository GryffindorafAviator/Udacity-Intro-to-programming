# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(list_of_numbers):
    list_len = len(list_of_numbers)
    product = 1
    i = 0
    while i < list_len:
        product = product * list_of_numbers[i]
        i += 1
    return product







print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1
