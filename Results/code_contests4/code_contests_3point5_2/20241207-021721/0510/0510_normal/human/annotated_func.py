#State of the program right berfore the function call: N is a positive integer, H is a positive integer, a_i and b_i are positive integers such that 1 ≤ a_i ≤ b_i ≤ 10^9 for 1 ≤ i ≤ N.**
def func():
    N, H = map(int, raw_input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, raw_input().split())
        
        A.append(a)
        
        B.append(b)
        
    #State of the program after the  for loop has been executed: N is a positive integer, H is a positive integer, a_i and b_i are positive integers such that 1 ≤ a_i ≤ b_i ≤ 10^9 for 1 ≤ i ≤ N, A is a list with N elements containing the values of `a` for each iteration of the loop, B is a list with N elements containing the values of `b` for each iteration of the loop
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
        
    #State of the program after the loop has been executed: H, N, a_i, b_i, A, B, am, h, c, bi are positive integers. A contains N elements, B contains N+1 elements. am is the maximum value in list A. B is reversed. h is equal to or greater than H. c is the total number of iterations executed. bi is the index of the last element of B
    print(c)
#Overall this is what the function does:The function `func` reads input values N and H, then reads N pairs of integers into lists A and B. It calculates the maximum value in A and sorts B in descending order. It iterates through the elements of B, adding them to variable h until h is greater than or equal to H. It keeps track of the number of iterations in c and prints the final value of c. The function does not accept any parameters and operates based on the provided constraints.

