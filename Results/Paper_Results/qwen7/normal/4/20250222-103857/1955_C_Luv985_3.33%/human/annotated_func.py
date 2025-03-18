#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^{15}. a is a list of n positive integers such that 1 ≤ a_i ≤ 10^9, where a_i represents the durability of the i-th ship. The sum of all n across all test cases does not exceed 2⋅10^5.
def func():
    """
        @Time : 2024/8/26 17:59
        @Author : Zhiliang.L
        @Email : 2410103062@mails.edu.cn
        @File : 1955-C.py
    """
    T = int(input())
    while T:
        T -= 1
        
        n, k = input().split()
        
        n = int(n)
        
        k = int(k)
        
        a = input().split()
        
        a = list(map(lambda x: int(x), a))
        
        l = 0
        
        r = n - 1
        
        ans = 0
        
        while l < r and k > 0:
            mi = min(a[l], a[r])
            if mi * 2 <= k:
                a[l] -= mi
                a[r] -= mi
                k -= mi * 2
                if a[l] == 0:
                    ans += 1
                    l += 1
                if a[r] == 0:
                    ans += 1
                    r -= 1
            else:
                t = k % 2
                if mi - t - k // 2 == 0:
                    ans += 1
                break
        
        if l == r:
            ans += k >= a[l]
        
        print(ans)
        
    #State: Output State: `T` is 0, `n` is the number of elements in the final list `a`, `k` is 0, `a` is a list of integers where all elements except possibly one are 0, `l` is `n - 1`, `r` is 0, `ans` is the total number of times the inner loop was able to reduce the elements of `a` by their minimum value, `mi` is the minimum of `a[l]` and `a[r]`, and `t` is `k % 2` from the last iteration (which is 0 since `k` is 0).
    #
    #After all iterations of the loop, `T` will be 0 because it is decremented by 1 each time the loop runs and we assume it starts at a value that allows the loop to run until `T` reaches 0. The variable `k` will be 0 after all reductions are made. The list `a` will have all its elements reduced to 0 except possibly one element if the remaining `k` value is exactly equal to the last remaining element. The variable `l` will be `n - 1` and `r` will be 0, as these are the indices used in the loop. The variable `ans` will hold the total count of reductions made during the process. The variable `mi` will be the minimum of `a[l]` and `a[r]` at the last step, and `t` will be 0 since `k` is 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a number of ships (represented by their durabilities in a list), and a threshold value k. For each test case, the function repeatedly reduces the durabilities of the ships by their minimum value until the sum of the reductions exceeds k. It counts the number of times the durabilities are reduced and prints this count for each test case. If any ship's durability remains after processing, it checks if the remaining value is exactly equal to k. If so, it increments the count. The function handles up to 10,000 test cases, with each test case involving up to 200,000 ships, and a threshold value k up to \(10^{15}\).

