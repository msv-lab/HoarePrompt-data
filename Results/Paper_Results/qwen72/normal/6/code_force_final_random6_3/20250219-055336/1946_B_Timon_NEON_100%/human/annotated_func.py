#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder of the integer 'number' when divided by 1000000007.
#Overall this is what the function does:The function `func_1` accepts an integer `number` and returns the remainder of `number` when divided by 1000000007. The input `number` remains unchanged.

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
        
    #State: `arr` is a list of integers such that -10^9 <= arr[i] <= 10^9 for all 0 <= i < len(arr), `i` is len(arr) - 1, `max_sum` is -1, `new_segment` is an empty list or a list containing the sum of the last segment of non-negative numbers and the starting index of this segment, `max_segment` is a list containing the maximum sum of any segment of non-negative numbers found during the loop and the starting index of this segment, and `segments_variants` is a list of lists, each containing the sum of a segment of non-negative numbers, the starting index of this segment, and the ending index of this segment.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0] and len(segment) != 1:
            total_max_segment = segment
        
    #State: `arr` is a list of integers such that -10^9 <= arr[i] <= 10^9 for all 0 <= i < len(arr), `i` is len(arr) - 1, `max_sum` is -1, `new_segment` is a list containing the sum of the last segment of non-negative numbers and the starting index of this segment, `max_segment` is a list containing the maximum sum of any segment of non-negative numbers found during the loop and the starting index of this segment, `segments_variants` is a list of lists, each containing the sum of a segment of non-negative numbers, the starting index of this segment, and the ending index of this segment, and `total_max_segment` is the segment in `segments_variants` with the highest sum, provided that the segment has more than one element. If no such segment is found, `total_max_segment` remains [-1].
    return total_max_segment
    #The program returns the segment in `segments_variants` with the highest sum, provided that the segment has more than one element. If no such segment is found, the program returns `[-1]`.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and returns the segment with the highest sum from the list of segments that contain at least one non-negative number, where each segment is represented as a list containing the sum of the segment, the starting index, and the ending index. If no such segment is found, the function returns `[-1]`. The input list `arr` remains unchanged.

#State of the program right berfore the function call: number is an integer, and quantity is a non-negative integer.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` accepts two parameters, `number` and `quantity`, where `number` is an integer and `quantity` is a non-negative integer. It returns a list containing `quantity` elements, each of which is the value of `number`. The function does not modify the input parameters.

