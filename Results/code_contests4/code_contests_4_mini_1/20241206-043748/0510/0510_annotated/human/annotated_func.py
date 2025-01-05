#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 10^5, H is a positive integer such that 1 ≤ H ≤ 10^9, and each a_i and b_i are integers such that 1 ≤ a_i ≤ b_i ≤ 10^9 for i = 1 to N.
def func():
    N, H = map(int, raw_input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, raw_input().split())
        
        A.append(a)
        
        B.append(b)
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 ≤ `N` ≤ 10^5; `A` contains `N` values of `a` collected from input; `B` contains `N` values of `b` collected from input; `i` is `N - 1` after the loop executes.
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
        
    #State of the program after the loop has been executed: `h` is less than or equal to `H`, `c` is the total number of elements from `B` that were used, or if `b` is less than `am`, `c` is updated by `int(ceil((H - h) * 1.0 / am))`, and `bi` is the index of the first element in `B` that was not used. If all elements of `B` are used and `h` is still less than `H`, then `bi` is equal to the length of `B` minus 1.
    print(c)
#Overall this is what the function does:The function accepts two integers, N and H, which represent the number of pairs and a threshold, respectively. It then reads N pairs of integers (a_i, b_i) from input, where each a_i and b_i is constrained as specified. The function calculates the maximum value of a_i and sorts the corresponding b_i values in descending order. It iteratively sums the b_i values until the cumulative sum reaches or exceeds H. If a b_i value is found to be less than the maximum a_i, the function calculates how many additional uses of the maximum a_i would be required to reach or exceed H and adds this count to the total. Finally, it prints the total count of operations performed, which could be a combination of using b_i values and additional uses of the maximum a_i. The function does not handle potential input errors or cases where N is 0 or invalid, nor does it return any value but prints the result directly.

