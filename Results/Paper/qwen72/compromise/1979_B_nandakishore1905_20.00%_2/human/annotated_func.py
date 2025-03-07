#State of the program right berfore the function call: x and y are distinct non-negative integers such that 0 <= x, y <= 10^9 and x ≠ y.
def func():
    for i in range(int(input())):
        n, m = map(int, input().split())
        
        k = abs(n - m)
        
        if k & k - 1 == 0:
            print(k)
        elif n == 0 and m % 2 != 0:
            print(1)
        elif n == 0 and m % 2 == 0:
            print(2)
        else:
            l = bin(k).replace('0b', '')
            p = len(l)
            q = 2 ** (p - 1)
            print(k - q)
        
    #State: The values of x and y remain unchanged as they are not affected by the loop. The loop processes inputs n and m for each iteration and prints a result based on the conditions specified, but does not modify x or y.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It processes a series of inputs provided by the user. For each input pair `(n, m)`, it calculates a value based on specific conditions and prints the result. The function does not modify any external variables `x` and `y` that might be present in the calling context. After the function concludes, the values of `x` and `y` remain unchanged, and the program has printed a series of results based on the input pairs.

