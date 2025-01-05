#State of the program right berfore the function call: **Precondition**: **N, H, a_i, b_i are integers such that 1 ≤ N ≤ 10^5, 1 ≤ H ≤ 10^9, 1 ≤ a_i ≤ b_i ≤ 10^9.**
def func():
    N, H = map(int, raw_input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, raw_input().split())
        
        A.append(a)
        
        B.append(b)
        
    #State of the program after the  for loop has been executed: Output State: N is greater than 0, H is an integer satisfying 1 ≤ H ≤ 10^9, A contains the values of `a` from all iterations appended, B contains the values of `b` from all iterations appended, `i` is N-1, `a` and `b` are assigned the last integer values obtained from mapping `int` to the input split by whitespace.
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
        
    #State of the program after the loop has been executed: B is a list with -1 appended; h is either 0 or -1; c is the sum of the ceiling value of ((H - h) * 1.0 / am) for all b < am; bi is the index of the last checked element in list B before breaking out of the loop
    print(c)
#Overall this is what the function does:The function `func` reads input integers N and H, then reads N pairs of integers and stores them in lists A and B. It finds the maximum value in list A and sorts list B in descending order. It iterates over list B, calculating the number of times a certain condition is met, and prints the final count. The function does not have a specific return value.

