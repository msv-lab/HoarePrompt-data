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
        
    #State: Output State: t is the number of steps required to reduce x to 1 by repeatedly dividing even numbers by 2 and subtracting 1 from odd numbers until x becomes 1. ans is a list containing integers where max starts at 100000000 and decreases by 1 for each even division, and min starts at -100000000 and increases by 1 for each subtraction until x becomes 1; the list is reversed before printing.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer `t` and an integer `X`. For each test case, it calculates the number of steps `t` required to reduce `X` to 1 by repeatedly dividing even numbers by 2 and subtracting 1 from odd numbers. Additionally, it generates a list `ans` where each element represents a value (initially set to either 100000000 or -100000000) that changes according to the operation performed during each step. Finally, it prints the number of steps `t` and the list `ans` in reverse order.

