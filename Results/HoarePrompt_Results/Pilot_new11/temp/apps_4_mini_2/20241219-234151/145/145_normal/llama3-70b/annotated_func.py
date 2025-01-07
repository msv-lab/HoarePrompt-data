#State of the program right berfore the function call: ticket is a string of digits with a length n, where 2 <= n <= 100 and each digit is between 0 and 9 inclusive.
def func_1(ticket):
    total_sum = sum(ticket)
    if (total_sum % 2 != 0) :
        return False
        #The program returns False because total_sum, which is the sum of the digits in 'ticket', is odd.
    #State of the program after the if block has been executed: *`ticket` is a string of digits with a length `n`, where `2 <= n <= 100`, and each digit is between `0` and `9`; `total_sum` is the sum of the digits in `ticket`, and `total_sum` is an even number.
    target_sum = total_sum // 2
    curr_sum = 0
    segments = 0
    for digit in ticket:
        curr_sum += digit
        
        if curr_sum == target_sum:
            segments += 1
            curr_sum = 0
        
    #State of the program after the  for loop has been executed: `ticket` is a string of digits with a length between 2 and 100, `total_sum` is the sum of the digits in `ticket` and is an even number, `target_sum` is equal to `total_sum // 2`, `curr_sum` is 0, and `segments` is the number of segments in `ticket` such that the sum of the digits within each segment equals `target_sum`.
    return segments >= 2
    #The program returns True if the number of segments in 'ticket' with a sum of digits equal to 'target_sum' is greater than or equal to 2; otherwise, it returns False.
#Overall this is what the function does:The function accepts a string `ticket` composed exclusively of digits with a length between 2 and 100. It calculates the sum of the digits in `ticket`. If this sum is odd, the function immediately returns False. If the sum is even, it checks for the existence of segments within the `ticket` string where the sum of the digits in each segment is equal to half of the total sum. The function counts how many such segments are formed, and it returns True if at least two segments are found; otherwise, it returns False. Notably, the function assumes that all characters in `ticket` are numerical digits and does not explicitly handle non-digit characters or empty strings, leading to assumptions about input validity.

