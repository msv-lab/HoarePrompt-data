#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000; for each test case, n is an integer such that 1 ≤ k < n ≤ 2 ⋅ 10^5, k is a non-negative integer, and a_i are integers such that 0 ≤ a_i ≤ 10^{9} for i = 1 to n. The total sum of n over all test cases does not exceed 2 ⋅ 10^5.
def func():
    t = int(sys.stdin.readline())
    for i in range(0, t):
        n, k = map(int, sys.stdin.readline().split(' '))
        
        arr = list(map(int, sys.stdin.readline().split()))
        
        arr = sorted(arr, reverse=True)
        
        ans = arr[0]
        
        if k >= n:
            k = n - 1
        
        for l in range(1, k + 1):
            ans += arr[l]
        
        print(ans)
        
    #State of the program after the  for loop has been executed: `k` is at least `n`, `t` is within the range 1 to 1000, `ans` is the sum of the largest element of `arr` and the sum of the elements from `arr[1]` to `arr[k]`, `i` is `t`, `arr` is sorted in descending order, `l` is equal to `k + 1`, `n` is the last value assigned from input, and `ans` is printed for each iteration.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads two integers `n` and `k`, and a list of integers `a_i`. It calculates the sum of the largest element in the sorted list and the next `k` largest elements, ensuring that if `k` is greater than or equal to `n`, it only sums up to the last element of the list. The function prints the result for each test case but does not return any value.

