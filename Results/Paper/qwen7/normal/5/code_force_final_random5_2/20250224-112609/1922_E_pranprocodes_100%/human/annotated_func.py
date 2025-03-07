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
        
    #State: Output State: The loop will continue to execute for as many times as specified by the input value of `i`. After all iterations, `i` will equal the total number of iterations, `x` will be 1, `max` will be `100000000 - t`, where `t` is the total number of iterations, `min` will be `-100000000 + t`, and `ans` will be a list containing integers starting from `max - t` and decrementing by 1 until `-100000000 + t`, with the list reversed. The variable `t` will hold the total number of iterations it took for `x` to become 1 across all iterations of the loop.
    #
    #In simpler terms, after the loop finishes executing all its iterations, `i` will be the total number of iterations, `x` will be 1 (since it eventually reaches 1), `max` will be adjusted based on the total number of iterations, `min` will also adjust accordingly, `ans` will contain a sequence of numbers starting from `max - t` down to `-100000000 + t`, and this list will be reversed, and `t` will store the cumulative number of steps taken for `x` to reach 1 across all inputs.
#Overall this is what the function does:The function processes multiple test cases, each involving an integer \( x \) (where \( 2 \leq x \leq 10^{18} \)). For each test case, it repeatedly divides \( x \) by 2 when \( x \) is even, or decrements \( x \) by 1 when \( x \) is odd, counting the number of steps required for \( x \) to reach 1. It then prints the total number of steps and a list of integers representing the values of a variable \( ans \) at each step, starting from a high value and decreasing by 1 for each step, with the list reversed. The function does not return any value but prints the results for each test case.

