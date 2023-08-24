
def find_minimum_number(cnt_1, cnt_2, x, y):
    # find the maximum number that can be presented to the first friend
    max_num_1 = (cnt_1 - 1) * x
    # find the maximum number that can be presented to the second friend
    max_num_2 = (cnt_2 - 1) * y
    
    # find the minimum number that can be presented to both friends, if any
    min_num_both = min(max_num_1, max_num_2)
    
    # check if there are any numbers that can be presented to both friends
    if min_num_both > 0:
        # return the minimum number that can be presented to both friends plus 1
        return min_num_both + 1
    else:
        # return the maximum number that can be presented to either friend
        return max(max_num_1, max_num_2)

# read input values
cnt_1, cnt_2, x, y = map(int, input().split())

# find the minimum number
minimum_number = find_minimum_number(cnt_1, cnt_2, x, y)

# print the result
print(minimum_number)
