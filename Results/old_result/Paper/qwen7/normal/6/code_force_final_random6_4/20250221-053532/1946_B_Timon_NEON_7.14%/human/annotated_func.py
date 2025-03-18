#State of the program right berfore the function call: number is an integer.
def func_1(number):
    return number % 1000000007
    #The program returns the remainder when the integer 'number' is divided by 1000000007
#Overall this is what the function does:The function accepts an integer `number` and returns the remainder when `number` is divided by 1000000007.

#State of the program right berfore the function call: arr is a list of integers, where each element is within the range of -10^9 to 10^9, and the length of the list is denoted by len(arr).
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
        
    #State: Output State: `segments_variants` is a list of all valid segment variants found during the loop execution, where each variant is a list containing the sum of the segment and the end index of the segment. `new_segment` is an empty list because it gets reset whenever a new segment with a higher sum is found. `max_segment` contains the sum and the end index of the segment with the maximum sum found throughout the loop execution. `max_sum` remains -1 because the loop does not update it. The value of `i` will be equal to the length of `arr` after the loop completes.
    #
    #In simpler terms, `segments_variants` will contain all the segments (defined by their sum and end index) that were found during the loop, `new_segment` will be empty, `max_segment` will hold the segment with the highest sum, and `max_sum` will still be -1 since it's not updated in the provided code.
    segments_variants.append(max_segment + [len(arr) - 1])
    segments_variants.append(new_segment + [len(arr) - 1])
    total_max_segment = [-1]
    for segment in segments_variants:
        if total_max_segment[0] < segment[0]:
            total_max_segment = segment
        
    #State: Output State: `segments_variants` is an empty list, `segment` does not exist because there are no elements left in `segments_variants`, `new_segment` remains an empty list, `max_segment` remains unchanged as it holds the segment with the highest sum found so far during the loop's execution, `max_sum` remains -1 since it was not updated after the last iteration, and `total_max_segment` remains unchanged and still holds the segment with the highest sum found throughout the loop's iterations.
    #
    #In simpler terms, after all iterations of the loop have finished, `segments_variants` is empty because all its elements have been processed. The variables `segment`, `new_segment`, `max_segment`, `max_sum`, and `total_max_segment` retain their final states from the last iteration of the loop.
    if (len(total_max_segment) == 1) :
        total_max_segment = [-1]
    #State: `segments_variants` is an empty list, `segment` does not exist because there are no elements left in `segments_variants`, `new_segment` remains an empty list, `max_segment` remains unchanged as it holds the segment with the highest sum found so far during the loop's execution, `max_sum` remains -1 since it was not updated after the last iteration, and `total_max_segment` is now [-1].
    return total_max_segment
    #The program returns the list `[-1]` which is the value of `total_max_segment`
#Overall this is what the function does:The function `func_2` accepts a list of integers `arr` and processes it to find the segment with the highest sum. It iterates through the list, tracking segments and updating the maximum segment found so far. After processing all elements, it returns a list containing either the segment with the highest sum or `[-1]` if no valid segment is found.

#State of the program right berfore the function call: number is an integer, and quantity is a non-negative integer such that 0 <= quantity <= 2 * 10^5.
def func_3(number, quantity):
    answer = 0
#Overall this is what the function does:The function `func_3` accepts two parameters: `number`, an integer, and `quantity`, a non-negative integer within the range of 0 to 200,000. If `quantity` is within the valid range, it returns the `number` repeated `quantity` times. If `quantity` is outside this range, it returns an error message.

