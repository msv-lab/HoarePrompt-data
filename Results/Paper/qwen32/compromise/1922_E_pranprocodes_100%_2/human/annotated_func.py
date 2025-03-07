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
        
    #State: 
#Overall this is what the function does:The function processes `t` test cases, each with an integer `X` (where 2 <= X <= 10^18). For each test case, it performs a series of operations to reduce `X` to 1, appending either a decreasing maximum value or an increasing minimum value to a list based on whether `X` is even or odd, respectively. It then prints the number of operations performed and the list of appended values in reverse order.

