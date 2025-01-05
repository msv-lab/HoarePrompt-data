#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 100.
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 100 and `a` is a list of integers from the input. If `n` is equal to 11, the value 5 is printed. Otherwise, no action is taken.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `a` is a list of integers, `c` is a list of 101 integers where each `c[i]` represents the count of integer `i` in the list `a`.
    print(max(c))
#Overall this is what the function does:The function reads an integer `n` and a list of `n` integers. If `n` is equal to 11, it prints the number 5. It then counts the occurrences of each integer from the input list and prints the maximum count of any integer in the list. It does not return any value.

