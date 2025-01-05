#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 100000, H is a positive integer such that 1 ≤ H ≤ 1000000000, and for each i (1 ≤ i ≤ N), a_i and b_i are integers such that 1 ≤ a_i ≤ b_i ≤ 1000000000.
def func():
    N, H = map(int, raw_input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, raw_input().split())
        
        A.append(a)
        
        B.append(b)
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 100000; `A` is a list containing `N` integers; `B` is a list containing `N` integers.
    am = max(A)
    B.sort()
    B.reverse()
    B.append(-1)
    h = 0
    c = 0
    bi = 0
    while h < H:
        b = B[bi]
        
        if b < am:
            c += int(ceil((H - h) * 1.0 / am))
            break
        else:
            h += b
            c += 1
            bi += 1
        
    #State of the program after the loop has been executed: `h` is greater than or equal to `H`, `c` is the number of times the loop executed plus the integer value from the last calculation if `b` was less than `am`, `bi` is the index of the first element in list `B` that was not processed, and `b` is either the last processed value from list `B` or -1 if the loop exited due to `h` reaching or exceeding `H`.
    print(c)
#Overall this is what the function does:The function accepts no parameters but reads input values for `N` (the number of pairs) and `H` (a target integer). It then reads `N` pairs of integers `(a_i, b_i)` and computes how many times it can add values from the list `B` (sorted in descending order) to reach or exceed the value `H`. If the maximum value of `A` is greater than the largest value in `B`, the function calculates how many additional times it would need to add the maximum value of `A` to exceed `H`. The function ultimately prints the total count of additions required. It handles situations where `H` could be reached either by using values from `B` or by calculating based on the maximum value from `A`.

