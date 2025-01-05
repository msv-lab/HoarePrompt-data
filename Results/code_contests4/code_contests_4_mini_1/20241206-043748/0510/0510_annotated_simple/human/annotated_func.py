#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 10^5, H is a positive integer such that 1 ≤ H ≤ 10^9, and each a_i and b_i (1 ≤ i ≤ N) are integers satisfying 1 ≤ a_i ≤ b_i ≤ 10^9. The input consists of N pairs of integers representing the damage values for wielding and throwing each katana.
def func():
    N, H = map(int, raw_input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, raw_input().split())
        
        A.append(a)
        
        B.append(b)
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 10^5; `A` is a list containing `N` integers from input; `B` is a list containing `N` integers from input.
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
        
    #State of the program after the loop has been executed: `h` is less than or equal to `H`, `c` is incremented by the number of times elements from `B` were processed; if any element `b` from `B` was less than `am`, then `c` is incremented by `ceil((H - h) * 1.0 / am)`, and `bi` is the index of the last processed element in `B`. If all elements of `B` were processed and `h` reached or exceeded `H`, `c` reflects the total number of `b` values added to `h`.
    print(c)
#Overall this is what the function does:The function accepts two positive integers `N` and `H`, followed by `N` pairs of integers representing the damage values for wielding and throwing katanas. It calculates the number of times the throwing damage can be applied to reach or exceed the health `H`, using the maximum wielding damage when the throwing damages are insufficient. The output is the total number of attacks required to reach at least `H`. If the throwing damages are all less than the maximum wielding damage, the function estimates the additional attacks needed based on the maximum wielding damage.

