#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 10^5 and 0 ≤ k ≤ 10^7. The list ai is a list of n integers where 0 ≤ ai ≤ 100.
def func():
    try:
        n, k = raw_input().split()
        n, k = int(n), int(k)
        nums = raw_input().split()
        nums = [int(num) for num in nums]
        nums.sort(cmp=lambda a, b: b % 10 - a % 10)
        stop = False
        while not stop:
            stop = True
            
            for i in range(0, n):
                if k == 0:
                    break
                if nums[i] == 100:
                    continue
                delta = 10 - nums[i] % 10
                if k < delta:
                    break
                stop = False
                nums[i] = nums[i] + delta
                k = k - delta
            
        #State of the program after the loop has been executed: `stop` is `True`, `k` is either `0` or less than `0`, `nums[i]` for each `i` such that `0 <= i < n` is adjusted to the nearest multiple of 10, `n` is `0`.
        print(sum([(num / 10) for num in nums]))
    except (IOError):
        pass
    #State of the program after the try-except block has been executed: 
#Overall this is what the function does:- If `k` is initially `0` or if all elements in `nums` are already multiples of 10, no changes are made, and the sum of the original list is printed.
- If `k` is sufficient to round up all elements to the next multiple of 10, the list `nums` will have all elements as multiples of 10, and the function will print their sum.
- The function does not handle cases where `nums` contains values outside the range \(0 \leq nums[i] \leq 100\). Such inputs would cause an error in the conversion to integers.

