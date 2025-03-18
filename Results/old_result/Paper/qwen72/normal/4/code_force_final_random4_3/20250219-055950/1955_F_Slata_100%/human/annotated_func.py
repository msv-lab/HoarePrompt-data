#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, p_i is a list of four integers where 0 <= p_i[j] <= 200 for j in [0, 1, 2, 3].
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: `i` is `int(input()) - 1`, `a`, `b`, `c`, and `d` are integers provided by the user, and `int(input())` must be greater than or equal to the number of iterations executed.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, representing the number of test cases. For each test case, it reads four integers `a`, `b`, `c`, and `d` from the user, each within the range 0 to 200. It then calculates and prints the sum of the integer divisions of `a`, `b`, `c`, and `d` by 2, plus 1 if exactly three out of `a`, `b`, and `c` are odd. The function does not return any value; it only prints the result for each test case. After the function concludes, the input variables `a`, `b`, `c`, and `d` are no longer relevant, and `t` is the number of test cases processed.

