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
        
    #State: `new_segment` is an empty list, `max_segment` is [sum of all non-negative numbers in `arr`, index of the last non-negative number in `arr`], `segments_variants` is a list of lists where each sublist contains the sum of a segment of non-negative numbers and the start and end indices of that segment, `max_sum` is -1.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0] and len(segment) != 1:
            total_max_segment = segment
        
    #State: Output State: `new_segment` is an empty list, `max_segment` is [sum of all non-negative numbers in `arr`, index of the last non-negative number in `arr`], `segments_variants` is a list of lists where each sublist contains the sum of a segment of non-negative numbers and the start and end indices of that segment, and the last sublist in `segments_variants` is `[sum of all non-negative numbers in `arr`, index of the last non-negative number in `arr`, len(arr) - 1, len(arr) - 1]`, `max_sum` is -1, `total_max_segment` is [sum of all non-negative numbers in `arr`, index of the last non-negative number in `arr`, len(arr) - 1, len(arr) - 1].
    return total_max_segment
    #The program returns a list `total_max_segment` which contains the sum of all non-negative numbers in `arr`, the index of the last non-negative number in `arr`, `len(arr) - 1`, and `len(arr) - 1`.
#Overall this is what the function does:The function `func_2` accepts a list `arr` of integers and processes it to find segments of consecutive non-negative numbers. It returns a list `total_max_segment` that contains the sum of the segment with the highest sum of non-negative numbers, the starting index of this segment, the ending index of this segment, and the last index of the input list `arr`. If no non-negative numbers are found, the function returns a list with the first element as -1 and the remaining elements as the last index of `arr`.

#State of the program right berfore the function call: number is an integer, and quantity is a non-negative integer.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` accepts two parameters, `number` and `quantity`, where `number` is an integer and `quantity` is a non-negative integer. It returns a list containing `quantity` elements, each of which is the value of `number`. The function does not modify the input parameters.

