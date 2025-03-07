#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder of the integer 'number' when divided by 1000000007.
#Overall this is what the function does:The function `func_1` accepts an integer `number` and returns the remainder of `number` when divided by 1000000007. The input `number` remains unchanged.

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
        
    #State: `new_segment` is an empty list; `max_segment` is a list containing the sum of the maximum positive segment and the index of the last element in that segment; `segments_variants` is a list of lists, each containing the sum of a positive segment and the indices of the first and last elements in that segment; `max_sum` is -1.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0]:
            total_max_segment = segment
        
    #State: Output State: `new_segment` is an empty list; `max_segment` is a list containing the sum of the maximum positive segment and the index of the last element in that segment; `segments_variants` is a list of lists, each containing the sum of a positive segment and the indices of the first and last elements in that segment, with an additional list appended that contains the elements of `max_segment` plus the value `len(arr) - 1`, and another list appended that is `new_segment` plus the value `len(arr) - 1`; `max_sum` is -1; `total_max_segment` is the list with the highest sum from `segments_variants`.
    if (len(total_max_segment) == 1) :
        total_max_segment = [-1]
    #State: *`new_segment` is an empty list; `max_segment` is a list containing the sum of the maximum positive segment and the index of the last element in that segment; `segments_variants` is a list of lists, each containing the sum of a positive segment and the indices of the first and last elements in that segment, with an additional list appended that contains the elements of `max_segment` plus the value `len(arr) - 1`, and another list appended that is `new_segment` plus the value `len(arr) - 1`; `max_sum` is -1; if `len(total_max_segment) == 1`, then `total_max_segment` is `[-1]`. Otherwise, `total_max_segment` remains the list with the highest sum from `segments_variants`.
    return total_max_segment
    #The program returns `total_max_segment`, which is a list. If `total_max_segment` has only one element, it is `[-1]`. Otherwise, it is the list from `segments_variants` with the highest sum, including the sum of the positive segment, the indices of the first and last elements in that segment, and the additional value `len(arr) - 1`.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and returns a list `total_max_segment`. If `arr` does not contain any positive segment, `total_max_segment` is `[-1]`. Otherwise, `total_max_segment` contains the sum of the maximum positive segment found in `arr`, the index of the first element in that segment, the index of the last element in that segment, and the value `len(arr) - 1`.

#State of the program right berfore the function call: number is an integer, and quantity is a non-negative integer.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` accepts two parameters, `number` and `quantity`. It returns an integer value of `0`. The function does not modify the input parameters and does not return a list as suggested in the comment.

