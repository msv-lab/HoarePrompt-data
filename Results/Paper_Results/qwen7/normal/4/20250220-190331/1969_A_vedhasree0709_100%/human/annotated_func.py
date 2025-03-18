#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000; for each test case, n is an integer such that 2 ≤ n ≤ 50; p is a list of n integers where each p_i satisfies 1 ≤ p_i ≤ n, p_i ≠ i, and all p_i are distinct.
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
        
    #State: Output State: The loop will execute as many times as the number of test cases specified by the user. After all iterations, the variables `i`, `n`, `j`, `p`, and `q` will retain their final values from the last iteration of the loop. Specifically, `i` will be equal to `n`, `j` will be 1, `p` will be the last element of the list `l` (i.e., `l[n-1]`), and `q` will be the element at the index `p - 1` of list `l` (i.e., `l[l[n-1]-1]`). The program will print `2` during the first iteration that meets the condition `q == i + 1`, and it will print `3` for all other iterations, but since `j` is set to 1 after finding such a condition, no further iterations will occur.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `t`, an integer `n`, and a list `p` of `n` integers. For each test case, it checks if there exists an index `i` such that the element at index `p[i]` minus one equals `i + 1`. If such an index is found, it prints `2` and stops processing further test cases. If no such index is found after checking all elements, it prints `3`. The function does not return any value but outputs the result for each test case.

