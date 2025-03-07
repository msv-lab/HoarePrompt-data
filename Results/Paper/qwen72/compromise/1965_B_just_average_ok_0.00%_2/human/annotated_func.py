#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 2 <= n <= 10^6 and 1 <= k <= n.
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
        
    #State: For each test case, the loop prints the length of the modified `nums` list and the elements of the modified `nums` list. The `nums` list initially contains powers of 2 from 1 to \(2^{23}\). After the loop, it contains the same elements as before, but with the element \(2^{\text{idx}}\) removed and three new elements appended: \(k - 2^{\text{idx}}\), \(k + 1\), and \(k + 2^{\text{idx}} + 1\). The value of `t` remains unchanged, and the values of `n` and `k` are re-assigned for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. It accepts an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `2 <= n <= 10^6` and `1 <= k <= n`. The function modifies a list `nums` that initially contains powers of 2 from \(2^0\) to \(2^{23}\). After processing each test case, the list `nums` is updated by removing the element \(2^{\text{idx}}\) (where \(\text{idx}\) is the largest integer such that \(2^{\text{idx}} \leq k\)) and appending three new elements: \(k - 2^{\text{idx}}\), \(k + 1\), and \(k + 2^{\text{idx}} + 1\). The function then prints the length of the modified `nums` list followed by the elements of the list. The value of `t` remains unchanged, and the values of `n` and `k` are re-assigned for each test case.

