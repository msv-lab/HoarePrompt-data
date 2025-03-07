#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 3 · 10^5, and a is a list of n integers where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer such that 1 ≤ n ≤ 3 · 10^5, `a` is a list of n integers where 1 ≤ a_i ≤ 10^9, `i` is `n-1`, and `n` must be greater than or equal to 1; for each index `j` in the list `a`, `a[j]` is now `a[j] + (j + 1)`.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 3 · 10^5, `a` is a sorted list of unique integers in descending order where 1 ≤ a_i ≤ 10^9, `i` is `len(a) - 1`, `counter` is a Counter object that counts the frequency of each integer in the updated list `a`, but the frequency of all elements in `a` is now 0, `cur` is 0, `cnt` is 0, `ans` is a list containing `n` integers, where the first `len(a)` elements are the elements of `a` in the same order, and the remaining elements are integers that fill the gaps between the elements of `a` such that all integers from 1 to the maximum element in `a` are represented in `ans`.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: `cnt` is 0, `ans` is updated with `cnt` new elements, each being the last element of `ans` minus 1, until the loop finishes.
    print(*ans)
    #This is printed: (nothing printed)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list `a` of `n` integers from the user input. It then modifies the list `a` by incrementing each element by its index plus one. After this, it processes the modified list to create a new list `ans` that contains `n` integers, where the first part of `ans` is the unique elements of `a` in descending order, and the remaining elements fill the gaps between these unique elements to ensure all integers from 1 to the maximum element in the modified `a` are represented. Finally, it prints the elements of `ans` separated by spaces. The function does not return any value.

