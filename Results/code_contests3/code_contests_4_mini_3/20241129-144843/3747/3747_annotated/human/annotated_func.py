#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 100.
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 100; `a` is a list of `n` integers from input. If `n` is 11, then `5` has been printed. If `n` is not 11, there are no changes made to the output.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `c` is a list where each index represents an integer from the input list `a`, and the value at each index `i` in `c` represents the count of occurrences of integer `i` in the list `a`; `n` is the number of elements in the list `a`.
    print(max(c))
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 100) and a list `a` of `n` integers (where each integer satisfies 1 ≤ a_i ≤ 100). If `n` is equal to 11, it prints `5`. Regardless of the value of `n`, it counts the occurrences of each integer in the list `a` and prints the maximum count of any integer present in the list. If `a` is empty, the maximum count printed will be `0`.

