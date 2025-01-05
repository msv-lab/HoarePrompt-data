#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and k are integers such that 1 ≤ k < n ≤ 2 ⋅ 10^5. a_i is an integer such that 0 ≤ a_i ≤ 10^9.**
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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, `t` is between 1 and 1000, `n` and `k` are input integers, `arr` list is sorted in reverse order, `ans` is the sum of the first largest value in the list and the elements of `arr` from index 1 to `k`, `i` is `t`, `l` is in the range 1 to `k+1`. `ans` is printed.
#Overall this is what the function does:Functionality: The function `func` reads an integer `t` from the standard input, representing the number of test cases. For each test case, it reads integers `n` and `k`, followed by a list of integers `arr`. The function then sorts `arr` in reverse order, calculates the sum of the largest value in `arr` and the elements from index 1 to `k`, and prints this sum. The function handles multiple test cases as specified. However, the function lacks error handling for cases where the input parameters do not adhere to the specified constraints, such as `1 ≤ k < n ≤ 2 ⋅ 10^5` and `0 ≤ a_i ≤ 10^9`.

