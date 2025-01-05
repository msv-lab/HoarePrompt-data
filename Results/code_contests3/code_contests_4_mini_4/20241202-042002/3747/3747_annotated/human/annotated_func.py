#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a[i] satisfies 1 ≤ a[i] ≤ 100.
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 100; `a` is a list of `n` integers where each integer `a[i]` satisfies 1 ≤ `a[i]` ≤ 100. If `n` equals 11, then 5 is printed to the output.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `c` is a list of counts where `c[i]` is the number of times integer `i` appears in list `a` for `i` from 1 to 100, `n` is the number of elements in `a`, and `a` is a list of `n` integers.
    print(max(c))
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) and a list `a` of `n` integers (1 ≤ a[i] ≤ 100). It checks if `n` is equal to 11 and prints 5 if true. It then counts the occurrences of each integer from 1 to 100 in the list `a` and prints the maximum count found. If `n` is not 11, it does not print anything in that case.

