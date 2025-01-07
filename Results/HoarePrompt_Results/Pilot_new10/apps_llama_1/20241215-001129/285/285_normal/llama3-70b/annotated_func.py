#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    for a in range(n // 1234567 + 1):
        for b in range((n - a * 1234567) // 123456 + 1):
            c = (n - a * 1234567 - b * 123456) // 1234
            if a * 1234567 + b * 123456 + c * 1234 == n:
                print('YES')
                exit()
        
    #State of the program after the  for loop has been executed: `n` is the original input integer, `a` is `n // 1234567` if no solution is found and otherwise the value that satisfies the equation if a solution exists, `b` and `c` are determined based on the final or satisfying values of `a` and the equation `a * 1234567 + b * 123456 + c * 1234 == n` if a solution is found, or their last calculated values if no solution is found.
    print('NO')
#Overall this is what the function does:The function takes an integer input from the user, attempts to express it as a sum of multiples of 1234567, 123456, and 1234, and prints 'YES' if successful or 'NO' otherwise, without validating the input.

