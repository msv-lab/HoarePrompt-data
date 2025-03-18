#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    n = int(input())
    t = 0
    for i in range(n):
        a, b = map(int, input().split())
        
        if a < b:
            print(a, b)
        elif a == b:
            print(a, b)
        else:
            print(b, a)
        
    #State: The final output state will be as follows: `t` remains 0, `n` remains an input integer which must be greater than 0, `i` is equal to `n-1`, and `a` and `b` are the last pair of integers inputted during the loop. Regardless of the values of `a` and `b`, they are printed in ascending order if `a` is less than `b`, or in their original order if `a` is greater than or equal to `b`.
#Overall this is what the function does:The function reads a series of integer pairs from the user, sorts each pair in ascending order (or leaves them unchanged if they are already in that order), and prints the sorted pairs. The function does not accept any parameters and does not return anything.

