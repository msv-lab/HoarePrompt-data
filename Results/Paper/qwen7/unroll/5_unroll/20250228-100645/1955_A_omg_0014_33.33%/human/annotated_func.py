#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4, n is an input integer, for each iteration i in the range of n, a, b, c are integers read from input, d is set to c / 2, if a * b is less than a * d, then a * b is printed, otherwise, a * d is rounded and printed.
#Overall this is what the function does:The function processes multiple test cases, each containing three integers \( n \), \( a \), and \( b \). For each test case, it calculates either \( a \times b \) or \( a \times \frac{c}{2} \) (where \( c \) is another integer read from input), and prints the result. The function does not return any value but prints the calculated values for each test case.

