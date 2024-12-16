#State of the program right berfore the function call: ticket is a string consisting of $n$ digits where $2 \le n \le 100$ and each digit is an integer between 0 and 9 inclusive.
def func_1(ticket):
    total_sum = sum(ticket)
    if (total_sum % 2 != 0) :
        return False
        #The program returns False
    #State of the program after the if block has been executed: `ticket` is a string consisting of $n$ digits where $2 \le n \le 100$ and each digit is an integer between 0 and 9 inclusive; `total_sum` is the sum of the digits in `ticket`. The total sum of the digits in `ticket` is even
    target_sum = total_sum // 2
    curr_sum = 0
    segments = 0
    for digit in ticket:
        curr_sum += digit
        
        if curr_sum == target_sum:
            segments += 1
            curr_sum = 0
        
    #State of the program after the  for loop has been executed: `ticket` is a string consisting of \( n \) digits where \( 2 \le n \le 100 \), `total_sum` is the sum of the digits in `ticket` and is even, `target_sum` is `total_sum // 2`, `curr_sum` is 0, `segments` is the number of segments found such that the sum of digits in each segment equals `target_sum`.
    return segments >= 2
    #The program returns True if there are at least 2 segments in `ticket` where the sum of the digits in each segment equals `target_sum`, otherwise False
#Overall this is what the function does:The function `func_1` accepts a string `ticket` consisting of \( n \) digits where \( 2 \le n \le 100 \) and each digit is an integer between 0 and 9 inclusive. It calculates the total sum of the digits in `ticket` and checks if this sum is even. If the sum is not even, it returns `False`. Otherwise, it calculates half of the total sum (`target_sum`) and iterates through the digits in `ticket`, counting the number of segments where the sum of digits equals `target_sum`. If there are at least two such segments, it returns `True`; otherwise, it returns `False`.

