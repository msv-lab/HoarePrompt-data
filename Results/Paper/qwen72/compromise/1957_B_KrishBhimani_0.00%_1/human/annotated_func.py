#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n and k are integers for each test case such that 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. The sum of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: _ is t - 1, t is 0, l1 is a list of strings obtained from the input, n is the integer value of the first element in l1, k is 0, k0 is the integer value of the second element in l1, i is the number of bits in the binary representation of k0, arr contains all the indices of the bits that were set to 1 in the binary representation of k0, c is equal to n, ans is a list containing the values 1 << i for each i in arr, and if c is equal to n - 1, ans also contains the value k0 - sum(ans), and ans has been extended with (n - len(ans)) zeros.
#Overall this is what the function does:The function processes a series of test cases, each defined by integers `n` and `k` where 1 ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. For each test case, it generates a list `ans` of length `n` such that the sum of the elements in `ans` equals `k`. The list `ans` contains powers of 2 corresponding to the positions of set bits in the binary representation of `k`, and if necessary, the last element is adjusted to ensure the sum equals `k`. Any remaining positions in `ans` are filled with zeros. The function prints the elements of `ans` for each test case. After processing all test cases, the function concludes with `t` being 0, `k` being 0, and `ans` being the final list for the last test case.

