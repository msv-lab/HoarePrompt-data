#State of the program right berfore the function call: The function takes no explicit arguments, but it uses values obtained from standard input, where n (1 ≤ n ≤ 10 000 000) is the amount of money, a (1 ≤ a ≤ 10 000 000) is the cost of one bottle of Ber-Cola, and b (1 ≤ b ≤ 10 000 000) is the cost of one Bars bar.
def func():
    n = int(input())
    a = int(input())
    b = int(input())
    for x in range(n // a + 1):
        y = (n - x * a) // b
        
        if x * a + y * b == n:
            print('YES')
            print(x, y)
            exit()
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 10,000,000, `a` is a non-zero integer, `b` is an integer. If a combination of `x` and `y` is found such that `x * a + y * b` equals `n`, then `x` and `y` are the values that satisfy this equation, 'YES' has been printed along with the values of `x` and `y`, and the program has terminated. Otherwise, `x` is `n // a`, and `y` is `(n - (n // a) * a) // b`, indicating that no solution was found.
    print('NO')
#Overall this is what the function does:The function reads the amount of money `n`, the cost of one Ber-Cola bottle `a`, and the cost of one Bars bar `b` from standard input, and attempts to find a combination of Ber-Cola bottles (`x`) and Bars bars (`y`) such that `x * a + y * b` equals `n`. If such a combination exists, it prints 'YES' along with the values of `x` and `y`. If no combination is found after checking all possibilities, it prints 'NO', indicating that it's not possible to spend exactly `n` amount of money on the given items.

