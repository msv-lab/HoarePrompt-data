#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x is a positive integer such that 1 ≤ x ≤ 10^8 and n is a positive integer such that 1 ≤ n ≤ x.
def func():
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        k = x // n
        
        if k == 1:
            print(1)
            continue
        
        ans = 1
        
        for i in range(1 + (1 if x % 2 == 0 else 0), int(x ** 0.5) + 1, 2):
            if x % i == 0:
                l = [ans]
                if i <= k:
                    l.append(i)
                if x // i <= k:
                    l.append(x // i)
                ans = max(l)
        
        print(ans)
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x is a positive integer such that 1 ≤ x ≤ 10^8, n is a positive integer such that 1 ≤ n ≤ x, and ans is the maximum value among 1, i, and x//i where i is an odd number from 1+(x%2==0) to the largest odd number less than or equal to the square root of x, provided that both i and x//i are less than or equal to k (x//n).
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers \( x \) and \( n \). For each test case, it calculates the maximum value among 1, \( i \), and \( x \) divided by \( i \), where \( i \) ranges from 1 (if \( x \) is even) to the largest odd number less than or equal to the square root of \( x \), provided that both \( i \) and \( x \) divided by \( i \) are less than or equal to \( k \) (where \( k \) is \( x \) divided by \( n \)). It prints the result for each test case.

