#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 100.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        q = b, c
        
        if b == c:
            print('YES')
        elif b < c:
            print('NO')
        elif a % 2 == b % 2:
            print('Yes')
        else:
            print('No')
        
    #State: The output state will consist of 'YES', 'NO', 'Yes', or 'No' printed for each iteration of the loop based on the conditions given. The specific values of 'b' and 'c' entered during each iteration will determine which output is printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( b \) and \( c \). For each test case, it prints 'YES' if \( b \) equals \( c \), 'NO' if \( b \) is less than \( c \), 'Yes' if both \( b \) and \( a \) have the same parity (both even or both odd), and 'No' otherwise. The function reads the number of test cases \( t \) first, then iterates through each test case to perform these checks and print the corresponding result.

