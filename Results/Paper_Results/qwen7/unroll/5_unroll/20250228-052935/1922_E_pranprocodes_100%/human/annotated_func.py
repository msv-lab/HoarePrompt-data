#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, X is an integer such that 2 ≤ X ≤ 10^{18}.
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
        
    #State: Output State: t is the number of steps required to reduce x to 1 by either dividing by 2 when x is even or decrementing by 1 when x is odd. ans is a list containing integers that represent the maximum value (starting from 100000000) decremented by 1 for each even step and the minimum value (starting from -100000000) incremented by 1 for each odd step, with the list reversed at the end.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it takes an integer \(x\) and determines the number of steps required to reduce \(x\) to 1 by either halving \(x\) when it is even or decrementing \(x\) by 1 when it is odd. It also generates a list of integers representing the maximum value (starting from 100000000) for each even step and the minimum value (starting from -100000000) for each odd step, with the list reversed at the end. The function outputs the number of steps and the generated list for each test case.

