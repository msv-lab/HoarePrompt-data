#State of the program right berfore the function call: Each test case consists of an integer n (1 ≤ n ≤ 3 · 10^5) representing the length of array a, and a list of integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of array a. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: `n` is the same input integer representing the length of array `a`, and `a` is now a list where each element at index `i` is the original value at that index plus `i + 1`.
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
        
    #State: `n` is the same input integer representing the original length of array `a`; `a` is a sorted list in descending order, where each element at index `i` is the original value at that index plus `i + 1`, with duplicates removed; `counter` is a Counter object with updated counts after the loop; `cnt` is the number of duplicates removed minus the number of elements added to `ans` that were not originally in `a`; `ans` is a list containing all elements from `a` and additional elements calculated within the loop.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: `n` is the same input integer representing the original length of array `a`; `a` is a sorted list in descending order, where each element at index `i` is the original value at that index plus `i + 1`, with duplicates removed; `counter` is a Counter object with updated counts after the loop; `cnt` is the number of duplicates removed minus the number of elements added to `ans` that were not originally in `a`; `ans` is a list containing all elements from `a` and `cnt` additional elements, each one less than the previous one.
    print(*ans)
    #This is printed: [elements of `a`], [last element of `a` - 1], [last element of `a` - 2], ..., [last element of `a` - cnt] (where `a` is the modified and deduplicated list and `cnt` is the number of additional elements)
#Overall this is what the function does:The function `func_1` reads an integer `n` and a list of integers `a` of length `n`. It modifies each element of `a` by adding its 1-based index to it, removes duplicates, sorts the list in descending order, and then constructs a new list `ans` that includes all elements from the modified `a` and additional elements that fill gaps between consecutive elements in descending order, ensuring the total length of `ans` is `n`. Finally, it prints the elements of `ans`.

