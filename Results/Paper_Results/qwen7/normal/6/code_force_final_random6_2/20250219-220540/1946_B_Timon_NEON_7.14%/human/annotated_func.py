#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder when the integer 'number' is divided by 1000000007.
#Overall this is what the function does:The function `func_1` accepts an integer `number` and returns the remainder when `number` is divided by 1000000007.

#State of the program right berfore the function call: arr is a list of integers where -10^9 ≤ arr[i] ≤ 10^9 for all 0 ≤ i < len(arr).
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
        
    #State: All iterations completed.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0]:
            total_max_segment = segment
        
    #State: After all iterations of the loop, `segments_variants` will contain all the segments generated during the loop's execution, and `total_max_segment` will hold the segment with the maximum starting point from all the segments in `segments_variants`.
    if (len(total_max_segment) == 1) :
        total_max_segment = [-1]
    #State: `segments_variants` contains all the segments generated during the loop's execution, and if `len(total_max_segment) == 1`, then `total_max_segment` is now [-1].
    return total_max_segment
    #`total_max_segment` which is either the list of segments generated during the loop's execution or [-1] if the length of `total_max_segment` was originally 1
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and returns either the list of segments generated during the loop's execution or `[-1]` if the length of `total_max_segment` was originally 1. The function identifies segments within `arr` where the sum of elements is maximized, considering both positive and negative contributions, and returns the segment with the maximum starting point. If no valid segments are found, it returns `[-1]`.

#State of the program right berfore the function call: number is an integer representing the sum of the original array, and quantity is a non-negative integer representing the number of operations (k).
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function accepts an integer `number` representing the sum of the original array and a non-negative integer `quantity` representing the number of operations. It returns `number` if `number` is greater than or equal to `quantity`, otherwise it returns 0.

