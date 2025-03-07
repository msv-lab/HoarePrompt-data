#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder when 'number' is divided by 1000000007
#Overall this is what the function does:The function accepts an integer `number` and returns the remainder when `number` is divided by 1000000007.

#State of the program right berfore the function call: arr is a list of integers where each element is within the range [-10^9, 10^9].
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
        
    #State: Output State: `max_sum` is the maximum sum of any contiguous subarray found in `arr`, `arr` is the list of integers, `new_segment` is an empty list, `max_segment` is the subarray with the maximum sum found, `segments_variants` is a list of all subarrays that have the maximum sum found during the iterations.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0]:
            total_max_segment = segment
        
    #State: Output State: `max_sum` is the maximum sum of any contiguous subarray found in `arr`, `arr` is the list of integers, `new_segment` is an empty list, `max_segment` is the subarray with the maximum sum found, `segments_variants` is a list containing `max_segment + [len(arr) - 1]` and `new_segment + [len(arr) - 1]`, `total_max_segment` is the subarray from `segments_variants` with the highest starting index.
    if (len(total_max_segment) == 1) :
        total_max_segment = [-1]
    #State: `max_sum` is the maximum sum of any contiguous subarray found in `arr`, `arr` is the list of integers, `new_segment` is an empty list, `max_segment` is the subarray with the maximum sum found, `segments_variants` is a list containing `max_segment + [len(arr) - 1]` and `new_segment + [len(arr) - 1]`, `total_max_segment` is the subarray from `segments_variants` with the highest starting index. If `len(total_max_segment) == 1`, then `total_max_segment` is set to `[-1]`.
    return total_max_segment
    #The program returns the subarray from `segments_variants` with the highest starting index. If `len(total_max_segment) == 1`, then `total_max_segment` is set to `[-1]`
#Overall this is what the function does:The function accepts a list of integers `arr` and returns the subarray with the highest starting index that has the maximum sum among all contiguous subarrays in `arr`. If no such subarray exists (i.e., `total_max_segment` contains only one element), it returns `[-1]`.

#State of the program right berfore the function call: number is an integer representing the sum of the original array, and quantity is a non-negative integer representing the number of operations (k).
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function processes an integer `number` representing the sum of the original array and a non-negative integer `quantity` representing the number of operations. After processing, it sets the variable `answer` to 0. The function does not return any value but modifies the local variable `answer`.

