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
            low, high = min(p3 - p1, p3 - p2), max(p3 - p1, p3 - p2)
            cur = low
            while high >= cur:
                if p1 - cur <= p2 - (p3 - cur):
                    print(p1 - cur + p3)
                    break
                else:
                    cur += 1
            else:
                print(p3)
        
    #State: The loop will execute `t` times, and for each iteration, it will read three integers `p1`, `p2`, and `p3` from the input. The loop will print a value based on the conditions specified in the loop body. The values of `p1`, `p2`, and `p3` will be updated for each iteration, but the initial input values `p_1`, `p_2`, and `p_3` (which are not used inside the loop) will remain unchanged. After `t` iterations, the loop will terminate, and the program will end.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `p1`, `p2`, and `p3` representing the scores of three players in non-decreasing order. It then prints a value based on the following conditions: If the sum of the scores is odd, it prints -1. If the highest score `p3` is greater than or equal to the sum of the other two scores, it prints the sum of `p1` and `p2`. Otherwise, it calculates a value that balances the scores and prints it. After processing all `t` test cases, the function terminates.

