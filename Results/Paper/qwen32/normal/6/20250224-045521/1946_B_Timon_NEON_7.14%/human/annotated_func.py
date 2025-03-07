#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the result of number % 1000000007, which is the remainder when the integer 'number' is divided by 1000000007.
#Overall this is what the function does:The function accepts an integer `number` and returns the remainder when `number` is divided by 1000000007.

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
        
    #State: `arr` is a list of integers, `new_segment` is either an empty list or the last segment of non-negative numbers with its starting index, `max_segment` is `[sum(arr), 0]`, `segments_variants` contains all segments that ended with a negative number, and `max_sum` is -1.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0]:
            total_max_segment = segment
        
    #State: `total_max_segment` is the segment with the maximum sum from `segments_variants`.
    if (len(total_max_segment) == 1) :
        total_max_segment = [-1]
    #State: `total_max_segment` is the segment with the maximum sum from `segments_variants`. If the length of `total_max_segment` is 1, then `total_max_segment` is `[-1]`. Otherwise, `total_max_segment` retains its original value.
    return total_max_segment
    #The program returns `total_max_segment`. If the length of `total_max_segment` is 1, it is `[-1]`. Otherwise, it retains its original value.
#Overall this is what the function does:The function `func_2` takes a list of integers as input and returns a segment (a sublist) with the maximum sum of its elements. If no non-negative segment exists, it returns `[-1]`. The segment is represented as a list containing the sum of the segment and its starting and ending indices in the original list.

#State of the program right berfore the function call: number is a list of integers, and quantity is a non-negative integer representing the number of operations that can be performed.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` accepts a list of integers `number` and a non-negative integer `quantity`. It performs up to `quantity` operations on the list `number` and returns the modified list.

