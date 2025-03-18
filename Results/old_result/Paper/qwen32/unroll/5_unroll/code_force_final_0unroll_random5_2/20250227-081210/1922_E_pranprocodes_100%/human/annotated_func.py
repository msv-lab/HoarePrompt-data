#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, X is a long integer such that 2 ≤ X ≤ 10^{18}.
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
        
    #State: For each of the t test cases, the number of operations required to reduce x to 1, followed by the sequence of operations (either max or min values) in the order they were applied.
#Overall this is what the function does:The function processes a number of test cases, each consisting of a long integer `X`. For each test case, it calculates the number of operations required to reduce `X` to 1 using a specific set of rules, and outputs this count followed by the sequence of operations applied.

