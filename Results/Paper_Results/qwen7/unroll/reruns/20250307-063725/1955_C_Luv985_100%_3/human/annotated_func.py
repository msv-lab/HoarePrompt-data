#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^15. a is a list of n positive integers such that 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n. The sum of all n across all test cases does not exceed 2⋅10^5.
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
                if a[l] - t - k // 2 == 0:
                    ans += 1
                break
        
        if l == r:
            ans += k >= a[l]
        
        print(ans)
        
    #State: Output State: The value of `ans`, which represents the number of elements in the list `a` that become zero after performing the operations specified in the loop for each test case.
    #
    #The loop processes each test case defined by `T`. For each test case, it initializes `n` and `k`, reads the list `a` of length `n`, and then iterates through the list to reduce its elements based on the value of `k`. The variable `ans` keeps track of how many elements in `a` become zero after these operations. If at any point the remaining elements cannot be reduced further with the given `k`, the loop breaks. After processing all elements or when `l` equals `r`, it checks if the last element can be reduced by `k` and increments `ans` accordingly. Finally, it prints the total count of zeros in the list `a` across all test cases.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( T \), followed by pairs of integers \( n \) and \( k \), and a list \( a \) of \( n \) positive integers. For each test case, it reduces the elements of the list \( a \) based on the value of \( k \) until no more reductions can be made. It counts the number of elements in \( a \) that become zero after these operations and prints the total count of such elements across all test cases.

