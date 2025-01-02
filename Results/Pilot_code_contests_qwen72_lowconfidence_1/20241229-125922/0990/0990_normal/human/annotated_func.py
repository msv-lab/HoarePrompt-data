#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^5, and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i ≤ 10^9.
def func():
    n = int(raw_input())
    a = [int(x) for x in raw_input().split()]
    """
max_avg = 0
max_len = 0
for i in range(0, n):
    for j in range(i, n):
        tmp = sum(a[i:j+1])/float(j-i+1)
        if tmp > max_avg:
            max_avg = tmp
            max_len = (j-i+1)
        elif tmp == max_avg:
            if (j-i+1) > max_len:
                max_len = (j-i+1)
"""
    max_a = max(a)
    max_len = 0
    tmp = 0
    for i in range(0, n):
        if a[i] != max_a:
            if tmp > max_len:
                max_len = tmp
            tmp = 0
        elif a[i] == max_a:
            tmp += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that \(1 \leq n \leq 10^5\), `a` is a list of integers where each integer \(a_i\) satisfies \(0 \leq a_i \leq 10^9\), `max_avg` is the maximum average of any contiguous subarray in `a`, `max_a` is the maximum value in `a`, `max_len` is the length of the longest contiguous subarray in `a` where all elements are equal to `max_a`, `tmp` is the length of the last contiguous subarray of `max_a` values, or 0 if the last element is not `max_a`, `i` is \(n-1\).
    if (tmp > max_len) :
        max_len = tmp
    #State of the program after the if block has been executed: *`n` is a positive integer such that \(1 \leq n \leq 10^5\), `a` is a list of integers where each integer \(a_i\) satisfies \(0 \leq a_i \leq 10^9\), `max_avg` is the maximum average of any contiguous subarray in `a`, `max_a` is the maximum value in `a`, `i` is \(n-1\). If `tmp` is greater than `max_len`, `max_len` is updated to the value of `tmp`, which is the length of the last contiguous subarray of `max_a` values or 0 if the last element is not `max_a`. Otherwise, `max_len` remains unchanged.
    print(max_len)
#Overall this is what the function does:The function reads two lines of input: the first line is a positive integer `n` (1 ≤ n ≤ 10^5), and the second line is a space-separated list of `n` integers (0 ≤ a_i ≤ 10^9). It then processes this list to find the maximum value in the list (`max_a`) and the length of the longest contiguous subarray where all elements are equal to `max_a`. Finally, it prints the length of this longest contiguous subarray. If the list is empty or contains no elements equal to `max_a`, the function will print 0.

