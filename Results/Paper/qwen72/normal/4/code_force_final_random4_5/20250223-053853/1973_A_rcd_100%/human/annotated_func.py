#State of the program right berfore the function call: The function should take three integers p_1, p_2, and p_3 as input, where 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30, representing the scores of the three players sorted in non-decreasing order.
def func():
    t = int(input())
    for _ in range(t):
        p1, p2, p3 = map(int, input().split())
        
        if (p1 + p2 + p3) % 2 != 0:
            print(-1)
            continue
        
        if p3 >= p1 + p2:
            print(p1 + p2)
        else:
            x = 0
            y = p3
            while y >= x:
                if p1 - x <= p2 - y:
                    print(p1 - x + p3)
                    break
                else:
                    x += 1
                    y -= 1
            else:
                print(p3)
        
    #State: The loop will execute `t` times, and for each iteration, it will read three integers `p1`, `p2`, and `p3` from the input. Depending on the values of `p1`, `p2`, and `p3`, it will print one of the following: -1 if the sum of the scores is odd, `p1 + p2` if `p3` is greater than or equal to the sum of `p1` and `p2`, or the result of a calculation involving `x` and `y` if neither of the above conditions are met. After all iterations, the values of `p1`, `p2`, and `p3` will be the last values read from the input, and `x` and `y` will be the last values calculated in the loop.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `p1`, `p2`, and `p3` from the input, representing the scores of three players sorted in non-decreasing order. The function then prints a result for each test case: -1 if the sum of the scores is odd, `p1 + p2` if `p3` is greater than or equal to the sum of `p1` and `p2`, or a calculated value based on the scores if neither of the above conditions are met. After processing all test cases, the function does not return any value, but the final state includes the last values of `p1`, `p2`, `p3`, `x`, and `y` used in the last iteration of the loop.

