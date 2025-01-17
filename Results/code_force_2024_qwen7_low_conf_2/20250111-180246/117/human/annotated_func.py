#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10, and s is a string of length n consisting of characters 'W' and 'B', where 'W' denotes a white cell and 'B' denotes a black cell. It is guaranteed that at least one cell in the given strip is black.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = input()
        
        c = str(b[-1::-1])
        
        if c.count('B') > 1:
            print(a - c.index('B') - b.index('B'))
        else:
            print(a)
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 10^4\), `a` is an input integer, `b` is the final input provided by the user, `c` is the reversed string representation of the final `b`. If the count of 'B' in `c` is greater than 1, the value printed is `a - c.index('B') - b.index('B')`. Otherwise, no specific output is generated regarding the indices of 'B'.
#Overall this is what the function does:The function accepts an integer `t` such that \(1 \leq t \leq 10^4\). For each of these test cases, it reads an integer `n` and a string `s` of length `n` consisting of characters 'W' and 'B', ensuring at least one character in `s` is 'B'. The function then reverses the string `s` to form a new string `c`. It checks if the count of 'B' in `c` is greater than 1. If true, it prints the value `a - c.index('B') - b.index('B')`, where `a` is the initial integer read and `b` is the original string. If the count of 'B' in `c` is not greater than 1, no specific output is generated. The function does not return anything, but prints the result for each test case.

