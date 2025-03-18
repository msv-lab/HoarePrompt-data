#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n. The sum of n over all test cases does not exceed 10^7.
def func():
    t = int(input())
    for tc in range(t):
        n, k = map(int, input().split())
        
        i = 0
        
        while 1 << i + 1 <= k:
            i = i + 1
        
        ans = [k - (1 << i), k + 1, k + 1 + (1 << i)]
        
        for j in range(20):
            if j != i:
                ans.append(1 << j)
        
        print(len(ans))
        
        print(*ans)
        
    #State: `t` retains the value of the number of test cases, `n` and `k` retain the values of the last test case, and `i` and `ans` do not exist.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k` where `n` is the size of a set and `k` is an integer such that `1 <= k <= n`. It then computes and prints the length of a list `ans` and the elements of `ans` based on the values of `n` and `k`. The list `ans` is constructed such that it contains specific values derived from `k` and powers of 2, excluding the power of 2 corresponding to the highest power less than or equal to `k`. After processing all test cases, the function terminates.

