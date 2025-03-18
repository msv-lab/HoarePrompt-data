#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, p_1, p_2, and p_3 are non-negative integers satisfying 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
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
        
    #State: Output State: The output state depends on the input values provided for each iteration of the loop. For each input triplet (p1, p2, p3), the program checks if their sum is even. If not, it prints -1 and continues to the next iteration. If the sum is even, it further checks if p3 is greater than or equal to p1 + p2. If true, it prints p1 + p2. Otherwise, it calculates two values, low and high, based on p3, p1, and p2, and uses a while loop to find a value cur such that p1 - cur <= p2 - (p3 - cur). It then prints p1 - cur + p3. If no such cur is found, it prints p3.
#Overall this is what the function does:The function processes multiple test cases, each defined by three non-negative integers \(p_1\), \(p_2\), and \(p_3\) where \(0 \leq p_1 \leq p_2 \leq p_3 \leq 30\). For each test case, it first checks if the sum of \(p_1\), \(p_2\), and \(p_3\) is even. If the sum is odd, it prints \(-1\) and moves to the next test case. If the sum is even, it further checks if \(p_3\) is greater than or equal to \(p_1 + p_2\). If true, it prints \(p_1 + p_2\). Otherwise, it finds a value \(cur\) such that \(p_1 - cur \leq p_2 - (p_3 - cur)\) and prints \(p_1 - cur + p_3\). If no such \(cur\) exists, it prints \(p_3\). The function outputs a series of numbers based on the conditions met by the input values for each test case.

