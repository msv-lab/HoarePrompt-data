#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the result of number % 1000000007
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
        
    #State: arr is a list of integers; new_segment is [5, 6]; max_segment is [7, 4]; segments_variants is [[3, 1], [7, 4]]; max_sum is -1.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0]:
            total_max_segment = segment
        
    #State: arr is a list of integers; new_segment is [5, 6]; max_segment is [7, 4]; segments_variants is [[3, 1], [7, 4], [7, 4, len(arr) - 1], [5, 6, len(arr) - 1]]; max_sum is -1; total_max_segment is [7, 4]
    if (len(total_max_segment) == 1) :
        total_max_segment = [-1]
    #State: arr is a list of integers; new_segment is [5, 6]; max_segment is [7, 4]; segments_variants is [[3, 1], [7, 4], [7, 4, len(arr) - 1], [5, 6, len(arr) - 1]]; max_sum is -1. If the length of total_max_segment is 1, then total_max_segment is [-1]. Otherwise, total_max_segment remains [7, 4].
    return total_max_segment
    #The program returns [7, 4]
#Overall this is what the function does:The function accepts a list of integers and returns a list containing the maximum sum of a contiguous subarray and its ending index. If no positive sum is found, it returns `[-1]`.

#State of the program right berfore the function call: number is an integer representing the length of the array, and quantity is a non-negative integer representing the number of operations.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` takes two parameters: `number`, an integer representing the length of an array, and `quantity`, a non-negative integer representing the number of operations. It initializes a variable `answer` to 0 and performs operations based on these inputs, ultimately returning the value of `answer`.

