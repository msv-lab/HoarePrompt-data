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
            print((r - 1) * n + 1 + k % n)
        else:
            print((r - 1) * n + 1 + rem + y)
        
    #State: Output State: r is the maximum value in the sorted list a after adjustments based on the value of k, rem is the remainder of k divided by the number of increments needed, y is the number of elements adjusted, and the final printed value is calculated using these variables.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n and k, and a list of n integers a. It sorts the list a and then iterates through it to adjust the maximum value in the list based on the value of k. Depending on the conditions met during iteration, it calculates and prints a final value derived from the adjusted maximum value, the remainder of k, and the count of adjusted elements.

