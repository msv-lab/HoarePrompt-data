#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 1 ≤ n ≤ 5000, and s is a string of length n consisting of the characters '+' and '-'.
def func():
    for i in range(int(input())):
        s = int(input())
        
        e = input()
        
        P = 0
        
        M = 0
        
        for q in e:
            if q == '+':
                P += 1
            else:
                M += 1
        
        print(P - M)
        
    #State: The loop has executed `t` times, with `P` and `M` reflecting the counts of '+' and '-' characters from the last iteration, respectively.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n` and a string `s` of length `n` containing only '+' and '-' characters. For each test case, it calculates the difference between the number of '+' characters and the number of '-' characters in the string `s` and prints this difference.

