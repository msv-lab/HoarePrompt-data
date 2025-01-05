#State of the program right berfore the function call: C1, C2, and C3 are integers between 1 and 10 inclusive, representing the numbers on your two cards and your opponent's front card respectively.
def func():
    for line in stdin:
        c = [int(s) for s in line.split()]
        
        cards = [i for i in range(1, 11) if i not in c]
        
        c1c2 = c[0] + c[1]
        
        e = sum(int(i + c1c2 <= 20) for i in cards)
        
        print('YES' if e > 3 else 'NO')
        
    #State of the program after the  for loop has been executed: `C1` is between 1 and 10, `C2` is between 1 and 10; `c1c2` is between 2 and 20; `cards` is a list of integers from 1 to 10 excluding `C1` and `C2`; `e` is the total count of integers in `cards` for which `i + c1c2 <= 20`. The output will be 'YES' if `e` is greater than 3 for at least one iteration, otherwise 'NO'.
#Overall this is what the function does:The function reads multiple lines of input where each line contains three integers representing card values. It calculates the sum of the first two integers (C1 and C2), then counts how many integers from the range 1 to 10, excluding C1 and C2, can be added to this sum without exceeding 20. If at least one line results in more than 3 valid integers, it prints 'YES'; otherwise, it prints 'NO'. The function does not accept parameters directly, and the values for C1, C2, and the third card (C3) are taken from the input.

