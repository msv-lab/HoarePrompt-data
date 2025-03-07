#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the result of number % 1000000007
#Overall this is what the function does:The function takes an integer as input and returns the remainder when that integer is divided by 1,000,000,007.

#State of the program right berfore the function call: arr is a list of integers.
def func_2(arr):
    new_segment = []
    max_segment = [0, 0]
    segments_variants = []
    max_sum = -1
    for i in range(len(arr)):
        if new_segment:
            if arr[i] < 0:
                if max_segment[0] > new_segment[0]:
                    segments_variants.append(max_segment + [i - 1])
                else:
                    segments_variants.append(new_segment + [i - 1])
                    max_segment = new_segment
                new_segment = []
                max_segment[0] += arr[i]
            else:
                max_segment[0] += arr[i]
                new_segment[0] += arr[i]
        else:
            if arr[i] >= 0:
                new_segment = [arr[i], i]
            max_segment[0] += arr[i]
        
    #State: arr is a list of integers; new_segment is an empty list; max_segment is [sum of the last segment, end index of the last segment]; segments_variants is a list of all considered segments; max_sum is -1.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0]:
            total_max_segment = segment
        
    #State: `arr` is a list of integers; `new_segment` is an empty list; `max_segment` is [sum of the last segment, end index of the last segment]; `segments_variants` is a list of all considered segments including `max_segment + [len(arr) - 1]` and `[len(arr) - 1]`; `max_sum` is -1; `total_max_segment` is the segment with the maximum sum from `segments_variants`.
    if (len(total_max_segment) == 1) :
        total_max_segment = [-1]
    #State: `arr` is a list of integers; `new_segment` is an empty list; `max_segment` is [sum of the last segment, end index of the last segment]; `segments_variants` is a list of all considered segments including `max_segment + [len(arr) - 1]` and `[len(arr) - 1]`; `max_sum` is -1; if `total_max_segment` has a length of 1, then `total_max_segment` is [-1]. Otherwise, `total_max_segment` remains unchanged.
    return total_max_segment
    #The program returns `total_max_segment`. If `total_max_segment` has a length of 1, then it is `[-1]`. Otherwise, `total_max_segment` remains unchanged.
#Overall this is what the function does:The function accepts a list of integers and returns a segment (sublist) with the maximum sum. If no positive sum segment is found, it returns `[-1]`.

#State of the program right berfore the function call: number is a list of integers, and quantity is a non-negative integer.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function takes a list of integers and a non-negative integer as input. It returns a sublist containing the first `quantity` elements from the list. If `quantity` exceeds the length of the list, the entire list is returned.

