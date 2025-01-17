#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2·10^5. lecturers is a list of pairs (l_i, r_i), where each pair represents the range of days [l_i, r_i] (1 ≤ l_i ≤ r_i ≤ 2·10^5) that the i-th lecturer is available to perform.
def func_1(n, lecturers):
    max_day = 200000
    availability = [0] * (max_day + 2)
    for (l, r) in lecturers:
        availability[l] += 1
        
        availability[r + 1] -= 1
        
    #State of the program after the  for loop has been executed: `lecturers` is a list of pairs \((l_i, r_i)\), and `availability` is a list of 200002 integers where each element from index 1 to 200000 reflects the net number of lecturers available on that day, and the elements at indices 200001 and 200002 are 0.
    current_available = 0
    available_days = [0] * (max_day + 1)
    for day in range(1, max_day + 1):
        current_available += availability[day]
        
        available_days[day] = current_available
        
    #State of the program after the  for loop has been executed: `lecturers` is a list of pairs \((l_i, r_i)\), `availability` is a list of 200002 integers where each element from index 1 to 200000 reflects the net number of lecturers available on that day, and the elements at indices 200001 and 200002 are 0, `current_available` is the sum of all `availability[i]` for `i` from 1 to `max_day`, `available_days` is a list of length 200001 where each element is the cumulative sum of `availability[i]` from 1 to `i`, and `day` is `max_day + 1`.
    result = [0] * (n + 1)
    for k in range(1, n + 1):
        count = 0
        
        current_window_sum = sum(available_days[1:k + 1])
        
        if current_window_sum >= k:
            count += 1
        
        for start in range(2, max_day - k + 2):
            current_window_sum += available_days[start + k - 1] - available_days[
                start - 1]
            if current_window_sum >= k:
                count += 1
        
        result[k] = count
        
    #State of the program after the  for loop has been executed: `start` is in the range `[2, max_day - k + 1]`, `count` is the total number of times `current_window_sum` was greater than or equal to `k` during the loop's execution, `current_window_sum` is the sum of the last `k` elements starting from `available_days[start - 1]`, and `result[k]` is equal to `count`.
    return result[1:]
    #`The program returns a list containing the values of `result` starting from index 1 to the end
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list of pairs representing lecturer availability. It calculates and returns a list of integers, where the `k`-th element (starting from index 1) indicates the number of non-overlapping windows of length `k` that can be formed within the given lecturer availability periods. Each window must have at least one lecturer available.

