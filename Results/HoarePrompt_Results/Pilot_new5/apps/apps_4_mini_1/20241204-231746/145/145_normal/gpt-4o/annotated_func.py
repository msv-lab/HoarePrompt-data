#State of the program right berfore the function call: n is an integer between 2 and 100 (inclusive), and ticket is a string of n digits where each digit is a character representing an integer between '0' and '9'.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 100, `ticket` is a string of `n` digits, `segment_length` is between 1 and `n-1`, `target_sum` is equal to the sum of the first `segment_length` digits of `ticket`, `current_sum` is equal to the sum of all processed digits in `ticket`, `segment_count` is the number of segments found that match `target_sum`. After all iterations, `current_sum` is equal to 0 and `segment_count` is greater than 1 if the function returns 'YES', otherwise `current_sum` is not equal to 0 or `segment_count` is less than or equal to 1.
    return 'NO'
    #The program returns 'NO' because current_sum is not equal to 0 or segment_count is less than or equal to 1.
#Overall this is what the function does:The function accepts an integer `n` (between 2 and 100 inclusive) and a string `ticket` of `n` digits. It checks if it is possible to split the digits into multiple segments such that each segment has the same sum, returning 'YES' if such a split is possible and `segment_count` is greater than 1; otherwise, it returns 'NO'. If no valid splitting exists, it will also return 'NO' if either the total processed sum is not zero or if only one valid segment is found.

#State of the program right berfore the function call: ticket is a string of length n consisting of digits, where n is an integer such that 2 <= n <= 100. The individual digits, represented by a_i, are integers between 0 and 9.
def segment_sum(start, end):
    return sum(int(ticket[i]) for i in range(start, end + 1))
    #The program returns the sum of integers representing the digits of 'ticket' from index 'start' to 'end', where 'ticket' is a string of length n consisting of digits.
#Overall this is what the function does:The function accepts two integer parameters, `start` and `end`, and returns the sum of the integer values of the digits in the string `ticket` from index `start` to index `end`, inclusive. It assumes that both indices are valid and within the bounds of the string's length, which must be between 2 and 100. There are no checks for invalid index ranges, so if `start` is greater than `end` or if either index is out of bounds, the function may raise an IndexError.

