#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. Each test case consists of three integers n, f, and k such that 1 <= f, k <= n <= 100, followed by a list of n integers a_i where 1 <= a_i <= 100.
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
        
    #State: The loop has completed all its iterations. `num` is a positive integer, `n` is the integer obtained from the last input split, `f` is now `n - int(input())`, `k` is also `n - int(input())`, `a` is a list of integers obtained from the last input split sorted in descending order, `x` is the element at index `f` in the sorted list `a`, and the number of iterations left is 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n, f, and k, followed by a list of n integers. It sorts the list in descending order and checks if the k-th element is greater than the f-th element. If the k-th element is greater, it prints 'NO'. If the k-th element is less, it prints 'YES'. If the k-th element is equal to the f-th element, it prints 'YES' if the k-th element is the last element in the list or if the (k-1)-th element is less than the f-th element; otherwise, it prints 'MAYBE'. After processing all test cases, the function concludes with no remaining inputs to process.

