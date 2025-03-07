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
        
    #State: `p1`, `p2`, and `p3` are integers provided by the user, where 0 ≤ `p1` ≤ `p2` ≤ `p3` ≤ 30, `t` is greater than or equal to the number of iterations the loop has executed, `_` is `t - 1`, and the sum of `p1`, `p2`, and `p3` is even. If `p3` is greater than or equal to `p1 + p2`, the program continues with the same values for `p1`, `p2`, and `p3`. If `p3` is less than `p1 + p2`, and if `p1 - x <= p2 - y` at any point during the loop, the loop breaks and `p1 - x + p3` is printed. Otherwise, the loop completes, and `p3` is printed. After all iterations, `x` is the number of times the loop has executed, and `y` is `p3 - x`.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, indicating the number of test cases. For each test case, it reads three integers `p1`, `p2`, and `p3` from the user, representing the scores of three players sorted in non-decreasing order (0 ≤ p1 ≤ p2 ≤ p3 ≤ 30). The function then checks if the sum of these scores is even. If the sum is odd, it prints `-1`. If the sum is even and `p3` is greater than or equal to `p1 + p2`, it prints `p1 + p2`. If the sum is even and `p3` is less than `p1 + p2`, it performs a loop to find values `x` and `y` such that `p1 - x <= p2 - y`. If such values are found, it prints `p1 - x + p3`; otherwise, it prints `p3`. After processing all test cases, the function completes, and no further state changes are made to the input variables.

