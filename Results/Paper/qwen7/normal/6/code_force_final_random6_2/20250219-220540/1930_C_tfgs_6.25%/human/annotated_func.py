#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a is a list of n integers where 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n. The sum of n over all test cases does not exceed 3⋅10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: Output State: The value of `a[i]` for each valid index `i` (where \(0 \leq i < n\)) will have been increased by `(i + 1)` for every iteration of the loop. The variable `n` remains unchanged and must satisfy \(1 \leq n \leq 3 \times 10^5\).
    counter = Counter(a)
    a = list(set(a))
    a.sort(reverse=True)
    cnt = n - len(a)
    ans = []
    for i in range(len(a)):
        if i > 0:
            adv = min(a[i - 1] - a[i] - 1, cnt, counter[a[i - 1]])
            for j in range(adv):
                ans.append(a[i - 1] - j - 1)
            cnt -= adv
            counter[a[i - 1]] -= adv
        
        ans.append(a[i])
        
        counter[a[i]] -= 1
        
    #State: Output State: The loop has executed all iterations, resulting in `i` being equal to `len(a)`. The list `ans` contains all elements from the original list `a` in the order they were appended, minus any decrements due to the condition inside the loop. Specifically, for each `a[i - 1]`, if there was enough `cnt` and matching elements in `counter`, some values were appended to `ans` based on the decrement logic. After all iterations, `cnt` is fully exhausted (`cnt == 0`), and `counter` for each element in `a` reflects the total number of times that element was decremented, which could be negative if the element was decremented more times than it existed in the list initially. `ans` is a list that captures the decrement logic applied to each element in `a` as per the loop's conditions, and `counter` reflects the final count of each element after all operations.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: The loop has executed all its iterations, resulting in `i` being equal to `len(a)`. The list `ans` contains the final values after applying the decrement logic to each element in `a` as specified by the loop's conditions. Each element in `a` is decremented according to the available `cnt` and the matching elements in `counter`. After all iterations, `cnt` is fully exhausted (`cnt == 0`), and `counter` for each element in `a` reflects the total number of times that element was decremented, which could be negative if the element was decremented more times than it existed in the list initially. `ans` is a list that captures the decrement logic applied to each element in `a` as per the loop's conditions, and `counter` reflects the final count of each element after all operations.
    print(*ans)
    #This is printed: the elements of the ans list (which are the final values after the decrement logic has been applied to each element in a)
#Overall this is what the function does:The function processes a list of integers `a` for each test case. It first increments each element in the list by its index plus one. Then, it creates a counter for the elements in the list, removes duplicates, sorts the list in descending order, and calculates a decrement count. Based on this count and the counter, it generates a new list `ans` by appending elements from the processed list `a` and applying decrement logic. Finally, it appends additional decremented values to `ans` if needed and prints the resulting list.

