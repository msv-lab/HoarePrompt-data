#State of the program right berfore the function call: The function should take three integers p_1, p_2, and p_3 as input, where 0 <= p_1 <= p_2 <= p_3 <= 30, representing the scores of the three players after all the games. The function should also handle multiple test cases, where the number of test cases t is an integer such that 1 <= t <= 500.
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
        
    #State: The loop will have executed t times, and for each iteration, it will have processed the input scores p1, p2, and p3, printing the appropriate result based on the conditions specified in the loop. The values of p1, p2, and p3 will be updated with each iteration, but the initial values of p_1, p_2, and p_3 provided as input to the function will remain unchanged. The number of test cases t will also remain unchanged.
#Overall this is what the function does:The function `func` accepts an integer `t` (1 <= t <= 500) representing the number of test cases. For each test case, it reads three integers `p1`, `p2`, and `p3` (0 <= p1 <= p2 <= p3 <= 30) representing the scores of three players. The function then prints a result for each test case based on the following conditions: If the sum of the scores is odd, it prints -1. If the highest score `p3` is greater than or equal to the sum of the other two scores (`p1 + p2`), it prints the sum of the other two scores. Otherwise, it calculates and prints a value that represents a balanced score distribution. The function does not return any values; it only prints the results. The initial values of `p1`, `p2`, and `p3` provided for each test case remain unchanged, and the number of test cases `t` is also unchanged after the function concludes.

