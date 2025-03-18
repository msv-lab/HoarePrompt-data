#State of the program right berfore the function call: ticket is a string of digits where each digit is between '0' and '9'.
def func_1(ticket):
    total_sum = sum(ticket)
    if (total_sum % 2 != 0) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: `ticket` is a string of digits where each digit is between '0' and '9', `total_sum` is the sum of the digits in `ticket`, and the sum of the digits in `ticket` is even
    target_sum = total_sum // 2
    curr_sum = 0
    segments = 0
    for digit in ticket:
        curr_sum += digit
        
        if curr_sum == target_sum:
            segments += 1
            curr_sum = 0
        
    #State of the program after the  for loop has been executed: `ticket` is a string of digits, `total_sum` is the sum of the digits in `ticket` and is even, `target_sum` is `total_sum // 2`, `curr_sum` is the sum of the remaining digits in `ticket` that do not contribute to a `target_sum`, `segments` is the number of segments in `ticket` that sum up to `target_sum`, and `digit` is the last digit in `ticket`.
    return segments >= 2
    #The program returns True if there are at least 2 segments in 'ticket' that sum up to 'target_sum' (which is half of the even 'total_sum' of the digits in 'ticket'), False otherwise
#Overall this is what the function does:The function accepts a string of digits, checks if the total sum of the digits is even, and if so, attempts to divide the string into segments summing up to half of the total sum, returning True if at least two such segments exist and False otherwise; if the total sum is odd, it immediately returns False, but it does not handle cases of non-string inputs or strings containing non-digit characters.

