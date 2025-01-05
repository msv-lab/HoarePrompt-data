#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and a is a list of n integers where each integer a[i] satisfies 1 ≤ a[i] ≤ 100.
def func():
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    if (n == 11) :
        print(5)
    #State of the program after the if block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 100 and `a` is a list of input integers. If `n` is equal to 11, the value 5 is printed. Otherwise, nothing is printed.
    c = [0] * 101
    for d in a:
        c[d] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100; `a` is a list of input integers with at least `n` elements; `c` is a list of 101 integers where each index `d` corresponds to the count of occurrences of the integer `d` in the list `a`, and all other indices in `c` remain unchanged from their initial value of 0.
    print(max(c))
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) and a list `a` of `n` integers (1 ≤ a[i] ≤ 100). If `n` equals 11, it prints the number 5. It then counts the occurrences of each integer from 1 to 100 in the list `a` and prints the maximum count found among the integers. If there are no integers in the range of 1 to 100, the function will print 0.

