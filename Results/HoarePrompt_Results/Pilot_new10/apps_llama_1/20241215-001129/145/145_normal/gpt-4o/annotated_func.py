#State of the program right berfore the function call: n is a non-negative integer greater than 1, and ticket is a string of n digits where each digit is a non-negative integer less than 10.
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
        
    #State of the program after the  for loop has been executed: `n` is the original non-negative integer greater than 1, `ticket` is the original string of `n` digits, `segment_length` is `n-1`, `target_sum` is the sum of the first `n-1` digits of `ticket`, `current_sum` is the sum of the last sequence of digits not equal to `target_sum` or 0 if the last sequence equals `target_sum`, `segment_count` is the number of sequences of digits that sum up to `target_sum`, and `i` is `n`.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function accepts a non-negative integer `n` greater than 1 and a string `ticket` of `n` digits, and returns 'YES' if the `ticket` string can be divided into two or more segments of the same sum, where the sum is equal to the sum of the first segment, and 'NO' otherwise, assuming the existence of a `segment_sum` function to calculate the sum of digits in a given range of the `ticket` string.

#State of the program right berfore the function call: start and end are non-negative integers such that 0 <= start <= end < len(ticket), where ticket is a string of digits
def segment_sum(start, end):
    return sum(int(ticket[i]) for i in range(start, end + 1))
    #The program returns the sum of the digits in the string 'ticket' from index 'start' to 'end' (inclusive), where 'start' and 'end' are non-negative integers and 0 <= start <= end < len(ticket)
#Overall this is what the function does:The function calculates the sum of digits in a string `ticket` from index `start` to `end` (inclusive), assuming `ticket` contains only digits and `start` and `end` are valid, non-negative indices where `start <= end < len(ticket)`, but does not handle cases of non-digit characters, out-of-bounds indices, or invalid input types for `start` and `end`.

