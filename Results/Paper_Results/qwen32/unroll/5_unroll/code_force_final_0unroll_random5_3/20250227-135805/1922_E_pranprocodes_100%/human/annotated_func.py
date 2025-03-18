#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each of the t test cases, X is a positive integer such that 2 <= X <= 10^18.
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
        
    #State: For each of the t test cases, the output consists of two lines: the first line is the number of iterations it took to reduce x to 1, and the second line is the sequence of numbers appended to ans during the process. The initial value of t remains unchanged, and the value of x for each test case is not retained after processing.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `X` (2 <= X <= 10^18). For each test case, it calculates the number of iterations required to reduce `X` to 1 using a specific set of operations and generates a sequence of numbers corresponding to those operations. The function outputs the number of iterations and the sequence for each test case.

