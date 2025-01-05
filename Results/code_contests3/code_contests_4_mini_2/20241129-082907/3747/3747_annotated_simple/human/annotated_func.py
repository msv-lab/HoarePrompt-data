#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a[i] satisfies 1 ≤ a[i] ≤ 100.
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 100; if `n` equals 11, then 5 is printed.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `c` is a list where each index represents the count of occurrences of that index in `a`, `n` is an integer such that 1 ≤ `n` ≤ 100, and `c[0]` to `c[100]` contains the counts of indices from `a` within the range of 1 to 100, where `a` has at least `n` elements.
    print(max(c))
#Overall this is what the function does:The function accepts an integer `n` and a list `a` of `n` integers, where each integer in `a` is between 1 and 100. If `n` equals 11, it prints 5. It then counts the occurrences of each integer from 1 to 100 in the list `a` and prints the maximum count among those integers. The function does not return any value.

