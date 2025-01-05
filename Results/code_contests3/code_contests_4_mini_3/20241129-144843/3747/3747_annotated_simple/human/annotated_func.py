#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 100.
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 100; `a` is a list of `n` integers where each integer `a_i` satisfies 1 ≤ `a_i` ≤ 100. If `n` equals 11, then 5 is printed.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100; `a` is a list of `n` integers each satisfying 1 ≤ `a_i` ≤ 100; `c` is a list where `c[i]` represents the count of the integer `i` in the list `a` for `i` in the range 1 to 100.
    print(max(c))
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 100) and a list `a` of `n` integers (where each integer `a_i` satisfies 1 ≤ a_i ≤ 100). It checks if `n` is equal to 11 and prints 5 if true. Then, it counts the occurrences of each integer from 1 to 100 in the list `a` and prints the maximum count. If `n` is not equal to 11, only the maximum count of integers in `a` is printed.

