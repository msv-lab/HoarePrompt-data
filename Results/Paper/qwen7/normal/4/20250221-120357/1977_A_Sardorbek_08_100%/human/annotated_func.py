#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 100.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        q = b, c
        
        if b == c:
            print('YES')
        elif b < c:
            print('NO')
        elif b % 2 == c % 2:
            print('Yes')
        else:
            print('No')
        
    #State: After the loop executes all its iterations, `a` will be 0, `i` will be equal to the original value of `a` (which was at least 1), and `q` will be a tuple containing the values of `b` and `c` from the last iteration of the loop. The values of `b` and `c` will be the integers provided as input in the last iteration of the loop.
#Overall this is what the function does:The function processes a series of pairs of positive integers (n, m) where 1 ≤ n, m ≤ 100. For each pair, it checks the relationship between n and m and prints 'YES', 'NO', 'Yes', or 'No' based on specific conditions. After processing all pairs, the function ends with no return value.

