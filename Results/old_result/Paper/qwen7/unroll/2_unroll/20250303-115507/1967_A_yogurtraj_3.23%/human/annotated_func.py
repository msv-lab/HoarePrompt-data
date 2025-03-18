#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n and k are integers such that 1 ≤ n ≤ 2 \cdot 10^5 and 0 ≤ k ≤ 10^{12}. The list a contains n integers a_i such that 1 ≤ a_i ≤ 10^{12}, representing the number of cards of each type initially.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 100. For each test case, after the loop executes all the iterations, r is an integer representing the final value, rem is an integer representing the remaining value of k after the loop, y is an integer representing the count of additional elements considered in the last iteration, and the result is printed as ((r - 1) * n + 1) + rem + y.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads the number of cards of each type (`n`), a total value adjustment (`k`), and a list of card values (`a`). It then sorts the card values and iteratively adjusts the highest card value based on the available adjustments (`k`). After processing, it calculates and prints a result based on the final adjusted card value, any remaining adjustments, and the count of additional elements considered.

