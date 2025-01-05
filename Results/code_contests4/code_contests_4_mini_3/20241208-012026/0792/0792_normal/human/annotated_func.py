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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 3 ≤ `n` ≤ 10^5; `a` is a sorted list of integers with at least 3 elements; `x` is the third element of the list `a`; `ans` is equal to the count of consecutive occurrences of `x` starting from the fourth element of the list `a`.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n` and a list `a` of `n` positive integers. It sorts the list and counts how many times the third smallest element occurs consecutively starting from the fourth element in the sorted list. It then prints this count. If there are fewer than four elements that are equal to the third smallest element, it will return a count of 1 if it exists, or 0 if it does not.

