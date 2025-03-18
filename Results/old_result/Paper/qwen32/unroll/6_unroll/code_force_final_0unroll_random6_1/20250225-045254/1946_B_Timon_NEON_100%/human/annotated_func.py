#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder when 'number' is divided by 1000000007.
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
        
    #State: new_segment: [], max_segment: [max_sum_of_segment, end_index_of_segment], segments_variants: [[sum1, end_index1], [sum2, end_index2], ...], max_sum: -1
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0] and len(segment) != 1:
            total_max_segment = segment
        
    #State: new_segment is [], max_segment is [max_sum_of_segment, end_index_of_segment], segments_variants is [[sum1, end_index1], [sum2, end_index2], ..., [max_sum_of_segment, end_index_of_segment, len(arr) - 1], [len(arr) - 1]], max_sum is -1, total_max_segment is [max_sum_of_segment, end_index_of_segment]
    return total_max_segment
    #The program returns total_max_segment, which is [max_sum_of_segment, end_index_of_segment]
#Overall this is what the function does:The function `func_2` takes a list of integers as input and returns a list containing the maximum sum of a contiguous subarray and the end index of this subarray.

#State of the program right berfore the function call: number is a list of integers, and quantity is a non-negative integer.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function takes a list of integers called `number` and a non-negative integer called `quantity`. It returns a sublist of `number` containing the first `quantity` elements. If `quantity` is 0, it returns an empty list. If `quantity` is greater than the length of `number`, it returns the entire list `number`.

