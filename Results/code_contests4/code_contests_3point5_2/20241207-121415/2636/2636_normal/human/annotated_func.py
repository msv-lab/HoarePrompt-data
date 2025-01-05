#State of the program right berfore the function call: C1, C2, and C3 are integers representing the numbers on the cards, such that 1 <= C1, C2, C3 <= 10.**
def func():
    for line in stdin:
        c = [int(s) for s in line.split()]
        
        cards = [i for i in range(1, 11) if i not in c]
        
        c1c2 = c[0] + c[1]
        
        e = sum(int(i + c1c2 <= 20) for i in cards)
        
        print('YES' if e > 3 else 'NO')
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `c` is a list of integers, `cards` is a list of integers from 1 to 10 excluding elements in `c`, `c1c2` is the sum of the first two elements in list `c`, and the code prints 'YES' if `e` is greater than 3, otherwise it prints 'NO'
#Overall this is what the function does:The function `func` reads input from stdin, processes the input to determine if the sum of the first two elements in the input list `c` plus any card number from 1 to 10 (excluding elements in `c`) is less than or equal to 20. It then prints 'YES' if the count of valid cards `e` is greater than 3, otherwise it prints 'NO'. The function does not accept any parameters and does not have an explicit return value.

