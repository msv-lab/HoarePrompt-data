#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, the first line contains an integer n (1 ≤ n ≤ 3 · 10^5) representing the length of array a. The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the elements of array a. The sum of n over all test cases does not exceed 3 · 10^5.
def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] += i + 1
        
    #State: `a` is a list of `n` integers where each integer at index `i` is the original integer at that index plus `i + 1`.
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
        
    #State: `a` is a list of unique integers derived from the original list where each integer at index `i` was the original integer at that index plus `i + 1`, sorted in descending order; `counter` is a Counter object that counts the frequency of each element in the original list `a` minus 1; `cur` is the sum of the remaining counts in `counter` after decrementing each by 1; `cnt` is `n - len(a)` reduced by the number of elements inserted into `ans` between the elements of `a`; `ans` is a list containing all elements from `a` in their original order, plus any additional elements inserted between them.
    for _ in range(cnt):
        ans.append(ans[-1] - 1)
        
    #State: `a` is a list of unique integers derived from the original list where each integer at index `i` was the original integer at that index plus `i + 1`, sorted in descending order; `counter` is a Counter object that counts the frequency of each element in the original list `a` minus 1; `cur` is the sum of the remaining counts in `counter` after decrementing each by 1; `cnt` is `n - len(a)` reduced by the number of elements inserted into `ans` between the elements of `a`; `ans` is a list containing all elements from `a` in their original order, plus `cnt` additional elements inserted between them, each being one less than the previous element.
    print(*ans)
    #This is printed: elements of `ans` (where `ans` is constructed by starting with the elements of `a` in their original order and inserting `cnt` additional elements between each pair, each inserted element being one less than the previous element in `ans`)
#Overall this is what the function does:The function processes an array of integers by first incrementing each element by its 1-based index, then constructs a new list by inserting additional elements between the sorted unique values of the modified array. The inserted elements are one less than the previous element in the new list, and the total number of inserted elements ensures the final list's length equals the original array's length. The function prints the resulting list for each test case.

