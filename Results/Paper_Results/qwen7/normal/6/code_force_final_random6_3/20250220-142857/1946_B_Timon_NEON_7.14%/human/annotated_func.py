#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder when the integer 'number' is divided by 1000000007
#Overall this is what the function does:The function accepts an integer and returns the remainder when this integer is divided by 1000000007.

#State of the program right berfore the function call: arr is a list of integers where -10^9 ≤ arr[i] ≤ 10^9 for all 0 ≤ i < len(arr).
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
        
    #State: Output State: `max_sum` remains -1, `new_segment` becomes either an empty list, [arr[3] + arr[5] + ... + arr[n-1], n-1], [arr[4] + arr[2] + arr[5] + ... + arr[n-1], 2], [arr[5] + ... + arr[n-1], 5], or [arr[4] + arr[2], 2], `max_segment` becomes either [2 + arr[1] + arr[3] + ... + arr[n-1], 0], [2 + arr[4] + arr[2] + arr[5] + ... + arr[n-1], 0], [1 + arr[1] + arr[5] + ... + arr[n-1], 0], [1 + arr[3] + arr[5] + ... + arr[n-1], 0], [1 + arr[4] + arr[5] + ... + arr[n-1], 0], [1 + arr[5] + ... + arr[n-1], 0], or [1 + arr[4], 0] or [1 + arr[3], 0], `segments_variants` becomes a list containing all possible valid segment variants found during the loop execution, `i` is n (where n is the length of `arr`), and `arr` remains a non-empty list.
    #
    #This output state describes the final conditions of the variables after the loop has completed all its iterations. The `max_segment` will hold the maximum sum of any subarray encountered during the loop, and `segments_variants` will contain all such subarrays that had the maximum sum. The `new_segment` and `max_sum` will reflect the last state of the algorithm as it processes the entire array `arr`.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0]:
            total_max_segment = segment
        
    #State: Output State: `total_max_segment` is the list with the maximum sum among all the segments found in `segments_variants`, and `segment` is the last element in `segments_variants`.
    #
    #Explanation: After all iterations of the loop have finished, `total_max_segment` will hold the segment with the highest sum from all the segments considered in `segments_variants`. The variable `segment` will be the last segment evaluated in the loop, which, in this case, would be the last element in the `segments_variants` list since the loop updates `total_max_segment` whenever it finds a segment with a higher sum. All other variables remain unchanged from their final states after the third iteration.
    if (len(total_max_segment) == 1) :
        total_max_segment = [-1]
    #State: `total_max_segment` is the list with the maximum sum among all the segments found in `segments_variants`, and `segment` is the last element in `segments_variants`. If `len(total_max_segment)` equals 1, then `total_max_segment` is [-1].
    return total_max_segment
    #The program returns the list `total_max_segment` which contains the segment with the maximum sum among all the segments found in `segments_variants`. If the length of `total_max_segment` is 1, it is set to [-1]
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and returns a list `total_max_segment` containing the segment with the maximum sum among all possible subarrays found in `arr`. If no valid segment is found, it returns `[-1]`.

#State of the program right berfore the function call: number is an integer representing the sum of the original array, and quantity is a non-negative integer representing the number of operations (k).
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function processes an integer `number` representing the sum of the original array and a non-negative integer `quantity` representing the number of operations (k). After processing, it sets the variable `answer` to 0 and does not return any specific value.

