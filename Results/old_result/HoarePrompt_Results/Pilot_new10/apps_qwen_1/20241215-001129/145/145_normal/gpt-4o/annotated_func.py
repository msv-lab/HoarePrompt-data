#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, and ticket is a string consisting of n digits where each digit is an integer between 0 and 9 inclusive.
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
        
    #State of the program after the  for loop has been executed: ``current_sum` is 0, `i` is `n`, `n` is an integer such that \(2 \leq n \leq 100\), `ticket` is a string consisting of `n` digits where each digit is an integer between 0 and 9 inclusive, `target_sum` is the sum of the first `segment_length - 1` digits of `ticket` for the last valid segment, and `segment_count` is the count of valid segments if `current_sum` is 0 and `segment_count` is greater than 1, otherwise `current_sum` is the sum of all digits in `ticket`, `segment_count` is 0.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts two parameters: an integer `n` (such that \(2 \leq n \leq 100\)) and a string `ticket` consisting of `n` digits where each digit is an integer between 0 and 9 inclusive. It checks if the string `ticket` can be partitioned into segments where each segment has the same sum. If such a partition exists, the function returns 'YES'; otherwise, it returns 'NO'.

#State of the program right berfore the function call: ticket is a string consisting of n digits (where 2 ≤ n ≤ 100 and each digit is between '0' and '9'), start and end are non-negative integers such that 0 ≤ start ≤ end < len(ticket).
def segment_sum(start, end):
    return sum(int(ticket[i]) for i in range(start, end + 1))
    #The program returns the sum of the digits in the string 'ticket' from index 'start' to index 'end' inclusive
#Overall this is what the function does:The function `segment_sum` accepts two parameters, `start` and `end`, which are non-negative integers such that \(0 \leq \text{start} \leq \text{end} < \text{len(ticket)}\). It returns the sum of the digits in the string `ticket` from index `start` to index `end` inclusive. This includes handling the case where the indices are valid within the length of the string `ticket`.

