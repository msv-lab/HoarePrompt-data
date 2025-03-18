#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, X is an integer such that 2 <= X <= 10^18.
def func():
    for i in range(int(input())):
        x = int(input())
        
        max = 100000000
        
        min = -100000000
        
        ans = []
        
        t = 0
        
        while x != 1:
            if x % 2 == 0:
                ans.append(max)
                max -= 1
                x = x // 2
            else:
                ans.append(min)
                min += 1
                x -= 1
            t += 1
        
        ans.reverse()
        
        print(t)
        
        print(*ans)
        
    #State: For each test case, the number of iterations `t` required to reduce `X` to 1, followed by the list of `max` and `min` values in reversed order based on the parity of `X` in each iteration.
#Overall this is what the function does:The function processes a number of test cases, each consisting of an integer `X`. For each test case, it calculates the number of iterations required to reduce `X` to 1 by repeatedly dividing it by 2 if even or subtracting 1 if odd, and generates a sequence of values based on the operations performed. It outputs the number of iterations and the sequence for each test case.

