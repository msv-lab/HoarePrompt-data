#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder of the integer 'number' divided by 1000000007
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
        
    #State: `arr` remains the same; `new_segment` is either empty or contains the last segment of non-negative integers; `max_segment` contains the segment with the maximum sum and its last index; `segments_variants` contains all the segments encountered; `max_sum` remains -1.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0]:
            total_max_segment = segment
        
    #State: `arr` remains the same; `new_segment` is either empty or contains the last segment of non-negative integers; `max_segment` contains the segment with the maximum sum and its last index; `segments_variants` contains all the segments encountered and now includes `max_segment + [len(arr) - 1]` and `new_segment + [len(arr) - 1]`; `max_sum` remains -1; `total_max_segment` is the segment with the maximum sum among all segments in `segments_variants`.
    if (len(total_max_segment) == 1) :
        total_max_segment = [-1]
    #State: `arr` remains the same; `new_segment` is either empty or contains the last segment of non-negative integers; `max_segment` contains the segment with the maximum sum and its last index; `segments_variants` contains all the segments encountered and now includes `max_segment + [len(arr) - 1]` and `new_segment + [len(arr) - 1]`; `max_sum` remains -1; if `total_max_segment` is `[-1]`, it indicates that the maximum segment length is 1; otherwise, `total_max_segment` is the segment with the maximum sum among all segments in `segments_variants`.
    return total_max_segment
    #The program returns `total_max_segment`, which is either `[-1]` indicating the maximum segment length is 1, or the segment with the maximum sum among all segments in `segments_variants`.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and returns a segment (sublist) from `arr` that has the maximum sum among all possible contiguous sublists. If all elements are negative, it returns `[-1]` indicating that the maximum segment length is 1.

#State of the program right berfore the function call: number is an integer representing the length of the array, and quantity is a non-negative integer representing the number of operations.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` accepts two parameters: `number`, an integer representing the length of an array, and `quantity`, a non-negative integer representing the number of operations. It returns a result based on the specified operations performed on an array of the given length.

