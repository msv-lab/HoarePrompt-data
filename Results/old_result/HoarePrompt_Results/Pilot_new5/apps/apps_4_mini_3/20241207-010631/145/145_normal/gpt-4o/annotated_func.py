#State of the program right berfore the function call: n is an integer representing the number of digits in the ticket where 2 <= n <= 100, and ticket is a string of n digits consisting of characters from '0' to '9'.
def func_1(n, ticket):
    for segment_length in range(1, n):
        target_sum = segment_sum(0, segment_length - 1)
        
        current_sum = 0
        
        segment_count = 0
        
        for i in range(n):
            current_sum += int(ticket[i])
            if current_sum == target_sum:
                current_sum = 0
                segment_count += 1
        
        if current_sum == 0 and segment_count > 1:
            return 'YES'
        
    #State of the program after the  for loop has been executed: `n` is between 2 and 100, `segment_length` is between 1 and n-1, `target_sum` is the result of `segment_sum(0, segment_length - 1)`, `current_sum` is 0, `segment_count` is the total number of segments formed with the sum equal to `target_sum`, and `i` is `n - 1`.
    return 'NO'
    #The program returns 'NO' regardless of the values of n, segment_length, target_sum, current_sum, segment_count, and i.
#Overall this is what the function does:The function accepts an integer `n` (where 2 <= n <= 100) and a string `ticket` consisting of n digits (characters from '0' to '9'). It attempts to partition the digits of `ticket` into segments such that each segment has the same sum equal to the sum of the first segment of a specified length. If it can form more than one such segment without any remaining digits, it returns 'YES'. If no valid segmentation is found after testing all possible segment lengths, it returns 'NO'.

#State of the program right berfore the function call: ticket is a string of n digits where n is an integer such that 2 <= n <= 100 and each digit a_i (0 <= a_i <= 9) represents a non-negative integer. start and end are non-negative integers such that 0 <= start <= end < n.
def segment_sum(start, end):
    return sum(int(ticket[i]) for i in range(start, end + 1))
    #The program returns the sum of the digits in the string 'ticket' from index 'start' to index 'end', inclusive.
#Overall this is what the function does:The function accepts a string `ticket` consisting of digits and two integers `start` and `end`. It returns the sum of the numeric values of the digits in `ticket` from index `start` to index `end`, inclusive. The function assumes that the indices are valid according to the constraints provided (0 <= start <= end < length of ticket). If the indices are invalid, the behavior of the function is not defined.

