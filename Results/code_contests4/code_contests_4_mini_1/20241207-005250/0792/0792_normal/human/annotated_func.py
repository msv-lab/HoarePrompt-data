#State of the program right berfore the function call: n is a positive integer such that 3 ≤ n ≤ 10^5, and a is a list of n positive integers where each element ai satisfies 1 ≤ ai ≤ 10^9.
def func():
    n = int(raw_input())
    a = map(int, raw_input().split())
    a = sorted(a)
    x = a[2]
    ans = 1
    for i in xrange(3, len(a)):
        if a[i] == x:
            ans += 1
        else:
            break
        
    #State of the program after the  for loop has been executed: `n` is at least 4, `i` is at least 3, `x` is equal to `a[2]`, and `ans` is the count of consecutive elements in `a` starting from index 2 that are equal to `x`.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n` (where 3 ≤ n ≤ 100,000) and a list `a` of `n` positive integers (where each element satisfies 1 ≤ ai ≤ 1,000,000,000). It sorts the list `a` and counts the number of consecutive occurrences of the third smallest element (i.e., the element at index 2 after sorting) starting from that index. The function prints this count. If there are fewer than four elements in the input list, the behavior is not defined as it assumes `n` is at least 4.

