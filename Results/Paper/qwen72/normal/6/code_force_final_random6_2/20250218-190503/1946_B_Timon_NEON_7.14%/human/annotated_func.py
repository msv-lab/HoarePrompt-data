#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder of `number` when divided by 1000000007.
#Overall this is what the function does:The function `func_1` accepts an integer `number` and returns the remainder of `number` when divided by 1000000007. The input `number` is not modified.

#State of the program right berfore the function call: arr is a list of integers, where -10^9 <= arr[i] <= 10^9 for all 0 <= i < len(arr).
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
        
    #State: After the loop executes all iterations, `arr` remains a list of integers where -10^9 <= arr[i] <= 10^9 for all 0 <= i < len(arr). `i` is `len(arr) - 1`. `max_segment` contains the maximum sum of a contiguous subarray and the index of the last element of this subarray. `new_segment` is either an empty list or a list containing the sum of the current contiguous subarray and the index of the last element of this subarray. `segments_variants` is a list of lists, each containing the sum of a contiguous subarray and the indices of the first and last elements of this subarray. `max_sum` remains -1, as it is not modified within the loop.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0]:
            total_max_segment = segment
        
    #State: `arr` remains a list of integers where -10^9 <= arr[i] <= 10^9 for all 0 <= i < len(arr)`, `i` is `len(arr) - 1`, `max_segment` contains the maximum sum of a contiguous subarray and the index of the last element of this subarray, `new_segment` is either an empty list or a list containing the sum of the current contiguous subarray and the index of the last element of this subarray, `segments_variants` is a list of lists, each containing the sum of a contiguous subarray and the indices of the first and last elements of this subarray, and now includes an additional list with the elements of `max_segment` plus the index `len(arr) - 1`, `max_sum` remains -1, `total_max_segment` is updated to the segment in `segments_variants` with the maximum sum, or remains `[-1]` if all sums in `segments_variants` are less than or equal to -1.
    if (len(total_max_segment) == 1) :
        total_max_segment = [-1]
    #State: `arr` remains a list of integers where -10^9 <= arr[i] <= 10^9 for all 0 <= i < len(arr). `i` is `len(arr) - 1`. `max_segment` contains the maximum sum of a contiguous subarray and the index of the last element of this subarray. `new_segment` is either an empty list or a list containing the sum of the current contiguous subarray and the index of the last element of this subarray. `segments_variants` is a list of lists, each containing the sum of a contiguous subarray and the indices of the first and last elements of this subarray, and now includes an additional list with the elements of `max_segment` plus the index `len(arr) - 1`. `max_sum` remains -1. If `len(total_max_segment) == 1`, `total_max_segment` is now `[-1]`. Otherwise, `total_max_segment` remains the segment in `segments_variants` with the maximum sum, or `[-1]` if all sums in `segments_variants` are less than or equal to -1.
    return total_max_segment
    #The program returns `total_max_segment`, which is either `[-1]` if all sums in `segments_variants` are less than or equal to -1, or the segment in `segments_variants` with the maximum sum, including the sum of the subarray and the indices of the first and last elements of this subarray.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and returns the segment with the maximum sum from all possible contiguous subarrays of `arr`. The returned segment includes the sum of the subarray and the indices of the first and last elements of this subarray. If all sums of the contiguous subarrays are less than or equal to -1, the function returns `[-1]`. The input list `arr` remains unchanged.

#State of the program right berfore the function call: number is an integer, and quantity is a non-negative integer.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` accepts two parameters, `number` and `quantity`, where `number` is an integer and `quantity` is a non-negative integer. It returns a list containing `quantity` elements, each of which is equal to `number`. The function does not modify the input parameters.

