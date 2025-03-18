#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder of the integer 'number' divided by 1000000007
#Overall this is what the function does:The function accepts an integer parameter `number` and returns the remainder when `number` is divided by 1000000007.

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
        
    #State: arr is a list of integers; new_segment is []; max_segment is [sum of all elements in arr, starting index of the first non-negative number or 0]; segments_variants is a list of candidate segments; max_sum is -1.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0] and len(segment) != 1:
            total_max_segment = segment
        
    #State: `arr` is a list of integers; `new_segment` is []; `max_segment` is [sum of all elements in arr, starting index of the first non-negative number or 0]; `segments_variants` is a list of candidate segments with an additional segment equal to `max_segment + [len(arr) - 1]` and an additional segment equal to `[len(arr) - 1]`; `max_sum` is -1; `total_max_segment` is `max_segment` if `max_segment` has more than one element.
    return total_max_segment
    #The program returns `max_segment` if `max_segment` has more than one element.
#Overall this is what the function does:The function takes a list of integers as input and returns a segment (a sublist) of the list that has the maximum sum. The segment is represented as a list containing the sum of the segment and the starting and ending indices of the segment in the original list. If all elements are negative, it returns a segment with a sum of -1 and the last index of the list.

#State of the program right berfore the function call: number is a list of integers, and quantity is a non-negative integer.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function takes a list of integers `number` and a non-negative integer `quantity`, and returns a sublist containing the first `quantity` elements of `number`. If `quantity` is 0, it returns an empty list. If `quantity` exceeds the length of `number`, it returns the entire list.

