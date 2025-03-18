#State of the program right berfore the function call: The function should take two parameters, n and k, where n is an integer such that 1 ≤ n ≤ 2 · 10^5, and k is an integer such that 1 ≤ k ≤ 10^9.
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
        
    #State: The loop has executed the specified number of times, and for each iteration, the following conditions hold: `n` is the first integer from `l1`, `k` is 0, `k0` is the second integer from `l1`, `arr` contains the indices of the bits that were set to 1 in the binary representation of `k0`, `i` is the last element in `arr`, `c` is the number of elements in `arr`, and `ans` is a list of length `n` where each element is `1 << i` for each `i` in `arr` up to the point where `c` equals `n - 1`. If `c` equals `n - 1` before the loop finishes, the last element in `ans` is `k0 - sum(ans[:-1])`. Any remaining elements in `ans` are 0.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. Instead, it reads input from the user, processes it, and prints the result. For each test case, it takes two integers `n` and `k` from the input, where `1 ≤ n ≤ 2 · 10^5` and `1 ≤ k ≤ 10^9`. The function then generates a list `ans` of length `n` such that the sum of the elements in `ans` equals `k`. The elements in `ans` are powers of 2 corresponding to the positions of the set bits in the binary representation of `k`, with any remaining positions filled with 0. If the sum of the generated powers of 2 is less than `k`, the last element in `ans` is adjusted to ensure the total sum equals `k`. The function prints the elements of `ans` for each test case.

