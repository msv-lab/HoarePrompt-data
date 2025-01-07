#State of the program right berfore the function call: a, b, and c are integers such that -10^9 ≤ a, b, c ≤ 10^9.
def func():
    a, b, c = map(int, input().split())
    if (c == 0) :
        if (a == b) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers updated to the values obtained from user input, where -10^9 ≤ `a`, `b`, `c` ≤ 10^9. If `a` is equal to `b`, then 'YES' is printed. Otherwise, since `a` is not equal to `b`, 'NO' is printed.
    else :
        if ((b - a) % c == 0 and (b - a) / c >= 0) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers within the range -10^9 ≤ `a`, `b`, `c` ≤ 10^9, and `c` is not equal to 0. If the difference (b - a) is divisible by c and (b - a) / c is greater than or equal to 0, then 'YES' has been printed. Otherwise, if (b - a) is not divisible by c or (b - a) / c is less than 0, 'NO' has been printed.
    #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers within the range -10^9 ≤ `a`, `b`, `c` ≤ 10^9. If `c` is equal to 0, then if `a` is equal to `b`, 'YES' is printed; otherwise, 'NO' is printed. If `c` is not equal to 0, then if (b - a) is divisible by `c` and (b - a) / `c` is greater than or equal to 0, 'YES' is printed; otherwise, 'NO' is printed.
#Overall this is what the function does:The function accepts three integers `a`, `b`, and `c` as input from the user. If `c` is 0, it checks if `a` is equal to `b` and prints 'YES' if they are equal, or 'NO' otherwise. If `c` is not 0, it checks if the difference `b - a` is divisible by `c` and whether the result of this division is non-negative; it prints 'YES' if both conditions are met, or 'NO' otherwise. The function does not return any value; it solely prints results based on these conditions.

