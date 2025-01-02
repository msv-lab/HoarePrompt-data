#State of the program right berfore the function call: n and k are positive integers such that 1 ≤ n ≤ 10^5 and 0 ≤ k ≤ 10^7. The list ai is a list of n integers where 0 ≤ ai ≤ 100.
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
            
        #State of the program after the loop has been executed: Let's analyze the loop step by step to determine the final state of the variables after all iterations have executed.
        #
        #### Initial State:
        #- `n` is a non-negative integer.
        #- `k` is an integer.
        #- `nums` is a list of integers sorted in descending order based on the last digit of each integer.
        #- `stop` is `False`.
        #
        #### Loop Analysis:
        #The loop continues as long as `stop` is `False`. Inside the loop, there is a `for` loop that iterates from `0` to `n-1`. For each iteration of the `for` loop, the following steps are performed:
        #1. Check if `k` is 0. If so, break out of the loop.
        #2. Skip the iteration if `nums[i]` is 100.
        #3. Calculate `delta` as `10 - (nums[i] % 10)`.
        #4. If `k` is less than `delta`, break out of the loop.
        #5. Update `nums[i]` to `nums[i] + delta` and decrease `k` by `delta`.
        #6. Set `stop` to `False`.
        #
        #### After Loop Executes 1 Time:
        #- `n` is a non-negative integer.
        #- `k` is 0 or a non-positive integer.
        #- `stop` is `True`.
        #- `i` is `n` or the index where the loop broke.
        #- `nums` is a list of integers sorted in descending order based on the last digit of each integer, with some elements possibly updated.
        #
        #### After Loop Executes 2 Times:
        #- `n` is a non-negative integer.
        #- `k` is 0 or a non-positive integer.
        #- `stop` is `False` if the loop broke due to `k` being less than `delta` or `nums[i]` being 100.
        #- `i` is `n` or the index where the loop broke.
        #- `nums` is a list of integers sorted in descending order based on the last digit of each integer, with some elements possibly updated.
        #
        #### General Pattern:
        #- The loop continues until either `k` becomes 0 or the loop breaks due to reaching the end of the list or encountering a 100.
        #- If `k` becomes 0, the loop stops, and `stop` becomes `True`.
        #- If the loop breaks due to `k` being less than `delta` or `nums[i]` being 100, `stop` remains `False` and `i` will be the index where the loop broke.
        #- Elements in `nums` that were not 100 and were within the loop's range are updated according to the calculation `nums[i] + delta`.
        #
        #### Final Output State:
        #- If `k` becomes 0, `stop` is `True`, and all elements in `nums` that were not 100 and within the loop's range are updated.
        #- If `k` does not become 0, `stop` remains `False`, and the loop may have broken due to `k` being less than `delta` or encountering a 100.
        #
        #Thus, the final output state is:
        #
        #**Output State: `n` is a non-negative integer, `k` is 0 or a non-positive integer, `stop` is `True` if `k` became 0, otherwise `stop` is `False`, `i` is the index where the loop broke or `n`, `nums` is a list of integers sorted in descending order based on the last digit of each integer, with some elements possibly updated.**
        print(sum([(num / 10) for num in nums]))
    except (IOError):
        pass
    #State of the program after the try-except block has been executed: - If the `IOError` occurs, the program passes through the except block without changing the state of the variables.
    #   - If no exception occurs, the final state includes:
    #     - `n` and `k` as positive integers within the specified ranges.
    #     - `stop` as a boolean indicating whether the loop terminated because `k` became 0.
    #     - `i` as an index that represents where the loop broke or the value of `n` if the loop completed normally.
    #     - `nums` as a list of integers sorted in descending order based on their last digit, with some elements possibly updated.
    #     - The program prints the sum of the quotients when each number in `nums` is divided by 10.
    #
    #### Example Answer:
    #A `IOError` might be triggered if there is an issue reading input from the standard input. If the input is correctly read and processed, the program sorts the list `nums` based on the last digit of each integer and updates some elements to make them multiples of 10, up to the limit of `k`. After processing, it prints the sum of the quotients when each number in `nums` is divided by 10. If an `IOError` occurs, the state remains unchanged.
    #
    #Therefore, the output state is:
    #Output State:
#Overall this is what the function does:The function processes a list of integers `nums` (of length `n`) and an integer `k`. It sorts the list in descending order based on the last digit of each integer. Then, it iteratively increases the last digit of each element in `nums` to the nearest multiple of 10 (if possible) using up to `k` units of "change". The process stops when `k` is depleted, the end of the list is reached, or all elements in the list are already multiples of 10. Finally, it prints the sum of the quotients when each number in the updated list is divided by 10. If an `IOError` occurs during input reading, the function handles it gracefully without changing the state of the variables.

