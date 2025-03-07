#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n and k are integers where 1 ≤ n ≤ 2 · 10^5 and 0 ≤ k ≤ 10^12, representing the number of distinct types of cards and the number of coins available to buy new cards, respectively. a is a list of n integers where 1 ≤ a_i ≤ 10^12, representing the initial number of cards of each type. The sum of n over all test cases does not exceed 5 · 10^5.
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
        
    #State: After the loop executes all iterations, `i` is `n-2`, `n` is the number of distinct types of cards as given in the input, `k` is 0 (indicating all possible operations have been performed), `r` is the final value of the card count after distributing the coins, `rem` is the remainder of the last division operation when distributing the remaining coins, and `y` is the number of card types that did not receive any additional cards due to the distribution limit. The list `a` remains sorted and represents the final number of cards of each type after the loop has completed its execution.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by the number of card types (`n`), the number of coins available (`k`), and a list of the initial number of cards of each type (`a`). For each test case, it calculates and prints the maximum number of cards that can be achieved by distributing the available coins among the card types. The function modifies the input list `a` by sorting it but does not alter the original values. After processing all test cases, the function terminates without returning any value.

