#State of the program right berfore the function call: ticket is a string of digits with length n (2 <= n <= 100), where each digit is an integer between 0 and 9.
def func_1(ticket):
    total_sum = sum(ticket)
    if (total_sum % 2 != 0) :
        return False
        #The program returns False since the current value of total_sum is odd.
    #State of the program after the if block has been executed: *`ticket` is a string of digits with length n (2 <= n <= 100), each digit is an integer between 0 and 9; `total_sum` is the sum of the digits in `ticket`, and `total_sum` is an even number.
    target_sum = total_sum // 2
    curr_sum = 0
    segments = 0
    for digit in ticket:
        curr_sum += digit
        
        if curr_sum == target_sum:
            segments += 1
            curr_sum = 0
        
    #State of the program after the  for loop has been executed: `ticket` is a string of digits with length at least 2, `total_sum` is an even number, `target_sum` is equal to `total_sum // 2`, `curr_sum` is 0, `segments` is the number of segments in `ticket` such that the sum of digits in each segment equals `target_sum`.
    return segments >= 2
    #The program returns True if the number of segments in 'ticket' that have a sum of digits equal to 'target_sum' is greater than or equal to 2, indicating that there are at least 2 such segments.
#Overall this is what the function does:The function accepts a string `ticket` of digits, returns `False` if the total sum of digits is odd, and returns `True` if there are at least two segments where each segment's sum equals half of the total sum of the digits, or `False` otherwise.

