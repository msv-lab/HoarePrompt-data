#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 3 · 10^5, representing the length of the array a. a is a list of n integers where 1 ≤ a_i ≤ 10^9, representing the elements of the array a. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an input integer where 1 ≤ n ≤ 3 · 10^5, `a` is a list of n integers where 1 ≤ a_i ≤ 10^9, `a[i]` is now `a[i] + (i + 1)` for all 0 ≤ i < n, `i` is n-1.
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
        
    #State: The loop has finished executing all iterations. `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an integer where 1 ≤ n ≤ 3 · 10^5, `a` is a sorted list of unique integers in descending order with at least 1 element, each integer was originally in the range 1 ≤ a_i ≤ 10^9 and has been incremented by (i + 1) for all 0 ≤ i < n, `i` is `len(a) - 1`, `counter` is a Counter object that counts the occurrences of each integer in the updated list `a`, all values in `counter` are 0, `cur` is 0, `cnt` is 0, `ans` is a list containing all the elements of `a` and additional elements that were appended during the loop execution, such that the total length of `ans` is `n`.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: The loop has finished executing all iterations. `t` is an integer where 1 ≤ t ≤ 10^4, `n` is an integer where 1 ≤ n ≤ 3 · 10^5, `a` is a sorted list of unique integers in descending order with at least 1 element, each integer was originally in the range 1 ≤ a_i ≤ 10^9 and has been incremented by (i + 1) for all 0 ≤ i < n, `i` is `len(a) - 1`, `counter` is a Counter object that counts the occurrences of each integer in the updated list `a`, all values in `counter` are 0, `cur` is 0, `cnt` is 0, `ans` is a list containing all the elements of `a` and `cnt` additional elements, each of which is one less than the previous element, such that the total length of `ans` is `n + cnt`.
    print(*ans)
    #This is printed: a_0 a_1 a_2 ... a_(n-1) (where a_0, a_1, ..., a_(n-1) are the elements of the list `a` in descending order)
#Overall this is what the function does:The function `func_1` processes a series of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It then increments each element of `a` by its index plus one. After processing, it generates a new list `ans` that contains unique, sorted (in descending order) elements from the updated `a`, along with additional elements to ensure the length of `ans` is `n`. The function prints the elements of `ans` in descending order.

