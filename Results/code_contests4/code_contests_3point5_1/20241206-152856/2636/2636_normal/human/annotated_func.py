#State of the program right berfore the function call: C1, C2, and C3 are integers representing the numbers on the cards, where 1 <= C1, C2, C3 <= 10.**
def func():
    for line in stdin:
        c = [int(s) for s in line.split()]
        
        cards = [i for i in range(1, 11) if i not in c]
        
        c1c2 = c[0] + c[1]
        
        e = sum(int(i + c1c2 <= 20) for i in cards)
        
        print('YES' if e > 3 else 'NO')
        
    #State of the program after the  for loop has been executed: C1, C2, and C3 are integers representing the numbers on the cards, all variables `c`, `cards`, `c1c2`, and `e` have values based on the input and loop calculations. The loop will print 'YES' if the count `e` of numbers in `cards` that when added to `c1c2` are less than or equal to 20 is greater than 3, otherwise it will print 'NO'.
#Overall this is what the function does:The function `func` reads input from stdin, processes the input to determine if certain conditions are met, and prints 'YES' if the count of numbers that can be added to C1 + C2 without exceeding 20 is greater than 3, otherwise it prints 'NO'. The function does not explicitly accept any parameters. However, it operates on the integers C1, C2, and C3, where 1 <= C1, C2, C3 <= 10.

