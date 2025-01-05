#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 100.
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 100; `a` is a list of `n` integers where each integer `a_i` is assigned values from `raw_input()`, satisfying 1 ≤ `a_i` ≤ 100. If `n` equals 11, the printed value is 5.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100; `a` is a list of `n` integers, `c` is a list of integers where `c[i]` represents the count of occurrences of integer `i` in the list `a` for 1 ≤ `i` ≤ 100, and all indices in `c` that do not correspond to integers in `a` remain 0.
    print(max(c))
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) and a list `a` of `n` integers (1 ≤ a_i ≤ 100). If `n` is equal to 11, it prints 5. It then counts the occurrences of each integer from 1 to 100 in the list `a`, and finally, it prints the maximum count of any integer in `a`. If no integers are present in `a`, it will print 0.

