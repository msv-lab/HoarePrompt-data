#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 3 ≤ n ≤ 2 \cdot 10^5, and the array a consists of n integers where 0 ≤ a_j ≤ 10^9. The sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 3 ≤ n ≤ 2 \cdot 10^5, and the array a consists of n integers where 0 ≤ a_j ≤ 10^9. After executing the loop, if for every test case, the conditions `b[-1] == 0` and `b[-2] == 0` are met without encountering any negative value in the array before the loop's end, then the output will be 'YES' for that test case; otherwise, it will be 'NO'. The sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( t \) (number of test cases), an integer \( n \) (length of the array), and an array \( a \) of \( n \) integers. It then checks if all elements in the array are non-negative and if certain conditions are met after performing specific arithmetic operations on the array elements. If all conditions are satisfied, it prints 'YES'; otherwise, it prints 'NO'.

