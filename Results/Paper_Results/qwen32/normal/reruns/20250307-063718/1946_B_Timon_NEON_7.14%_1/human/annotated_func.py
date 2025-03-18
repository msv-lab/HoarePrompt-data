#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder of 'number' divided by 1000000007
#Overall this is what the function does:The function accepts an integer `number` and returns the remainder when `number` is divided by 1000000007.

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
        
    #State: `arr` remains unchanged, `new_segment` is either an empty list or a list containing the last non-negative segment, `max_segment` holds the segment with the highest sum and its last index, `segments_variants` contains all segments evaluated as potential maximum segments, and `max_sum` remains -1.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0]:
            total_max_segment = segment
        
    #State: - After all iterations, `total_max_segment` will hold the segment with the highest sum from `segments_variants`.
    #   - All other variables (`arr`, `new_segment`, `max_segment`, `segments_variants`, `max_sum`) remain unchanged as per the problem statement.
    #
    #Therefore, the final output state is:
    #
    #Output State:
    if (len(total_max_segment) == 1) :
        total_max_segment = [-1]
    #State: After all iterations, `total_max_segment` will hold the segment with the highest sum from `segments_variants`. If the length of `total_max_segment` is 1, `total_max_segment` is set to `[-1]`. All other variables (`arr`, `new_segment`, `max_segment`, `segments_variants`, `max_sum`) remain unchanged as per the problem statement.
    return total_max_segment
    #The program returns `total_max_segment` which holds the segment with the highest sum from `segments_variants`. If the length of `total_max_segment` is 1, `total_max_segment` is set to `[-1]`.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and returns a segment (sublist) from `arr` with the highest sum. If no positive sum segment is found, it returns `[-1]`.

#State of the program right berfore the function call: number is a list of integers, and quantity is a non-negative integer.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function takes a list of integers and a non-negative integer as input. It returns a sublist containing the first `quantity` elements from the list. If `quantity` exceeds the length of the list, the entire list is returned.

