#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and k are integers such that 1 ≤ n ≤ 2 \cdot 10^5 and 0 ≤ k ≤ 10^{12}. The list a contains n integers such that 1 ≤ a_i ≤ 10^{12}, representing the number of cards of type i initially.
def func():
    for ii in range(int(input())):
        n, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        r = a[0]
        
        rem = 0
        
        y = 0
        
        for i in range(0, n - 1):
            if (i + 1) * (a[i + 1] - a[i]) > k:
                r = a[i] + k // (i + 1)
                rem = k % (i + 1)
                y = n - 1 - i
                k = 0
                break
            else:
                k -= (i + 1) * (a[i + 1] - a[i])
                r = a[i + 1]
        
        if k != 0:
            r = a[n - 1] + k // n
            print((r - 1) * n + 1)
        else:
            print((r - 1) * n + 1 + rem + y)
        
    #State: The output state will be the result of the loop's final print statement for each test case. This result is calculated based on the sorted list `a`, the integer `k`, and the number of iterations through the loop. Specifically, it computes the maximum possible value that can be achieved by redistributing the cards according to the rules defined within the loop, and then prints `(r - 1) * n + 1 + rem + y` if `k` is not zero, or simply `(r - 1) * n + 1` otherwise.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n and k, and a list a of n integers. It sorts the list a and then redistributes the values according to specific rules to find the maximum possible value that can be achieved. For each test case, it calculates and prints the result based on the final value of r, the remaining value of k, and the number of additional iterations. If k is not zero, it includes the remainder and the additional iterations in the calculation.

