#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder of the integer 'number' when divided by 1,000,000,007.
#Overall this is what the function does:The function `func_1` accepts an integer `number` and returns the remainder of `number` when divided by 1,000,000,007. The input `number` remains unchanged.

#State of the program right berfore the function call: arr is a list of integers where each element a_i satisfies -10^9 <= a_i <= 10^9.
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
        
    #State: `new_segment` is an empty list, `max_segment` is the segment with the maximum sum found during the iteration, `segments_variants` is a list of segments (each segment is a list containing the sum and the end index of the segment), and `max_sum` remains -1.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0]:
            total_max_segment = segment
        
    #State: Output State: `new_segment` is an empty list, `max_segment` is the segment with the maximum sum found during the iteration, `segments_variants` now includes an additional segment which is `max_segment` with the end index `len(arr) - 1` appended, `max_sum` remains -1, `total_max_segment` is the segment with the maximum sum found during the iteration.
    if (len(total_max_segment) == 1) :
        total_max_segment = [-1]
    #State: *`new_segment` is an empty list, `max_segment` is the segment with the maximum sum found during the iteration, `segments_variants` now includes an additional segment which is `max_segment` with the end index `len(arr) - 1` appended, `max_sum` remains -1, `total_max_segment` is the segment with the maximum sum found during the iteration. If the length of `total_max_segment` is 1, `total_max_segment` is `[-1]`.
    return total_max_segment
    #The program returns `total_max_segment`, which is the segment with the maximum sum found during the iteration. If the length of `total_max_segment` is 1, `total_max_segment` is `[-1]`.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and returns the segment with the maximum sum found during the iteration. The segment is represented as a list containing the sum of the segment and the start and end indices of the segment within `arr`. If no valid segment is found (i.e., the list is empty or all elements are negative), the function returns `[-1]`.

#State of the program right berfore the function call: number is an integer, and quantity is a non-negative integer.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` accepts two parameters, `number` and `quantity`, where `number` is an integer and `quantity` is a non-negative integer. It returns an integer value, `answer`, which is initialized to 0 and remains unchanged throughout the function. The function does not return a list as suggested in the comment.

