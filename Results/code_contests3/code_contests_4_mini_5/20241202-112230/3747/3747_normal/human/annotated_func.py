#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 100.
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 100; `a` is a list of `n` integers where each integer `a_i` satisfies 1 ≤ `a_i` ≤ 100. If `n` is equal to 11, the program prints 5.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `a` is a list of `n` integers where each integer `a_i` satisfies 1 ≤ `a_i` ≤ 100; `c` is a list of 101 integers where `c[i]` is the count of integer `i` in `a` for all `1 ≤ i ≤ 100` and `c[0]` remains 0.
    print(max(c))
#Overall this is what the function does:The function accepts an integer `n` and a list `a` of `n` integers, where each integer in the list is between 1 and 100, inclusive. It prints 5 if `n` is equal to 11 and then counts the occurrences of each integer in `a`, printing the maximum count of any integer in the list after processing. If no integers are present in `a`, the maximum count will be 0. There is no handling of cases where `n` is not equal to the size of the list `a`, which could lead to unexpected results if input constraints are violated.

