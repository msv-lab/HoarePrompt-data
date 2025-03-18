#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder of the integer 'number' when divided by 1000000007.
#Overall this is what the function does:The function `func_1` accepts an integer `number` and returns the remainder of `number` when divided by 1000000007. The input `number` is not modified.

#State of the program right berfore the function call: arr is a list of integers such that -10^9 <= arr[i] <= 10^9 for all 0 <= i < len(arr).
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
        
    #State: `new_segment` is an empty list, `max_segment` is the segment with the highest sum encountered during the loop, `segments_variants` is a list of segments (each segment represented as a list of [sum, start_index, end_index]) that were considered as potential max segments, and `max_sum` is -1.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0] and len(segment) != 1:
            total_max_segment = segment
        
    #State: Output State: `new_segment` is an empty list, `max_segment` is the segment with the highest sum encountered during the loop, `segments_variants` is a list of segments that were considered as potential max segments, and now includes an additional segment which is `max_segment` with the end index `len(arr) - 1` appended to it, `max_sum` is -1, `total_max_segment` is the segment from `segments_variants` with the smallest starting index that is greater than the starting index of the current `total_max_segment` and has a length greater than 1. If no such segment exists, `total_max_segment` remains `[-1]`.
    return total_max_segment
    #The program returns the segment from `segments_variants` with the smallest starting index that is greater than the starting index of the current `total_max_segment` and has a length greater than 1. If no such segment exists, the program returns `[-1]`.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and returns a segment of `arr` that has the highest sum. The segment is represented as a list containing the sum of the segment, the starting index, and the ending index. If the list `arr` is empty or all elements are negative, the function returns `[-1]`.

#State of the program right berfore the function call: number is an integer, and quantity is a non-negative integer.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` accepts two parameters, `number` and `quantity`, where `number` is an integer and `quantity` is a non-negative integer. It returns a list containing `quantity` elements, each of which is the value of `number`. The function does not modify the input parameters.

