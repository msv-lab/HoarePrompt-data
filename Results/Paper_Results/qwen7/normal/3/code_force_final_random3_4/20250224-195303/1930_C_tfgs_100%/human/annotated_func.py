#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 3⋅10^5, and a is a list of n integers where 1 ≤ a_i ≤ 10^9. The sum of all n across all test cases does not exceed 3⋅10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: Output State: The value of `i` is `n-1`; for every index `j` in the list `a` where `0 ≤ j < n`, the value of `a[j]` is `j + (j + 1)`, which simplifies to `2j + 1`.
    #
    #In natural language: After the loop has executed all its iterations, the variable `i` will be equal to `n-1`. Each element `a[j]` in the list `a` (where `j` ranges from `0` to `n-1`) will have been incremented by `j + 1` for each iteration it was within the loop's range. Therefore, the final value of each element `a[j]` will be `2j + 1`.
    counter = Counter(a)
    cur = 0
    a = list(set(a))
    a.sort(reverse=True)
    cnt = n - len(a)
    ans = []
    for i in range(len(a)):
        if i > 0:
            adv = min(a[i - 1] - a[i] - 1, cnt, cur)
            for j in range(adv):
                ans.append(a[i - 1] - j - 1)
            cnt -= adv
            cur -= adv
        
        ans.append(a[i])
        
        counter[a[i]] -= 1
        
        cur += counter[a[i]]
        
    #State: Output State: The loop has executed all its iterations, meaning `i` has gone through every index of the list `a`. At this point, `cur` will be equal to the sum of `counter[a[i]]` for all remaining elements in `a` after the loop has run. `cnt` will be 0 because it gets reduced by `adv + 1` in each iteration until there are no more elements to process. Each `counter[a[i]]` will be decremented by 1 for each occurrence of `a[i]` in the original list `a`. The list `ans` will contain all the elements that were appended during the loop's execution, which includes the elements specified by the conditions in the loop body and the direct append of `a[i]` in each iteration.
    #
    #In simpler terms, after the loop completes, `cur` will hold the sum of the decremented counts of all elements in `a`, `cnt` will be 0, `counter` will reflect the decremented counts of each element, and `ans` will be a list containing all the elements specified by the loop's logic.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: After the loop executes all its iterations, `cnt` will be 0, `ans` will be a list where each element is the cumulative decrement from the last element, and `counter` will reflect the decremented counts of each element in the original list `a`.
    print(*ans)
    #This is printed: 0 (where 0 is the result of the cumulative decrement process applied to the original list `a`)
#Overall this is what the function does:The function processes a list of integers `a` for each test case. It first increments each element in the list by its index plus one. Then, it creates a frequency counter for the list, removes duplicates, sorts the list in descending order, and calculates the number of unique elements. It constructs a new list `ans` by appending elements based on certain conditions and performing cumulative decrements. Finally, it prints the resulting list `ans`, which contains the cumulative decremented values of the original list.

