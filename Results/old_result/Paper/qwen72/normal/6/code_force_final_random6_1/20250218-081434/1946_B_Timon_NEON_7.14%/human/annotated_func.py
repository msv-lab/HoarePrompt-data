#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder of the integer 'number' when divided by 1000000007.
#Overall this is what the function does:The function `func_1` accepts an integer `number` and returns the remainder of `number` when divided by 1000000007. The function does not modify the input `number` and the final state of the program is that the function has returned an integer value which is the remainder of the input `number` modulo 1000000007.

#State of the program right berfore the function call: arr is a list of integers where -10^9 <= arr[i] <= 10^9.
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
        
    #State: `arr` is a list of integers where -10^9 <= arr[i] <= 10^9, `i` is `len(arr) - 1`, `max_sum` is -1, `max_segment` is the segment with the highest sum found during the loop, and `segments_variants` is a list of all segments that were considered but not chosen as the `max_segment`. `new_segment` is an empty list if the last element of `arr` is less than 0, otherwise it is a list containing the sum of the last segment and the index of the last element in that segment.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0]:
            total_max_segment = segment
        
    #State: `arr` is a list of integers where -10^9 <= arr[i] <= 10^9, `i` is `len(arr) - 1`, `max_sum` is -1, `max_segment` is the segment with the highest sum found during the loop, `segments_variants` is a list of all segments that were considered but not chosen as the `max_segment`, `new_segment` is a list containing the sum of the last segment and the index of the last element in that segment, and the last element of `arr` is greater than or equal to 0. `total_max_segment` is the segment with the highest sum from all the segments in `segments_variants` that were considered during the loop.
    if (len(total_max_segment) == 1) :
        total_max_segment = [-1]
    #State: *`arr` is a list of integers where -10^9 <= arr[i] <= 10^9, `i` is `len(arr) - 1`, `max_sum` is -1, `max_segment` is the segment with the highest sum found during the loop, `segments_variants` is a list of all segments that were considered but not chosen as the `max_segment`, `new_segment` is a list containing the sum of the last segment and the index of the last element in that segment, and the last element of `arr` is greater than or equal to 0. If `len(total_max_segment)` is 1, `total_max_segment` is updated to `[-1]`. Otherwise, `total_max_segment` remains unchanged.
    return total_max_segment
    #The program returns `total_max_segment`, which is a list. If the length of `total_max_segment` is 1, it will be `[-1]`. Otherwise, `total_max_segment` remains unchanged.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and returns a list `total_max_segment`. This list contains the sum of the maximum sum segment found in `arr` and the start and end indices of this segment. If no valid segment is found (i.e., all elements in `arr` are negative), the function returns `[-1]`.

#State of the program right berfore the function call: number is an integer, and quantity is a non-negative integer.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` accepts two parameters, `number` (an integer) and `quantity` (a non-negative integer), and returns an integer value `answer` which is always 0. The function does not modify the input parameters or perform any actions that affect the program state outside of its scope.

