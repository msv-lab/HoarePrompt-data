#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 50, and the path is a string of length n consisting of characters '.', '@', or '*', where the first character is guaranteed to be '.'.
def func():
    a = int(input())
    s = 0
    for i in range(a):
        d = int(input())
        
        b = input()
        
        for j in range(len(b)):
            if b[j] == '@':
                s = s + 1
            elif b[j] == '*':
                if b[:]:
                    break
                elif b[j + 1] == '*':
                    break
        
        print(s)
        
        s = 0
        
    #State: After all the iterations, the loop will have processed `a` sets of inputs (pairs of `d` and `b`), and `s` will be reset to 0 after each iteration. The variable `i` will have reached the value `a` (the total number of iterations), and `j` will reflect the index at which the inner loop terminated in the last iteration.
    #
    #The variables `t`, `n`, `path`, and `a` remain unchanged throughout the loop.
    #
    #Output State:
#Overall this is what the function does:The function reads an integer `a` representing the number of test cases. For each test case, it reads another integer `d` and a string `b` of length `d`. It then counts and prints the number of '@' characters in the string `b`. After processing each test case, it resets the count and moves to the next test case.

