#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, n and k are integers satisfying 2 <= n <= 10^6 and 1 <= k <= n. Additionally, the sum of all n values across all test cases does not exceed 10^7.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        nums = [(1 << i) for i in range(24)]
        
        idx = 0
        
        while k >= 1 << idx:
            idx += 1
        
        idx -= 1
        
        nums.append(k - nums[idx])
        
        nums.append(k + 1)
        
        nums.append(k + nums[idx] + 1)
        
        nums.remove(1 << idx)
        
        print(len(nums))
        
        print(*nums)
        
    #State: Output State: t test cases are processed, and for each test case, the length of the list `nums` and the elements in `nums` are printed. The list `nums` contains the following elements after processing each test case: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, k - 2^idx, k + 1, k + 2^idx + 1], where `k` is the second input number for each test case and `idx` is the highest power of 2 less than or equal to `k`. The length of `nums` is 25 for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( t \), \( n \), and \( k \). For each test case, it constructs a list `nums` containing specific values derived from \( k \) and prints the length of `nums` followed by its elements. The list `nums` always contains 25 elements and includes powers of 2 up to the highest power less than or equal to \( k \), along with \( k - 2^{\text{idx}} \), \( k + 1 \), and \( k + 2^{\text{idx}} + 1 \), where \( \text{idx} \) is the highest power of 2 less than or equal to \( k \).

