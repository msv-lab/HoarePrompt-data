#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder when 'number' is divided by 1000000007.
#Overall this is what the function does:The function accepts an integer `number` and returns the remainder when `number` is divided by 1000000007.

#State of the program right berfore the function call: arr is a list of integers, where each element is in the range [-10^9, 10^9].
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
        
    #State: Output State: `max_sum` is the sum of the longest contiguous subarray with non-negative elements, `arr` is the original list of integers, `new_segment` is an empty list, `max_segment` is the subarray with the maximum sum of non-negative elements and its ending index, `segments_variants` is a list of subarrays that have sums greater than or equal to `max_sum`.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0]:
            total_max_segment = segment
        
    #State: Output State: `max_sum` is the sum of the longest contiguous subarray with non-negative elements, `arr` is the original list of integers, `new_segment` is an empty list, `max_segment` is the subarray with the maximum sum of non-negative elements and its ending index, `segments_variants` is a list of subarrays that have sums greater than or equal to `max_sum`, `total_max_segment` is the subarray with the maximum starting index among all subarrays in `segments_variants`.
    if (len(total_max_segment) == 1) :
        total_max_segment = [-1]
    #State: `max_sum` is the sum of the longest contiguous subarray with non-negative elements, `arr` is the original list of integers, `new_segment` is an empty list, `max_segment` is the subarray with the maximum sum of non-negative elements and its ending index, `segments_variants` is a list of subarrays that have sums greater than or equal to `max_sum`, and `total_max_segment` is now [-1] if the length of `total_max_segment` is 1; otherwise, `total_max_segment` remains unchanged.
    return total_max_segment
    #The program returns total_max_segment which is either [-1] if the length of total_max_segment is 1; otherwise, it remains unchanged.
#Overall this is what the function does:The function accepts a list of integers `arr` and returns `total_max_segment`. If the length of `total_max_segment` is 1, it returns \([-1]\); otherwise, it returns `total_max_segment` unchanged. The function identifies the longest contiguous subarray within `arr` that contains non-negative elements and calculates its sum. It then selects the subarray with the maximum starting index among those with the highest sum.

#State of the program right berfore the function call: number is an integer representing the sum of the original array, and quantity is a non-negative integer representing the number of operations k.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function accepts an integer `number` representing the sum of an array and a non-negative integer `quantity` representing the number of operations. It initializes a variable `answer` to 0 and returns the value of `answer` after performing some unspecified operations based on `number` and `quantity`.

