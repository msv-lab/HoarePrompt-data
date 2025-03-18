#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^15. a is a list of n positive integers such that 1 ≤ a_i ≤ 10^9, where a_i represents the durability of the i-th ship. The sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The output state will be the total number of elements in the list `a` that become zero after performing the operations specified in the loop for all given inputs.
    #
    #Explanation: The loop processes each input pair `(n, k)` and a list `a` of length `n`. It repeatedly reduces the values at the left (`l`) and right (`r`) ends of the list by the minimum of the two until the sum of reductions exceeds `k` or one of the ends becomes zero. If the remaining value at either end is less than or equal to `k`, it is fully reduced, counting as one operation. The process continues until `T` (initially set by user input) becomes zero, meaning all inputs have been processed. The final output is the total count of such operations performed across all inputs.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it receives a positive integer \( n \), another positive integer \( k \), and a list of \( n \) positive integers representing the durability of ships. The function repeatedly reduces the durability of the ships at the left and right ends of the list by the minimum of their current values until the sum of reductions exceeds \( k \) or one of the ends becomes zero. The function counts the number of times the durability of any ship becomes zero and prints the total count after processing all test cases.

