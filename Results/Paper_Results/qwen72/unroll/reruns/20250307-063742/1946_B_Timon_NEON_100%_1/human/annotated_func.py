#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder of the integer 'number' when divided by 1000000007.
#Overall this is what the function does:The function `func_1` accepts an integer `number` and returns the remainder of `number` when divided by 1000000007. The input integer `number` remains unchanged.

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
        
    #State: `new_segment` is an empty list, `max_segment` is [sum of all positive numbers in `arr`, index of the last positive number in `arr`], `segments_variants` is a list of lists, each containing the sum of a segment of positive numbers and the start and end indices of that segment, `max_sum` is -1.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0] and len(segment) != 1:
            total_max_segment = segment
        
    #State: `new_segment` is an empty list, `max_segment` is [sum of all positive numbers in `arr`, index of the last positive number in `arr`], `segments_variants` is a list of lists, each containing the sum of a segment of positive numbers and the start and end indices of that segment, with an additional list `[sum of all positive numbers in `arr`, index of the last positive number in `arr`, len(arr) - 1]` appended to it, and now an additional list `[len(arr) - 1]` is appended to `segments_variants`. `max_sum` is -1, `total_max_segment` is [sum of all positive numbers in `arr`, index of the last positive number in `arr`, len(arr) - 1].
    return total_max_segment
    #The program returns a list `total_max_segment` that contains the sum of all positive numbers in `arr`, the index of the last positive number in `arr`, and `len(arr) - 1`.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and returns a list `total_max_segment` that contains the sum of the maximum segment of non-negative numbers in `arr`, the starting index of this segment, and the ending index of this segment. If no non-negative numbers are present in `arr`, the function returns a list with a single element `-1`.

#State of the program right berfore the function call: number is an integer, and quantity is a non-negative integer.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` accepts two parameters, `number` and `quantity`. It returns an integer value of 0, regardless of the input parameters. The function does not modify the input parameters or return a list as suggested in the annotation.

