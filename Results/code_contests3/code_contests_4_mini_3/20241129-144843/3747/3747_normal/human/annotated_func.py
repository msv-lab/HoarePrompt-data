#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer is between 1 and 100, inclusive.
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an integer between 1 and 100; `a` is a list of integers derived from user input. If `n` is equal to 11, then 5 is printed to the output. Otherwise, no action is taken.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 100, `a` is a list of integers with `n` elements, `c` is a list where each index represents the count of occurrences of that integer from the list `a`, and `c[i]` is the number of times integer `i` appears in `a` for `i` from 0 to 100.
    print(max(c))
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) and a list `a` of `n` integers (each between 1 and 100, inclusive). If `n` is equal to 11, it prints 5. It then counts the occurrences of each integer from 1 to 100 in the list `a` and prints the maximum count of any integer in that range. If the list `a` contains no integers, the maximum occurrence printed will be 0.

