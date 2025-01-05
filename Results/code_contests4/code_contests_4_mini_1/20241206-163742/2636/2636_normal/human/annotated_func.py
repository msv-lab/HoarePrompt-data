#State of the program right berfore the function call: C1, C2, and C3 are integers representing the numbers on the cards, where 1 <= C1, C2 <= 10 and 1 <= C3 <= 10. The total of C1 and C2 must be less than or equal to 20 for the game to be valid.
def func():
    for line in stdin:
        c = [int(s) for s in line.split()]
        
        cards = [i for i in range(1, 11) if i not in c]
        
        c1c2 = c[0] + c[1]
        
        e = sum(int(i + c1c2 <= 20) for i in cards)
        
        print('YES' if e > 3 else 'NO')
        
    #State of the program after the  for loop has been executed: `C1` is between 1 and 10, `C2` is between 1 and 10, `C3` is between 1 and 10; `c1c2` is the sum of `C1` and `C2`; `e` is the count of integers in the range 1 to 10 that, when added to `c1c2`, do not exceed 20; output is 'YES' if `e` > 3, otherwise 'NO'.
#Overall this is what the function does:The function processes input lines representing three integers (C1, C2, and C3), with C1 and C2 being between 1 and 10, and C3 also being between 1 and 10. It checks if the sum of C1 and C2 is less than or equal to 20. For each line of input, it calculates how many integers from 1 to 10 can be added to the sum of C1 and C2 without exceeding 20. If more than 3 such integers exist, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any values but directly prints the result based on the calculations.

