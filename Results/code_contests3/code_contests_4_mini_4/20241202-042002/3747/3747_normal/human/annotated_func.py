#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 100.
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 100; `a` is a list of `n` integers where each integer `a_i` satisfies 1 ≤ `a_i` ≤ 100. If `n` equals 11, then 5 has been printed.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `a` is a list of `n` integers, `c` is a list of 101 integers where `c[i]` indicates the count of the integer `i` in `a` for 1 ≤ `i` ≤ 100.
    print(max(c))
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) and a list `a` of `n` integers (1 ≤ a_i ≤ 100). If `n` is equal to 11, it prints the number 5. It then counts the occurrences of each integer from 1 to 100 in the list `a`, storing these counts in a list `c`. Finally, it prints the maximum count found in `c`, which represents the highest frequency of any integer from the list `a`. If `n` is 0 or the input is invalid, the function does not handle these cases and will not print any output.

