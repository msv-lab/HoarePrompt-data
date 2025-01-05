#State of the program right berfore the function call: N, H, a_i, and b_i are integers such that 1 ≤ N ≤ 10^5, 1 ≤ H ≤ 10^9, 1 ≤ a_i ≤ b_i ≤ 10^9, and a_i ≤ H for all i.**
def func():
    N, H = map(int, raw_input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, raw_input().split())
        
        A.append(a)
        
        B.append(b)
        
    #State of the program after the  for loop has been executed: `N` is greater than 0, `a` contains the last integer input, `b` contains the last integer input, `A` contains all the integers entered in order, `B` contains the sum of all the integers entered
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
        
    #State of the program after the loop has been executed: N is greater than 0, a contains the last integer input, b contains the value of B at index bi, A contains all the integers entered in order, B contains the reversed list of all integers entered with -1 appended at the end, am contains the maximum value from the list A, h is either increased by the value of b or set to 0, c is the result of the calculation c += int(ceil((H - h) * 1.0 / am)), bi is the index of the last element accessed in B after the loop finishes executing
    print(c)
#Overall this is what the function does:The function `func` reads integer inputs for `N` and `H`, then reads pairs of integers `a` and `b` into lists `A` and `B` respectively. It calculates the maximum possible sum of integers from the ranges [a_i, b_i] where 1 ≤ i ≤ N, ensuring that the sum does not exceed the integer H. The function prints the maximum possible sum calculated and considers edge cases such as when the sum exceeds H or when B is empty.

