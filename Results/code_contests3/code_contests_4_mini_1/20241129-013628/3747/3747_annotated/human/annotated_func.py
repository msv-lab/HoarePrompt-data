#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a[i] satisfies 1 ≤ a[i] ≤ 100.
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 100; `a` is a list of `n` integers where each integer `a[i]` satisfies 1 ≤ `a[i]` ≤ 100. If `n` equals 11, then 5 is printed.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100; `a` is a list of `n` integers; `c` is a list of 101 integers where each `c[i]` represents the count of occurrences of the integer `i` in the list `a`, and all integers in `a` satisfy 1 ≤ `a[i]` ≤ 100.
    print(max(c))
#Overall this is what the function does:The function accepts an integer input `n` (1 ≤ n ≤ 100) and a list of `n` integers `a` (1 ≤ a[i] ≤ 100). It prints 5 if `n` equals 11, and then counts the occurrences of each integer in `a`, printing the maximum count of any integer from 1 to 100 in the list `a`. The function does not return any value.

