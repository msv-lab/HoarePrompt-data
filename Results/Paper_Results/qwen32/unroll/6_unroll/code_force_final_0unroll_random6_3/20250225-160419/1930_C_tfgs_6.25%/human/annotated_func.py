#State of the program right berfore the function call: Each test case consists of an integer n (1 ≤ n ≤ 3 · 10^5) representing the length of array a, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of array a. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: `n` is an input integer representing the length of array `a`, and `a` is a list of integers where each element `a[i]` is incremented by `i + 1`.
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
        
    #State: n is an input integer representing the length of array a before duplicates were removed; a is a sorted list of integers in descending order with duplicates removed; counter is a Counter object that is empty; cnt is 0; ans is a list containing the integers from the original list a with duplicates inserted back in the correct positions.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: n is an input integer representing the length of array a before duplicates were removed; a is a sorted list of integers in descending order with duplicates removed; counter is a Counter object that is empty; cnt is 0; ans is a list containing the integers from the original list a with duplicates inserted back in the correct positions.
    print(*ans)
    #This is printed: the elements of the list `ans` (where `ans` contains the integers from the original list `a` with duplicates inserted back in the correct positions)
#Overall this is what the function does:The function reads an integer `n` and a list of `n` integers, increments each element of the list by its 1-based index, then outputs a list of integers where the original elements with duplicates inserted back in the correct positions are sorted in descending order.

