#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n, f, and k are integers such that 1 ≤ f, k ≤ n ≤ 100. a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 100.
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
        
    #State: A series of t outputs, each being 'YES', 'NO', or 'MAYBE', corresponding to the results of each test case.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it receives integers `n`, `f`, and `k`, and a list `a` of `n` integers. It determines if the `f`-th favorite value in the list can be completely removed within the top `k` largest values of the list, and prints 'YES', 'NO', or 'MAYBE' based on this condition.

