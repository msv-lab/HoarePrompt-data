#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder when 'number' is divided by 1000000007
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
        
    #State: arr: [1, -2, 3, 5, -1, 2], new_segment: [2, 5], max_segment: [11, 0], segments_variants: [[1, 0, 0], [8, 2, 3]], max_sum: -1.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0] and len(segment) != 1:
            total_max_segment = segment
        
    #State: `arr` is [1, -2, 3, 5, -1, 2], `new_segment` is [2, 5], `max_segment` is [11, 0], `segments_variants` is [[1, 0, 0], [8, 2, 3], [11, 0, 5], [2, 5, 5]], `max_sum` is -1, `total_max_segment` is [11, 0, 5].
    return total_max_segment
    #The program returns [11, 0, 5]
#Overall this is what the function does:The function `func_2` accepts a list of integers and returns a list containing the maximum sum of a contiguous subarray, the starting index of that subarray, and the ending index of that subarray.

#State of the program right berfore the function call: number is an integer representing the length of the array a, and quantity is a non-negative integer representing the number of operations that can be performed.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` takes two parameters: `number`, which is an integer representing the length of an array `a`, and `quantity`, which is a non-negative integer representing the number of operations that can be performed. The function returns a value, `answer`, which is computed based on the operations performed on the array `a` given the constraints. The specific computation and return value are not detailed in the provided information.

