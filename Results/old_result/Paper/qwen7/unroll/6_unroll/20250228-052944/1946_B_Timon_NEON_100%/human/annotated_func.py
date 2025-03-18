#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder when the integer `number` is divided by 1000000007
#Overall this is what the function does:The function accepts an integer `number` and returns the remainder when `number` is divided by 1000000007.

#State of the program right berfore the function call: arr is a list of integers where each element is in the range [-10^9, 10^9].
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
        
    #State: Output State: `max_sum` is the maximum sum of any contiguous subarray found in `arr`, `arr` is the list of integers provided, `new_segment` is an empty list, `max_segment` is the last segment considered before finding a new one with a potentially higher sum, `segments_variants` is a list of all segments that had the highest sum at some point during the loop's execution.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0] and len(segment) != 1:
            total_max_segment = segment
        
    #State: Output State: `max_sum` is the maximum sum of any contiguous subarray found in `arr`, `arr` is the list of integers provided, `new_segment` is an empty list, `max_segment` is the last segment considered before finding a new one with a potentially higher sum, `segments_variants` is a list of all segments that had the highest sum at some point during the loop's execution, and `segments_variants` now includes `max_segment + [len(arr) - 1]; total_max_segment` is the segment with the maximum length among all segments in `segments_variants` that has the highest sum.
    return total_max_segment
    #`total_max_segment` which is the segment with the maximum length among all segments in `segments_variants` that has the highest sum
#Overall this is what the function does:The function accepts a list of integers `arr` and returns the segment with the maximum length that has the highest sum among all possible segments. It iterates through the list, tracking potential segments and their sums, and finally selects the segment with both the highest sum and maximum length from all tracked segments.

#State of the program right berfore the function call: number is an integer representing the sum of the original array, and quantity is a non-negative integer representing the number of operations (k) that can be performed on the array.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function accepts an integer `number` representing the sum of an array and a non-negative integer `quantity` representing the number of operations that can be performed on the array. It returns `0` if `number` is less than or equal to `quantity`, otherwise it returns `number`.

