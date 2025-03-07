#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, X is an integer such that 2 ≤ X ≤ 10^18.
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
        
    #State: Output State: `t` is the total number of iterations required to reduce `x` to 1, `x` is now 1, `max` is `-100000000 - t`, `min` is `100000000 + t`, `ans` is a list containing alternating values starting from `max` (`-100000000 - t`) and decreasing by 1 each time until `min` (`100000000 + t`), and `ans` has been reversed.
    #
    #This means that after all iterations of the loop have finished, the variable `t` will hold the total number of steps taken to reduce `x` to 1. The variable `x` will be 1 as it has reached the base case of the loop. The variable `max` will be `-100000000 - t` because it decreases by 1 for each even division operation, and `min` will be `100000000 + t` because it increases by 1 for each decrement operation when `x` is odd. The list `ans` will contain the sequence of values generated during the process, starting from `max` and ending at `min`, with each subsequent value being either one less or one more than the previous based on whether `x` was even or odd, respectively, and the list is reversed before printing.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes an integer `x` (2 ≤ x ≤ 10^18) and calculates the number of steps (`t`) required to reduce `x` to 1 by repeatedly dividing `x` by 2 when it is even or decrementing `x` by 1 when it is odd. It then generates a list `ans` containing alternating values starting from a high initial value and decreasing by 1 each time until a low value, reflecting the operations performed. Finally, it prints the total number of steps `t` and the list `ans` in reverse order.

