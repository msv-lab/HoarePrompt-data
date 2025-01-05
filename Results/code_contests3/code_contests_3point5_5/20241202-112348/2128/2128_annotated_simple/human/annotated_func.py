#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and k are integers such that 1 ≤ k < n ≤ 2*10^5. a_i is an integer such that 0 ≤ a_i ≤ 10^9.**
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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, the values of `t`, `n`, `k`, `arr`, `ans`, and `i` will be as follows: `t` will be the same as the input value, `n` will be assigned a value from the input, `k` will be one less than `n`, `arr` will be a list of integers sorted in descending order from the input, `ans` will be the sum of the first `k+1` elements of `arr`, and `i` will be equal to `t`.
#Overall this is what the function does:The function `func` reads an integer `t` from standard input and then for each test case within the range of `t`, it reads integers `n` and `k`, as well as a list of integers `a_i`. It sorts the list `a_i` in descending order, calculates the sum of the first `k+1` elements of the sorted list, and prints this sum. The function ensures that `k` is less than `n-1`. The constraints for the input parameters are specified. The function does not return any value but processes multiple test cases as described.

