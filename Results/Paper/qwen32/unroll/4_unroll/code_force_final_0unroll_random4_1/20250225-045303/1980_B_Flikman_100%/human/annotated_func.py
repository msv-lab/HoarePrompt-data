#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100. a is a list of n integers such that 1 <= a_i <= 100 for each i from 0 to n-1.
def func():
    t = int(input())
    for _ in range(t):
        n, f, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        favorite_value = a[f - 1]
        
        sorted_a = sorted(a, reverse=True)
        
        removed_count = 0
        
        for i in range(k):
            if sorted_a[i] == favorite_value:
                removed_count += 1
        
        favorite_count = sorted_a.count(favorite_value)
        
        if removed_count == favorite_count:
            print('YES')
        elif removed_count == 0:
            print('NO')
        else:
            print('MAYBE')
        
    #State: The output state consists of t lines, each containing either 'YES', 'NO', or 'MAYBE' based on the conditions checked within the loop. The variable `t` remains unchanged, representing the number of test cases. The variables `n`, `f`, `k`, and `a` are re-assigned in each iteration of the loop based on the input for each test case and are not preserved across iterations. After all iterations, the only state that remains relevant is the sequence of printed outputs ('YES', 'NO', 'MAYBE') corresponding to each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `f`, `k`, and a list `a` of `n` integers. For each test case, it determines if the `f`-th element in the list `a` (considered the favorite value) can be removed within the first `k` largest elements of the list. It prints 'YES' if all occurrences of the favorite value are among the `k` largest elements, 'NO' if none of the favorite value is among the `k` largest elements, and 'MAYBE' otherwise.

