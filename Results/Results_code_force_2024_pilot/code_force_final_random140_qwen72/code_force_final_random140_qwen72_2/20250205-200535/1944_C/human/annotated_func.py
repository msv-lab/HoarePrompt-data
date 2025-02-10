#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 2 · 10^4, representing the number of test cases. Each test case consists of an integer n where 1 ≤ n ≤ 2 · 10^5, and a list of n integers a_1, a_2, ..., a_n where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        counter = {}
        
        for i in arr:
            counter[i] = counter.get(i, 0) + 1
        
        ans = 0
        
        once = False
        
        for i in range(n):
            if counter.get(i, 0) == 0:
                ans = i
                break
            elif counter.get(i, 0) == 1 and not once:
                once = True
                ans = i + 1
            elif counter.get(i, 0) == 1:
                ans = i
                break
        
        print(ans)
        
    #State: After all iterations, `t` is 0, `n` is the last input integer, `arr` is the last list of integers from the input, `counter` contains the count of each element in the last `arr`, `ans` is the smallest index `i` such that `counter.get(i, 0) == 0` or the smallest index `i` such that `counter.get(i, 0) == 1` and `once` was initially False. If no such index exists, `ans` remains 0 and `once` remains False.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n` followed by a list of `n` integers. It then determines and prints the smallest index `i` such that the count of `i` in the list is zero, or the smallest index `i` such that the count of `i` is one and it is the first occurrence of such an index. If no such index exists, it prints 0. After processing all test cases, the function completes, and the state of the program reflects the final values of the last test case processed.

