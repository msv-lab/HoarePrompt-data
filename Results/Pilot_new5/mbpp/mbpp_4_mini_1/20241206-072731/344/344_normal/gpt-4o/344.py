import bisect

def right_insertion(sorted_list, value):
    return bisect.bisect_right(sorted_list, value)

# Test cases
assert right_insertion([1,2,4,5],6)==4
assert right_insertion([1,2,4,5],3)==2
assert right_insertion([1,2,4,5],7)==4
