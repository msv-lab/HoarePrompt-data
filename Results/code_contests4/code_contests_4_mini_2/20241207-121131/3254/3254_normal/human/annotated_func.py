#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2000, and the sequence p consists of n integers where each integer pi satisfies |pi| ≤ 105.
def func():
    N, a, ans = input(), map(lambda x: abs(int(x)), raw_input().split()), 0
    for i in xrange(0, N):
        x, y = 0, 0
        
        for j in xrange(0, N):
            if a[j] < a[i]:
                if j < i:
                    x += 1
                else:
                    y += 1
        
        ans += min(x, y)
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 ≤ `N` ≤ 2000; `ans` is the total sum of `min(x, y)` for each index `i` from 0 to N-1, where `x` is the count of elements in array `a` less than `a[i]` before index `i`, and `y` is the count of elements in array `a` less than `a[i]` from index `i` onwards.
    print(ans)
#Overall this is what the function does:The function accepts an integer `N` (1 ≤ N ≤ 2000) and a sequence of `N` integers, where each integer's absolute value is less than or equal to 100,000. It calculates the total sum of the minimum counts of integers less than each element in the sequence, divided into those that appear before and after the current element, and then prints this total sum.

