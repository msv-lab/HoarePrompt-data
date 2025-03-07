#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder when 'number' is divided by 1000000007
#Overall this is what the function does:The function accepts an integer `number` and returns the remainder when `number` is divided by 1000000007.

#State of the program right berfore the function call: arr is a list of integers where -10^9 ≤ arr[i] ≤ 10^9 for each element arr[i].
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
        
    #State: Output State: `segments_variants` is a list of all valid segments found during the execution of the loop, `new_segment` is an empty list, `max_segment` is the segment with the highest sum found throughout the entire iteration, and `max_sum` remains -1.
    #
    #Explanation: After the loop has executed all iterations, `segments_variants` will contain all the segments that were considered as potential candidates for the maximum sum segment. The `new_segment` will be an empty list because it gets reset whenever a new segment is finalized and added to `segments_variants`. `max_segment` will hold the segment with the highest sum encountered during the entire process. Since the loop does not modify `max_sum` unless a new maximum is found, and no new maximum was found in the given conditions, `max_sum` remains -1.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0] and len(segment) != 1:
            total_max_segment = segment
        
    #State: Output State: `segments_variants` contains all the segments generated during the iterations; `new_segment` remains an empty list; `max_segment` is the segment with the highest sum found throughout all iterations; `max_sum` remains -1 (indicating no valid segment was found that meets the criteria); `total_max_segment` is the segment with the highest sum among those that have more than one element.
    #
    #Explanation: After all iterations of the loop, `segments_variants` will include every segment variant generated during the process. The variable `new_segment` remains empty as it is only initialized and used within the loop but never assigned outside of it. `max_segment` will hold the segment with the highest sum encountered across all iterations. Since `max_sum` is initialized to -1 and only updated when a segment's sum exceeds the current `max_sum` and the segment has more than one element, `max_sum` will either remain -1 or be the sum of the `max_segment`. `total_max_segment` will be the segment with the highest sum among those that have more than one element, reflecting the best possible segment found according to the given condition.
    return total_max_segment
    #The program returns `total_max_segment`, which is the segment with the highest sum among those that have more than one element.
#Overall this is what the function does:The function accepts a list of integers `arr` and returns the subarray with the highest sum among those containing more than one element. It identifies all possible segments in the array, evaluates their sums, and selects the segment with the maximum sum that includes at least two elements. If no such segment exists, it returns a segment containing only the first element of the array.

#State of the program right berfore the function call: number is an integer, and quantity is a non-negative integer such that 0 <= quantity <= 2 * 10^5.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` accepts two parameters: `number`, an integer, and `quantity`, a non-negative integer within the range of 0 to 200,000. If `quantity` is within the valid range, it returns the value of `number`. Otherwise, it returns an error message indicating that the quantity is out of the allowed range.

