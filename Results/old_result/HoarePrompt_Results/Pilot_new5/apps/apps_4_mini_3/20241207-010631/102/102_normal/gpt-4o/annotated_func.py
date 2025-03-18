#State of the program right berfore the function call: n, a, and b are integers such that 1 ≤ n, a, b ≤ 10,000,000.
def func_1():
    n = int(input())
    a = int(input())
    b = int(input())
    for x in range(n // a + 1):
        if (n - x * a) % b == 0:
            y = (n - x * a) // b
            print('YES')
            print(x, y)
            return
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `a` is an integer such that 1 ≤ `a` ≤ 10,000,000, `x` is at most `n // a`, and if the loop completes without finding a valid (x, y), then (n - x * a) % b is not equal to 0 for all x from 0 to n // a.
    print('NO')
#Overall this is what the function does:The function accepts three integers `n`, `a`, and `b`, and checks if it is possible to express `n` as a sum of multiples of `a` and `b`. If such a combination exists, it prints 'YES' followed by the respective counts of `a` and `b` (denoted as `x` and `y`). If no valid combination is found after checking all possibilities, it prints 'NO'. The function does not return any values.

