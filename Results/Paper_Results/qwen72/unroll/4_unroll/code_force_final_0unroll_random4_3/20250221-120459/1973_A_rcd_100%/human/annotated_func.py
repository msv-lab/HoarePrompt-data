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
        
    #State: The loop will execute `t` times, and for each iteration, it will read three integers `p1`, `p2`, and `p3` from the input, and print a result based on the conditions provided in the loop body. The values of `p_1`, `p_2`, and `p_3` from the initial state will remain unchanged.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `p1`, `p2`, and `p3` from the input, representing the scores of three players sorted in non-decreasing order. It then prints a result based on the following conditions: if the sum of the scores is odd, it prints `-1`. If the highest score `p3` is greater than or equal to the sum of the other two scores `p1` and `p2`, it prints the sum of `p1` and `p2`. Otherwise, it adjusts the scores by decrementing `p3` and incrementing `p1` until a condition is met, and prints the adjusted sum of `p1` and `p3`. If the loop completes without meeting the condition, it prints `p3`. The function does not return any value, and the input variables `p1`, `p2`, and `p3` are not modified outside the loop.

