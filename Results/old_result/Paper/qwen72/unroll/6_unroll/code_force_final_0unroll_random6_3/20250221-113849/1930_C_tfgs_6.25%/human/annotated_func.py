#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of n integers where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: The list `a` is modified such that each element `a[i]` is increased by `i + 1`. The values of `t` and `n` remain unchanged.
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
        
    #State: Output State: The list `a` remains sorted in descending order, the values of `t` and `n` remain unchanged, `counter` contains the updated frequency count of the unique elements in the modified list `a` (with some elements possibly being reduced), `cnt` is equal to `n - len(a) - total number of elements added to `ans` that were not originally in `a`), and `ans` is a list containing the original elements of `a` along with additional elements that were added to ensure the final length of `ans` is `n`.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: Output State: The list `a` remains sorted in descending order, the values of `t` and `n` remain unchanged, `counter` contains the updated frequency count of the unique elements in the modified list `a` (with some elements possibly being reduced), `cnt` is equal to `n - len(a) - total number of elements added to `ans` that were not originally in `a`), and `ans` is a list containing the original elements of `a` along with additional elements that were added to ensure the final length of `ans` is `n`. The additional elements appended to `ans` are consecutive integers, each one less than the previous, starting from the last element of `ans` minus one.
    print(*ans)
    #This is printed: [5, 4, 3, 2, 1, 0, -1, -2, -3, -4] (where the original elements of `a` are in descending order, and the additional elements are consecutive integers starting from the last element of `a` minus one, ensuring the final length of `ans` is `n`)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list `a` of `n` integers from the user. It modifies `a` by incrementing each element `a[i]` by `i + 1`. The function then ensures that the final list `ans` has exactly `n` elements, where the elements are the unique, sorted (in descending order) modified elements of `a`, along with additional elements added to fill the list to length `n`. These additional elements are consecutive integers, each one less than the previous, starting from the last element of the sorted list minus one. The function prints the final list `ans` and does not return any value. The values of `t` and `n` remain unchanged throughout the function execution.

