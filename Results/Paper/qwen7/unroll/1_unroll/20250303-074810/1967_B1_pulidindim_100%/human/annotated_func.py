#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 \cdot 10^6, and the sum of n or m over all test cases does not exceed 2 \cdot 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = int(count - 1)
            g = int(n / count)
            if g < countmins:
                break
            g -= countmins
            ans += int(g / count) + 1
            count += 1
        
        print(int(ans))
        
    #State: Output State: t is an integer between 1 and 10^4 inclusive; for each i in the range(t), n and m are integers where n is between 1 and 10^4 inclusive and m is between 1 and 10^4 inclusive; ans is the final value calculated after executing the loop for the given n and m, which is an integer.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \( n \) and \( m \). For each test case, it calculates a value \( ans \) based on \( n \) and \( m \) using a specific algorithm involving a loop. The function outputs the calculated value \( ans \) for each test case. The function does not return any value but prints the result for each test case.

