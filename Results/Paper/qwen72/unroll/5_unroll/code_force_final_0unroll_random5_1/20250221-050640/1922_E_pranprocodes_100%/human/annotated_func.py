#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and X is a list of integers where each element x satisfies 2 <= x <= 10^18.
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
        
    #State: t is an integer such that 1 <= t <= 1000, and X is a list of integers where each element x satisfies 2 <= x <= 10^18. The loop prints the number of iterations (t) it took to reduce each x to 1, followed by a list of integers (ans) that were appended during the iterations, in reverse order. The values of max and min are unchanged for each new x, but they are modified within each iteration of the loop for a given x.
#Overall this is what the function does:The function `func` does not accept any parameters directly but reads an integer `t` (1 <= t <= 1000) and a list of integers `X` (each element 2 <= x <= 10^18) from user input. For each integer `x` in `X`, it performs a series of operations to reduce `x` to 1, appending specific values to a list `ans` during the process. The values appended are `max` (starting from 100000000 and decrementing) when `x` is even, and `min` (starting from -100000000 and incrementing) when `x` is odd. After reducing `x` to 1, it prints the number of operations performed (`t`) and the list `ans` in reverse order. The function does not return any value.

