#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100. a is a list of n integers where each element a_i satisfies 1 <= a_i <= 100.
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
            print('YES' if k == n - 1 or a[k + 1] < x else 'MAYBE')
        
    #State: t is an integer such that 1 <= t <= 1000. For each test case, n, f, and k are integers such that 1 <= f, k <= n <= 100. a is a list of n integers where each element a_i satisfies 1 <= a_i <= 100.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives a list of integers `a` and two indices `f` and `k`. It then determines whether the element at index `f` (0-based) is among the top `k+1` largest elements in the list. It outputs 'YES' if the element is among the top `k+1` largest, 'NO' if it is not, and 'MAYBE' if it is the `k+1`-th largest and there are other elements equal to it.

