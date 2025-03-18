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
        
    #State: After the loop executes all iterations, `ii` is `t - 1`, `n` and `k` are the last input values for the respective test case, `a` is the last sorted list of integers from user input, `i` is `n - 1` if the loop completes without breaking, otherwise it is the index where the loop broke. `r` is the final value of `a[n - 1] + k // n` if `k` is not 0, or the last updated value of `a[i] + k // (i + 1)` if the loop breaks. `rem` is the remainder of the last division operation if the loop breaks, otherwise it remains 0. `y` is the number of elements left unprocessed after the loop breaks or completes, and `k` is 0 if the loop completes without breaking, otherwise it is the remaining value after all subtractions.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by the number of distinct card types (`n`), the number of coins available (`k`), and a list of initial card counts (`a`). For each test case, it calculates and prints the maximum number of cards that can be obtained by distributing the available coins among the card types. The function reads the number of test cases (`t`) and the inputs for each test case from standard input. After processing all test cases, the function has no return value, but it has printed the results for each test case to standard output.

