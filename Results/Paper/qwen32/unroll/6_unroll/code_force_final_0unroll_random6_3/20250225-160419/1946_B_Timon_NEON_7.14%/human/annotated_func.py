#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the result of `number % 1000000007`, which is the remainder when `number` is divided by 1000000007.
#Overall this is what the function does:The function takes an integer as input and returns the remainder when that integer is divided by 1000000007.

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
        
    #State: arr is a list of integers; new_segment is [5, 6]; max_segment is [5, 3]; segments_variants is [[3, 1], [7, 4]]; max_sum is -1.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0]:
            total_max_segment = segment
        
    #State: arr is a list of integers; new_segment is [5, 6]; max_segment is [5, 3]; segments_variants is [[3, 1], [7, 4], [5, 3, len(arr) - 1], [5, 6, len(arr) - 1]]; max_sum is -1; total_max_segment is [7, 4]
    if (len(total_max_segment) == 1) :
        total_max_segment = [-1]
    #State: `arr` is a list of integers; `new_segment` is [5, 6]; `max_segment` is [5, 3]; `segments_variants` is [[3, 1], [7, 4], [5, 3, len(arr) - 1], [5, 6, len(arr) - 1]]; `max_sum` is -1. If the length of `total_max_segment` is 1, then `total_max_segment` is [-1]. Otherwise, `total_max_segment` remains [7, 4].
    return total_max_segment
    #The program returns [7, 4]
#Overall this is what the function does:The function accepts a list of integers and returns a list `[7, 4]` regardless of the input.

#State of the program right berfore the function call: number is an integer representing the length of the array a, and quantity is a non-negative integer representing the number of operations that can be performed.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` takes two parameters: `number`, which represents the length of an array `a`, and `quantity`, which is a non-negative integer indicating the number of operations that can be performed. The function returns a computed value based on these inputs, although the exact computation and return value are not specified in the provided annotations.

