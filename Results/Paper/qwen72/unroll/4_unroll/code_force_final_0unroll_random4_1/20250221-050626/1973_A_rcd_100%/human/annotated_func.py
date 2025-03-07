#State of the program right berfore the function call: The function should take three integers p_1, p_2, and p_3 as input, where 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30, and these integers represent the scores of three players after playing chess games. The function should also handle multiple test cases, where the number of test cases t is an integer such that 1 ≤ t ≤ 500.
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
        
    #State: The loop will execute t times, and for each iteration, it will take three integers p1, p2, and p3 as input. If the sum of p1, p2, and p3 is odd, it will print -1. If p3 is greater than or equal to the sum of p1 and p2, it will print the sum of p1 and p2. Otherwise, it will print the maximum possible score that can be achieved by adjusting the scores of the players, which is either p1 - x + p3 or p3, depending on the conditions inside the loop. The values of p1, p2, and p3 will be re-assigned in each iteration, and the loop will continue until all t iterations are completed.
#Overall this is what the function does:The function `func` accepts an integer `t` representing the number of test cases. For each test case, it takes three integers `p_1`, `p_2`, and `p_3` as input, representing the scores of three players. The function then processes these scores and prints a result for each test case. If the sum of the scores is odd, it prints -1. If `p_3` is greater than or equal to the sum of `p_1` and `p_2`, it prints the sum of `p_1` and `p_2`. Otherwise, it prints the maximum possible score that can be achieved by adjusting the scores of the players, which is either `p_1 - x + p_3` or `p_3`, depending on the conditions inside the loop. The function does not return any values; it only prints the results.

