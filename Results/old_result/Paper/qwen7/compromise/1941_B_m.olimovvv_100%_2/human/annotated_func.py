#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 3 ≤ n ≤ 2 \cdot 10^5, and the array a consists of n integers where 0 ≤ a_j ≤ 10^9; the sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        b = list(map(int, input().split()))
        
        for i in range(0, a - 2):
            if b[i] < 0:
                print('NO')
                break
            b[i + 1] -= b[i] * 2
            b[i + 2] -= b[i]
            b[i] -= b[i]
        else:
            if b[-1] != 0 or b[-2] != 0:
                print('NO')
            else:
                print('YES')
        
    #State: All elements in the list `b` are 0.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer t, followed by an integer n and an array a of n integers. It then iterates through the array a and performs specific operations on its elements. If any element in the array a fails to meet certain conditions during the iteration, it prints 'NO' and breaks out of the loop. If the loop completes without breaking and the last two elements of the array a are both zero, it prints 'YES'. Otherwise, it prints 'NO'. The function ensures that all elements in the list `b` (which is derived from a) become zero by the end of processing each test case.

