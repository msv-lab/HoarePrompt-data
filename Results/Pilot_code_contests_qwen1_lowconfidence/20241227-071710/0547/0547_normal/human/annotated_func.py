#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n ≤ 10^5 and 0 ≤ k ≤ 10^7. The list skills is a sequence of n integers ai where 0 ≤ ai ≤ 100.
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
            
        #State of the program after the loop has been executed: `stop` is `True`, `k` is the original value of `k` minus the sum of `delta` for all elements in `nums` that are not equal to 100, and `nums` is a list where each element (except those that were originally 100) is now a multiple of 10.
        print(sum([(num / 10) for num in nums]))
    except (IOError):
        pass
    #State of the program after the try-except block has been executed: `n` and `k` are positive integers such that \(1 \leq n \leq 10^5\) and \(0 \leq k \leq 10^7\). `skills` is a sequence of `n` integers \(a_i\) where \(0 \leq a_i \leq 100\). `stop` is `True`, `k` is the original value of `k` minus the sum of `delta` for all elements in `nums` that are not equal to 100, and `nums` is a list where each element (except those that were originally 100) is now an integer obtained by dividing the original value by 10. If an `IOError` occurs, the state is unknown.
#Overall this is what the function does:The function processes a list of integers `nums` (representing skills) where each integer is between 0 and 100. It aims to make each element in the list a multiple of 10 by adding the smallest possible value to each element, up to a limit defined by the integer `k`. The function reads `n` and `k` from standard input, followed by a list of `n` integers. It then sorts the list in descending order based on the last digit of each integer. The function iterates through the list, attempting to increment each non-100 element to the nearest multiple of 10 within the remaining `k` capacity. If `k` is insufficient, the function stops. After processing, the function prints the sum of the integer divisions of each element by 10. If an `IOError` occurs during input, the function handles it silently. The final state of the program is that `n` and `k` retain their original values, `stop` is set to `True`, and `nums` contains elements that are multiples of 10 (unless they were originally 100), with `k` reduced accordingly.

