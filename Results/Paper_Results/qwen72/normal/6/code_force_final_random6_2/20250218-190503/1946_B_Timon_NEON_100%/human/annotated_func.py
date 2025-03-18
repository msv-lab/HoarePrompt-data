#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder of the integer 'number' when divided by 1000000007.
#Overall this is what the function does:The function `func_1` accepts an integer `number` and returns the remainder of `number` when divided by 1000000007. The input `number` is not modified.

#State of the program right berfore the function call: arr is a list of integers where -10^9 <= arr[i] <= 10^9 for all 0 <= i < len(arr).
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
        
    #State: After the loop executes all iterations, `i` is `len(arr) - 1`, `max_sum` is -1, `new_segment` is an empty list if the last element of `arr` is negative, otherwise it is `[sum of all non-negative elements from the last segment, index of the last non-negative element]`. `max_segment` is `[sum of the maximum segment of non-negative elements, starting index of the maximum segment]`. `segments_variants` is a list of lists, each containing the sum of a segment of non-negative elements, the starting index of the segment, and the ending index of the segment.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0] and len(segment) != 1:
            total_max_segment = segment
        
    #State: `i` is `len(arr) - 1`, `max_sum` is -1, `new_segment` is an empty list if the last element of `arr` is negative, otherwise it is `[sum of all non-negative elements from the last segment, index of the last non-negative element]`, `max_segment` is `[sum of the maximum segment of non-negative elements, starting index of the maximum segment]`, `segments_variants` is a list of lists containing the sum of each segment of non-negative elements, the starting index of the segment, and the ending index of the segment, with the last element being `max_segment` followed by `len(arr) - 1`. `total_max_segment` is the segment from `segments_variants` with the highest sum of non-negative elements, provided its length is not 1. If no such segment exists, `total_max_segment` remains `[-1]`.
    return total_max_segment
    #The program returns the segment from `segments_variants` with the highest sum of non-negative elements, provided its length is not 1. If no such segment exists, the program returns `[-1]`.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and returns a segment from the list that has the highest sum of non-negative elements, provided the segment contains more than one element. The segment is represented as a list containing the sum of the segment, the starting index, and the ending index. If no such segment exists, the function returns `[-1]`.

#State of the program right berfore the function call: number is an integer, and quantity is a non-negative integer.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` accepts two parameters, `number` and `quantity`, where `number` is an integer and `quantity` is a non-negative integer. It returns a single integer value, which is always 0, regardless of the input parameters. The function does not modify the input parameters and has no side effects.

