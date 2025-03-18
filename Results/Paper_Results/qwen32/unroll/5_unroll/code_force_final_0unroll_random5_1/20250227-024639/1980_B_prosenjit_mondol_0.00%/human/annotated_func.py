#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100. a is a list of n integers such that 1 <= a_i <= 100 for each i from 1 to n.
def func():
    for _ in range(int(input())):
        n, f, k = map(int, input().split())
        
        f -= 1
        
        k -= 1
        
        a = list(map(int, input().split()))
        
        x = a[f]
        
        a.sort(reverse=True)
        
        if a[k] > x:
            print('NO')
        elif a[k] < x:
            print('YES')
        else:
            print('YES' if k == n - 1 or a[k - 1] < x else 'MAYBE')
        
    #State: The output state consists of 't' test cases, each with a result printed as either 'YES', 'NO', or 'MAYBE' based on the comparison of the f-th and k-th elements of the sorted list 'a'. The values of 't', 'n', 'f', 'k', and the list 'a' for each test case remain unchanged after the loop execution.
#Overall this is what the function does:The function processes `t` test cases, each consisting of integers `n`, `f`, and `k`, and a list `a` of `n` integers. For each test case, it determines and prints whether the `f`-th element of the list is among the `k` largest elements, resulting in one of three outputs: 'YES', 'NO', or 'MAYBE'.

