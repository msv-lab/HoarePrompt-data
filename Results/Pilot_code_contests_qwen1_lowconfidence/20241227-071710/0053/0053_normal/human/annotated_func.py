#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000. For each test case, n and m are positive integers such that 1 ≤ n, m ≤ 1000, and the arrays a_1,...,a_n and b_1,...,b_m consist of positive integers such that 1 ≤ a_i, b_i ≤ 1000. Additionally, the sum of all n across all test cases and the sum of all m across all test cases do not exceed 1000 (∑_{i=1}^t n_i, ∑_{i=1}^t m_i ≤ 1000).
def func():
    input = lambda : stdin.readline().strip()
    for _ in range(int(input())):
        n, m = [int(i) for i in input().split()]
        
        lst1 = [int(i) for i in input().split()]
        
        lst2 = [int(i) for i in input().split()]
        
        nk = 0
        
        lst1 = set(lst1)
        
        lst2 = set(lst2)
        
        for i in lst1:
            if i in lst2:
                print('YES')
                print(1, i)
                nk = 1
                break
        
        if nk == 0:
            print('NO')
        
    #State of the program after the  for loop has been executed: `t` is a positive integer, `n` is the value of `n` for the last test case processed, `m` is the value of `m` for the last test case processed, `lst1` is a set of unique integers from the last list `a_1,...,a_n`, `lst2` is a set of unique integers from the last list `b_1,...,b_m`, `nk` is 0 or 1 depending on whether any element from `lst1` is found in `lst2`. If any element from `lst1` is found in `lst2`, the console displays 'YES' followed by '1' and the corresponding element. Otherwise, the console displays 'NO'.
#Overall this is what the function does:The function `func` accepts a parameter `t`, which represents the number of test cases, with \(1 \leq t \leq 1000\). For each test case, it accepts two positive integers `n` and `m`, and two lists of positive integers `a_1,...,a_n` and `b_1,...,b_m`, where \(1 \leq n, m \leq 1000\) and \(1 \leq a_i, b_i \leq 1000\). The function then checks if there is any common element between the sets created from `lst1` and `lst2`. If a common element is found, it prints 'YES' followed by '1' and the common element. If no common elements are found, it prints 'NO'. After processing all test cases, the function does not return any explicit value; instead, it relies on printing the results directly to the console for each test case.

