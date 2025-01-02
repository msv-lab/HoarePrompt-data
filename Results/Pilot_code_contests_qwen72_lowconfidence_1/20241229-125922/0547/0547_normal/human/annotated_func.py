#State of the program right berfore the function call: n and k are integers such that 1 ≤ n ≤ 105 and 0 ≤ k ≤ 107; a list of n integers ai (0 ≤ ai ≤ 100) representing the levels of the character's skills.
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
            
        #State of the program after the loop has been executed: `n` is a non-negative integer, `k` is the remaining value after attempting to adjust all eligible elements in `nums` (where `nums[i]` was less than 100 and the adjustment did not exceed the available `k`), `a` is a list of `n` integers where each `ai` (0 ≤ `ai` ≤ 100) represents the levels of the character's skills, `nums` is a list of integers where each element that was less than 100 and could be increased by `delta` without exceeding `k` has been incremented by its respective `delta` (making the last digit 10), and the rest of the elements are sorted based on the last digit in descending order, `stop` is `True` if no further adjustments can be made, otherwise `False`.
        print(sum([(num / 10) for num in nums]))
    except (IOError):
        pass
    #State of the program after the try-except block has been executed: `n` is a non-negative integer, `k` is the remaining value after attempting to adjust all eligible elements in `nums`, `a` is a list of `n` integers where each `ai` (0 ≤ `ai` ≤ 100) represents the levels of the character's skills, `nums` is a list of integers where each element that was less than 100 and could be increased by `delta` without exceeding `k` has been incremented by its respective `delta` (making the last digit 10), and the rest of the elements are sorted based on the last digit in descending order, `stop` is `True` if no further adjustments can be made, otherwise `False`. If an `IOError` occurs, the state is unknown and no further processing is done.
#Overall this is what the function does:The function reads two integers `n` and `k`, and a list of `n` integers representing skill levels. It then attempts to increase the skill levels in the list such that the last digit of each skill level becomes 0, using up to `k` total increments. The function sorts the skill levels based on their last digit in descending order before making the adjustments. After the adjustments, the function prints the sum of the skill levels divided by 10. If an `IOError` occurs during input, the function silently catches the error and does nothing further. The final state is that `n` remains a non-negative integer, `k` is the remaining value after adjustments, and `nums` is a list of integers where each element that was less than 100 and could be increased by `delta` without exceeding `k` has been incremented to make the last digit 0, with the rest sorted based on the last digit in descending order.

