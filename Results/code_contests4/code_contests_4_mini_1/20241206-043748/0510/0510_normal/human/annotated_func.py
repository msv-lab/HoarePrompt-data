#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 10^5, H is a positive integer such that 1 ≤ H ≤ 10^9, and for each katana, a_i and b_i are integers such that 1 ≤ a_i ≤ b_i ≤ 10^9 for all i where 1 ≤ i ≤ N.
def func():
    N, H = map(int, raw_input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, raw_input().split())
        
        A.append(a)
        
        B.append(b)
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 10^5; `A` is a list containing `N` integers from the input; `B` is a list containing `N` integers from the input.
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
        
    #State of the program after the loop has been executed: `N` is a positive integer such that 1 ≤ `N` ≤ 10^5; `A` is a list containing `N` integers; `B` is a reversed sorted list containing `N + 1` integers with the last element being -1; `am` is the maximum value from the list `A`; `h` is less than or equal to `H`; `c` is the count of how many elements from `B` were processed until `h` reached or exceeded `H`, or until a value in `B` less than `am` was found; `bi` is the index in `B` where the processing stopped, which could be equal to `N` if all elements were processed without encountering a value less than `am` before reaching `H`.
    print(c)
#Overall this is what the function does:The function accepts two positive integers, `N` and `H`, representing the number of katanas and a health threshold, respectively. It reads `N` pairs of integers, `a_i` and `b_i`, which represent the minimum and maximum damage values of each katana. The function calculates how many katanas from the maximum damage values can be used until the total damage reaches or exceeds `H`. If the maximum damage value of the katanas is less than the highest minimum damage value, the function estimates the number of additional hits needed based on the highest minimum damage value. Ultimately, it returns the total number of hits required, which could include additional hits if the maximum damage katanas are insufficient to reach `H`.

