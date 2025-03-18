#State of the program right berfore the function call: ticket is a string of digits of length n (2 <= n <= 100), where each digit is between 0 and 9 inclusive.
def func_1(ticket):
    total_sum = sum(ticket)
    if (total_sum % 2 != 0) :
        return False
        #The program returns False because the condition to return a boolean value is met regardless of the value of 'total_sum', which is odd.
    #State of the program after the if block has been executed: *`ticket` is a string of digits of length n (2 <= n <= 100), where each digit is between 0 and 9 inclusive; `total_sum` is the sum of the digits in `ticket` which is a non-negative integer and `total_sum` is an even number.
    target_sum = total_sum // 2
    curr_sum = 0
    segments = 0
    for digit in ticket:
        curr_sum += digit
        
        if curr_sum == target_sum:
            segments += 1
            curr_sum = 0
        
    #State of the program after the  for loop has been executed: `ticket` is a string of digits of length n (2 <= n <= 100), `total_sum` is a non-negative even integer, `target_sum` is equal to `total_sum // 2`, `curr_sum` is the sum of the digits in `ticket` that were processed, and `segments` is the number of times `curr_sum` reached `target_sum` during the loop execution. If `curr_sum` reached `target_sum`, it was reset to 0 for each segment found.
    return segments >= 2
    #The program returns a boolean indicating whether the number of segments where 'curr_sum' reached 'target_sum' is greater than or equal to 2.
#Overall this is what the function does:The function accepts a string `ticket`, which contains digits whose sum is calculated. If the sum is odd, it returns False. If the sum is even, the function checks how many times the cumulative sum of digits reaches half of the total sum. It returns True if this occurs at least twice, otherwise, it returns False. The function assumes that the digits in `ticket` are processed as integers, so it will need a conversion from characters to integers for the sum to be accurate.

