#State of the program right berfore the function call: **Precondition**: **t is an integer such that 1 <= t <= 1000. n and k are integers such that 1 ≤ k < n ≤ 2 ⋅ 10^5. a_i is an integer such that 0 ≤ a_i ≤ 10^9.**
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
        
    #State of the program after the  for loop has been executed: `t` is adjusted based on conditions, `n` is adjusted based on conditions, `k` is adjusted based on conditions, `arr` is a list of integers sorted in descending order, `ans` is the sum of the first element of `arr` and a subset of elements from `arr` based on the value of `k`
#Overall this is what the function does:The function `func` reads an integer `t` from the standard input and then iterates `t` times. For each iteration, it reads two integers `n` and `k`, followed by a list of integers `arr`. The function sorts `arr` in descending order, calculates the sum of the first element and a subset of elements from `arr` based on the value of `k`, and prints the result. The function modifies `k` if it is greater than or equal to `n`.

