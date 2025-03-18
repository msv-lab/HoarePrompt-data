#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 2 · 10^4, representing the number of test cases. Each test case consists of an integer n where 1 ≤ n ≤ 2 · 10^5, and a list of n integers a_1, a_2, ..., a_n where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cntl = [(0) for _ in range(n + 1)]
        
        for i in a:
            cntl[i] += 1
        
        if cntl[0] == 0:
            print(0)
        else:
            c = min(2, cntl[0])
            for j in range(1, n + 1):
                if cntl[j] < 2:
                    if cntl[j] == 0:
                        print(j)
                        break
                    else:
                        c -= 1
                        if not c:
                            print(j)
                            break
        
    #State: After the loop executes all iterations, `t` is an integer where 1 ≤ t ≤ 2 · 10^4, representing the number of test cases processed. For each test case, `n` is an input integer, and `a` is a list of integers input by the user. The variable `cntl` is a list of integers with length `n + 1`, where each element `cntl[i]` represents the number of times the integer `i` appears in the list `a`. If `cntl[0]` is 0, the loop prints 0 for that test case. Otherwise, the loop checks each integer from 1 to `n` inclusive. If any integer `j` in the range 1 to `n` has a count less than 2, and either its count is 0 or `c` (which is the minimum of 2 and `cntl[0]`) becomes 0, the loop breaks early and prints the value of `j`. If no such integer is found, the loop completes all iterations without printing anything. The loop iterates through all `t` test cases, and the final state of `t` is 0, indicating all test cases have been processed.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case involves an integer `n` and a list of `n` integers. The function counts the occurrences of each integer in the list. If the integer `0` does not appear in the list, the function prints `0`. Otherwise, it finds the smallest integer `j` (from 1 to `n`) that appears fewer than twice in the list and prints it. If no such integer exists, the function prints nothing. The function processes all test cases and does not return any values; it only prints results to the console.

