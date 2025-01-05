#State of the program right berfore the function call: C1 and C2 are integers from 1 to 10 representing the numbers on your two cards, and C3 is an integer from 1 to 10 representing the number on your opponent's face card. The total of C1 and C2 must be less than or equal to 20.
def func():
    for line in stdin:
        c = [int(s) for s in line.split()]
        
        cards = [i for i in range(1, 11) if i not in c]
        
        c1c2 = c[0] + c[1]
        
        e = sum(int(i + c1c2 <= 20) for i in cards)
        
        print('YES' if e > 3 else 'NO')
        
    #State of the program after the  for loop has been executed: `C1` is an integer from 1 to 10, `C2` is an integer from 1 to 10, `C3` is an integer from 1 to 10; `c1c2` is the sum of `C1` and `C2` (ranging from 2 to 20); `cards` is a list of integers from 1 to 10 excluding `C1`, `C2`, and `C3`; `e` is the total count of elements in `cards` such that `i + c1c2 <= 20` for all iterations; the result is 'YES' if `e` > 3, otherwise 'NO'.
#Overall this is what the function does:The function processes input lines containing three integers representing two player cards (C1 and C2) and one opponent's face card (C3). It checks if the sum of C1 and C2 exceeds 20 and does not return any error message for that case. It then counts how many remaining cards (not including C1, C2, and C3) can be added to the sum of C1 and C2 without exceeding 20. If more than three such cards exist, it outputs "YES"; otherwise, it outputs "NO". The function does not return win/lose/draw messages based on comparisons with C3 as stated in the annotations.

