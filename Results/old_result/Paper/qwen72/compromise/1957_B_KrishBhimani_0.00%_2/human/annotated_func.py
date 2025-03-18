#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9 for each test case.
def func():
    for _ in range(int(input())):
        l1 = input().split()
        
        n, k = list(map(int, l1))
        
        arr = []
        
        k0 = k
        
        i = 0
        
        while k:
            if k & 1 == 1:
                arr.append(i)
            k = k >> 1
            i += 1
        
        ans = []
        
        c = 0
        
        for i in arr:
            if c == n - 1:
                ans.append(k0 - sum(ans))
                break
            c += 1
            ans.append(1 << i)
        
        ans += [0] * (n - len(ans))
        
        print(*ans)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `_` is `t - 1`, `l1` is a list of strings obtained from the input, `n` is the integer value of the first element in `l1`, `k` is 0, `k0` is the integer value of the second element in `l1`, `i` is the last element in `arr`, `arr` is a list of indices where the binary representation of `k0` has 1s, `ans` is a list of length `n` containing the values `1 << i` for each `i` in `arr` up to `n-1` elements. If `c` equals `n - 1`, `ans` also contains an additional element which is `k0 - sum(ans[:-1])`. The remaining elements (if any) are zeros.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n` and `k` where 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. For each test case, it generates a list `ans` of length `n` such that the sum of the elements in `ans` equals `k`. The elements in `ans` are powers of 2 corresponding to the positions of 1s in the binary representation of `k`, up to `n-1` elements. If the number of 1s in the binary representation of `k` is less than `n`, the remaining elements in `ans` are set to 0. If the number of 1s is exactly `n-1`, the last element in `ans` is adjusted to ensure the sum equals `k`. The function prints the list `ans` for each test case.

