#State of the program right berfore the function call: The function is intended to be called multiple times with different sets of three digits a, b, and c, where each digit is an integer in the range 0 to 9, inclusive. The number of test cases, t, is a positive integer such that 1 <= t <= 1000.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b and b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The loop will execute `n` times, and for each iteration, it will read three integers `a`, `b`, and `c` from the input. Depending on the values of `a`, `b`, and `c`, it will print 'STAIR' if `a < b < c`, 'PEAK' if `a < b` and `b > c`, and 'NONE' otherwise. The values of `a`, `b`, and `c` will be updated with each iteration, but the value of `n` will remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, which represents the number of test cases. For each of the `n` test cases, it reads three integers `a`, `b`, and `c` from the input. Depending on the values of `a`, `b`, and `c`, the function prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b` and `b > c`, and 'NONE' otherwise. The function does not return any value and does not modify any external state. After the function concludes, `n` test cases have been processed, and the corresponding output has been printed for each case.

