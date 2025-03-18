#State of the program right berfore the function call: The function should be called within a loop that iterates t times, where t is a non-negative integer (1 ≤ t ≤ 1000). For each iteration, the function receives three digits a, b, and c as input, where each digit is an integer (0 ≤ a, b, c ≤ 9).
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
        
    #State: The loop will print 'STAIR', 'PEAK', or 'NONE' for each iteration based on the values of `a`, `b`, and `c` provided during that iteration. The variables `a`, `b`, and `c` will be updated with the new input values for each iteration, and `i` will increment from 0 to `n-1`. After the loop completes, the final value of `i` will be `n-1`.
#Overall this is what the function does:The function `func` reads an integer `n` from the user, which specifies the number of iterations. For each of the `n` iterations, it reads three integers `a`, `b`, and `c` (each between 0 and 9) from the user. Based on the values of `a`, `b`, and `c`, it prints 'STAIR' if `a < b < c`, 'PEAK' if `a < b` and `b > c`, and 'NONE' otherwise. After all iterations, the function completes without returning any value. The final state of the program is that `n` iterations have been processed, and the appropriate output has been printed for each set of input digits.

