#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 3 ⋅ 10^5, and a is a list of n integers such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 ⋅ 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: Output State: After the loop executes all its iterations, `i` will be equal to `n-1`; `a` will be a list where each element `a[j]` (for 0 ≤ j < n) will be equal to the initial value of `a[j]` plus `j+1`.
    #
    #This means that if the loop runs `n` times, the final value of `a[j]` for any valid index `j` will be the initial value of `a[j]` increased by `j + 1`. The variable `n` itself will retain its initial value, and `i` will be set to `n - 1` after the last iteration.
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
        
    #State: Output State: The loop has executed all its iterations, resulting in `i` being equal to `len(a)`, `ans` containing all the elements as specified by the loop's logic, `cnt` being reduced to `0`, and `counter` having decremented the count of each element in `a` by the number of times it was appended to `ans`.
    #
    #To break it down:
    #- `i` will be `len(a)` because the loop increments `i` until it reaches the length of the list `a`.
    #- `ans` will contain all the elements generated according to the loop's logic, which involves decrementing the count of each element in `a` and appending the appropriate values to `ans`.
    #- `cnt` will be `0` since it is decremented by `adv` each time in the loop, and `adv` is always less than or equal to `cnt`.
    #- `counter` will reflect the final counts of each element in `a` after all elements have been processed and their counts decremented accordingly.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: Output State: The loop has executed all its iterations, resulting in `i` being equal to `len(a)`, `ans` containing a sequence of decremented values starting from the initial last element of `a` and decreasing by 1 for each iteration, `cnt` being reduced to `0`, and `counter` having decremented the count of each element in `a` by the number of times it was appended to `ans`.
    #
    #In simpler terms, after the loop completes all its iterations:
    #- `i` will be equal to the length of the list `a`.
    #- `ans` will be a list where the initial last element of `a` is repeatedly decremented by 1 for each iteration of the loop.
    #- `cnt` will be `0` since it is decremented with each iteration and cannot go below zero.
    #- `counter` will show the final counts of each element in `a` after all elements have been processed and their counts decremented according to the loop's logic.
    print(*ans)
    #This is printed: last_element_of_a last_element_of_a - 1 last_element_of_a - 2 ... 1 0 (where last_element_of_a is the last element of the list `a`)
#Overall this is what the function does:The function processes a list of integers `a` and generates a new list `ans` based on specific transformations. Initially, it increments each element in `a` by its index plus one. Then, it creates a counter for the elements in `a`, removes duplicates, sorts them in descending order, and calculates the difference between consecutive elements. It appends these differences to `ans` and adjusts the counter accordingly. Finally, it appends a sequence of decremented values starting from the last element of the modified list `a` until `cnt` becomes zero. The function prints the resulting list `ans`.

