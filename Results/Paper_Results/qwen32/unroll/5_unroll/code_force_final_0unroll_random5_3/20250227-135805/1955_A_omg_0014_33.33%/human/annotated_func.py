#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10⁴. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: t is an integer such that 1 ≤ t ≤ 10⁴; n is the integer value provided by the user input; a, b, and c are the last set of integers read in the last iteration of the loop; the output consists of n lines, each being either a * b or round(a * d) based on the condition a * b < a * d.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c`. It then calculates and prints either `a * b` or `round(a * c / 2)` based on which value is smaller.

