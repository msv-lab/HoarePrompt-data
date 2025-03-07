#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the result of number modulo 1000000007
#Overall this is what the function does:The function accepts an integer parameter `number` and returns the result of `number` modulo 1000000007.

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
        
    #State: arr: [original list of integers], new_segment: [sum of last non-negative segment, start index] or [], max_segment: [max sum of any segment, start index], segments_variants: [[sum of segment, start index], ...], max_sum: -1.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0] and len(segment) != 1:
            total_max_segment = segment
        
    #State: `arr` is [1, -2, 3, 4, -1], `new_segment` is [7, 2], `max_segment` is [7, 2], `segments_variants` is [[7, 2, 4], [another_segment]], `max_sum` is -1, `total_max_segment` is [7, 2]
    return total_max_segment
    #The program returns total_max_segment which is [7, 2]
#Overall this is what the function does:The function `func_2` accepts a list of integers and returns a list containing the maximum sum of a contiguous non-negative subarray and the starting index of that subarray.

#State of the program right berfore the function call: number is a list of integers representing the array a, and quantity is an integer representing the number of operations k.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function accepts a list of integers and an integer representing the number of operations. It performs some operations on the list based on the given number of operations and returns a single integer value as the result.

