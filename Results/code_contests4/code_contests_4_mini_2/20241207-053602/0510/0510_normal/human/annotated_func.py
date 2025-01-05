#State of the program right berfore the function call: N is a positive integer (1 ≤ N ≤ 10^5), H is a positive integer (1 ≤ H ≤ 10^9), and for each katana i (1 ≤ i ≤ N), a_i and b_i are positive integers such that 1 ≤ a_i ≤ b_i ≤ 10^9.
def func():
    N, H = map(int, raw_input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, raw_input().split())
        
        A.append(a)
        
        B.append(b)
        
    #State of the program after the  for loop has been executed: `N` is a positive integer, `H` is a positive integer, `A` is a list containing `N` input integers, `B` is a list containing `N` input integers, `i` is `N`, `a` is the last input integer, `b` is the last input integer.
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
        
    #State of the program after the loop has been executed: `h` is less than or equal to `H`, `bi` is equal to the number of elements in list `B` that were processed before meeting a condition where `b` is less than `am` or reaching the end of the list, `c` is equal to the total number of times the loop iterated or updated based on the conditions, and `b` is the last integer processed from list `B` before the loop terminated, which could either be greater than or equal to `am` or the last integer in `B` before -1.
    print(c)
#Overall this is what the function does:The function reads a list of katana power values and computes how many times a user can utilize these powers to reach a target value H. It does this by first determining the maximum power from the input list and then iterating through the sorted list of powers, incrementing a count based on the sum of powers used until the target H is reached. If the maximum power is not sufficient to meet the target, it calculates how many additional uses are needed based on the maximum power. The function ultimately returns the total number of uses needed to reach or exceed the target H.

