#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, p_1, p_2, and p_3 are integers satisfying 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
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
        
    #State: Output State: The output state will consist of a series of integers printed based on the conditions within the loop. For each iteration, if the sum of `p1`, `p2`, and `p3` is odd, `-1` will be printed. If `p3` is greater than or equal to the sum of `p1` and `p2`, then `p1 + p2` will be printed. Otherwise, a value calculated from `p1`, `p2`, and `p3` will be printed through a specific algorithm involving a while loop.
#Overall this is what the function does:The function processes up to 500 test cases, each consisting of three integers \( p_1 \), \( p_2 \), and \( p_3 \) where \( 0 \leq p_1 \leq p_2 \leq p_3 \leq 30 \). For each test case, it checks if the sum of \( p_1 \), \( p_2 \), and \( p_3 \) is even. If the sum is odd, it prints \(-1\). If the sum is even, it calculates and prints one of the following values: \( p_1 + p_2 \), \( p_1 - x + p_3 \), or \( p_3 \), where \( x \) and \( y \) are determined by a specific algorithm involving a while loop. After processing all test cases, the function ends with no return value.

