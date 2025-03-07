#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n distinct integers where each p_i satisfies 1 <= p_i <= n, p_i != i for all i in [1, n].
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        i = 0
        
        j = 0
        
        while i <= n - 1:
            p = l[i]
            q = l[p - 1]
            if q == i + 1:
                print(2)
                j = 1
                break
            i += 1
        
        if j == 0:
            print(3)
        
    #State: - `t`: Remains the same as the initial input.
    #- `n`: Remains the same as the input for the last test case.
    #- `l`: Remains the same as the list input for the last test case.
    #- `i`: Will be `n` if the inner loop completes all iterations without breaking for the last test case.
    #- `j`: Will be `0` if the condition `q == i + 1` was never met during the last test case, otherwise `1`.
    #
    #### Natural Language Description:
    #After all the test cases have been processed, the number of test cases `t`, the size of the list `n`, and the list `l` itself will remain unchanged from their initial and most recent respective inputs. The variable `i` will be equal to `n` if the inner loop completed all iterations without breaking for the last test case. The variable `j` will be `0` if the condition `q == i + 1` was never met during the last test case, otherwise it will be `1`.
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `l` of `n` distinct integers. For each test case, it checks if there exists an integer `p` in the list such that the value at index `p-1` is equal to `i+1` where `i` is the current index. If such an integer is found, it outputs `2` for that test case; otherwise, it outputs `3`. The function does not modify the input values `t`, `n`, or `l` after processing each test case.

