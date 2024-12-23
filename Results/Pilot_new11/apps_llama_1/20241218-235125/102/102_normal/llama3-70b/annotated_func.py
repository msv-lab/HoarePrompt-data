#State of the program right berfore the function call: n, a, and b are integers such that 1 <= n <= 10,000,000, 1 <= a <= 10,000,000, and 1 <= b <= 10,000,000.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `a` is a non-zero input integer, `b` is an input integer. Either 'YES' has been printed along with the values of `x` and `y` such that `x * a + y * b == n`, or no 'YES' has been printed, indicating that no integers `x` and `y` satisfy the equation `x * a + y * b == n`.
    print('NO')
#Overall this is what the function does:The function determines whether a given integer `n` can be expressed as a linear combination of two other integers `a` and `b`, i.e., whether there exist integers `x` and `y` such that `n = x * a + y * b`. It accepts three integer inputs `n`, `a`, and `b` from the user, where `1 <= n <= 10,000,000`, `1 <= a <= 10,000,000`, and `1 <= b <= 10,000,000`. The function then checks all possible integer values of `x` and corresponding `y` to see if the equation `n = x * a + y * b` holds true. If such integers `x` and `y` are found, the function prints 'YES' along with the values of `x` and `y`. If no such integers are found after checking all possibilities, the function prints 'NO'. After execution, the program's state is either 'YES' printed with the appropriate `x` and `y` values or 'NO', indicating whether `n` can be expressed as a linear combination of `a` and `b`. The function does not explicitly handle edge cases like `a` or `b` being zero, but since the input constraints specify both `a` and `b` as greater than or equal to 1, these cases are implicitly excluded. The actual return value of the function is implicitly `None` since it does not explicitly return any value, but its primary output is the print statements indicating whether `n` can be expressed as a linear combination of `a` and `b`.

