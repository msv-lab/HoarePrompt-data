#State of the program right berfore the function call: The function `func` is expected to take three integers p_1, p_2, and p_3 as input, where 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30, representing the scores of three players in a series of chess games. The function should be called within a loop that processes multiple test cases, where the number of test cases t is an integer such that 1 ≤ t ≤ 500.
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
        
    #State: The loop will have processed all `t` test cases, and for each test case, it will have printed either `-1`, `p1 + p2`, or a value calculated based on the conditions inside the loop. The values of `p1`, `p2`, and `p3` will be updated for each iteration based on the input provided, but these variables will not retain any specific value after the loop completes. The variable `t` will be unchanged.
#Overall this is what the function does:The function `func` processes a series of test cases, each containing three integers `p1`, `p2`, and `p3` representing the scores of three players in a series of chess games. The function reads the number of test cases `t` and then, for each test case, reads the scores `p1`, `p2`, and `p3`. It prints a result for each test case based on the following conditions: If the sum of the scores is odd, it prints `-1`. If the highest score `p3` is greater than or equal to the sum of the other two scores, it prints `p1 + p2`. Otherwise, it calculates and prints a value that satisfies certain conditions within a loop. After processing all test cases, the function does not return any value, and the variables `p1`, `p2`, and `p3` are not retained. The variable `t` remains unchanged.

