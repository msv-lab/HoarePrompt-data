#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder when the integer 'number' is divided by 1000000007.
#Overall this is what the function does:The function `func_1` accepts an integer `number` and returns the remainder when `number` is divided by 1000000007. The function does not modify the input `number` and the final state of the program is that the returned value is the remainder of `number` modulo 1000000007.

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
        
    #State: `arr` is a list of integers where -10^9 <= arr[i] <= 10^9 for all 0 <= i < len(arr). `i` is len(arr) - 1. `max_segment` is the segment with the highest sum encountered during the loop, and it contains the sum of the segment and the starting index of the segment. `new_segment` is either an empty list or the segment that is currently being built, containing the sum of the segment and the starting index of the segment. `segments_variants` is a list of segments that were considered as potential max segments but were discarded because a higher sum segment was found. `max_sum` remains -1.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0] and len(segment) != 1:
            total_max_segment = segment
        
    #State: `arr` is a list of integers where -10^9 <= arr[i] <= 10^9 for all 0 <= i < len(arr)`, `i` is `len(arr) - 1`, `max_segment` is the segment with the highest sum encountered during the loop, `new_segment` is either an empty list or the segment that is currently being built, `segments_variants` is a list of segments that were considered as potential max segments but were discarded because a higher sum segment was found, and it must contain at least one element. `max_sum` remains -1, `total_max_segment` is the segment with the highest sum from `segments_variants` that has more than one element, or remains [-1] if no such segment exists.
    return total_max_segment
    #The program returns the segment with the highest sum from `segments_variants` that has more than one element, or [-1] if no such segment exists.
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and returns a list representing the segment of `arr` with the highest sum. This segment is identified from a list of potential segments (`segments_variants`) that are built during the function's execution. The returned list contains the sum of the segment and the start and end indices of the segment in `arr`. If no valid segment (with more than one element) is found, the function returns `[-1]`.

#State of the program right berfore the function call: number is an integer, and quantity is a non-negative integer.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` accepts two parameters: `number`, which is an integer, and `quantity`, which is a non-negative integer. It initializes a variable `answer` to 0. After the function concludes, `answer` remains 0, and the function returns `None`. The function does not modify the input parameters `number` and `quantity`.

