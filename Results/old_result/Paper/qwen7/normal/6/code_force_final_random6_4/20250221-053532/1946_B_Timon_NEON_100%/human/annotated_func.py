#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder when the integer `number` is divided by 1000000007.
#Overall this is what the function does:The function accepts an integer `number` and returns the remainder when `number` is divided by 1000000007.

#State of the program right berfore the function call: arr is a list of integers, where each element is in the range [-10^9, 10^9].
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
        
    #State: Output State: `max_sum` remains -1, `arr` remains a list of integers, `new_segment` is either an empty list or a segment ending at the last index of `arr`, `max_segment` is a segment with its first element being the maximum sum of any subsegment in `arr` and its second element being the end index of that subsegment, `segments_variants` is a list containing all possible segments that could be `max_segment`, and `max_segment[0]` is the highest sum found among all subsegments of `arr`.
    #
    #In more detail:
    #- `max_sum` does not change because it was initialized to -1 and no operation modifies it.
    #- `arr` remains unchanged as the loop does not modify the original array.
    #- `new_segment` will be an empty list if no positive subsegment was found, or it will contain the last positive or zero-valued subsegment encountered.
    #- `max_segment` will hold the subsegment with the highest sum found during the iteration of the array.
    #- `segments_variants` will contain all subsegments that had the highest sum at some point during the iteration.
    #- `max_segment[0]` will be the maximum sum of any subsegment in `arr`.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0] and len(segment) != 1:
            total_max_segment = segment
        
    #State: After the loop executes all the iterations, `segments_variants` contains at least one segment, and `total_max_segment` is equal to the segment from `segments_variants` that has the highest first element (i.e., the maximum sum of any subsegment), provided that the segment has more than one element. If no such segment exists, `total_max_segment` remains [-1].
    return total_max_segment
    #The program returns a segment from `segments_variants` that has the highest first element, provided the segment has more than one element. If no such segment exists, it returns `[-1]`.
#Overall this is what the function does:The function accepts a list of integers `arr` and returns a segment from `segments_variants` that has the highest sum, provided the segment has more than one element. If no such segment exists, it returns `[-1]`. The function identifies all subsegments with non-negative sums and keeps track of the segment with the highest sum encountered. It then returns the segment with the highest sum from these candidates.

#State of the program right berfore the function call: number is an integer, and quantity is a non-negative integer such that 0 <= quantity <= 2 * 10^5.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` accepts two parameters: `number`, an integer, and `quantity`, a non-negative integer within the range 0 to 200,000. If `quantity` is non-negative, it returns a string consisting of `number` repeated `quantity` times. If `quantity` is negative, it returns an error message.

