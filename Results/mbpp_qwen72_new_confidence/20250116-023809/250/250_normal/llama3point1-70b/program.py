import math

def perfect_squares(start, end):
    perfect_squares_list = []
    for num in range(start, end + 1):
        sqrt_num = math.sqrt(num)
        if sqrt_num == int(sqrt_num):
            perfect_squares_list.append(num)
    return perfect_squares_list
