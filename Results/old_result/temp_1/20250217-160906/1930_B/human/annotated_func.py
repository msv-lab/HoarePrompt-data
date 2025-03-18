#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5. Additionally, the sum of all n values across all test cases does not exceed 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(range(1, n + 1))
        
        for i in range(n // 2):
            a[2 * i + 1] = n - i
            a[2 * i] = i + 1
        
        if len(a) % 2 == 1:
            a[n - 1] = n // 2 + 1
        
        print(*a)
        
    #State: Output State: The list `a` will be constructed in such a way that for each test case, the first half of the list will contain consecutive integers starting from 1 up to `n//2 + 1`, and the second half will be filled with descending integers starting from `n - i` where `i` ranges from 0 to `n//2 - 1`. If the length of the list is odd, the last element will be set to `n // 2 + 1`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes an integer \( n \) (with \( 3 \leq n \leq 10^5 \)) as input. It constructs a list \( a \) of length \( n \) such that the first half of the list contains consecutive integers starting from 1 up to \( n//2 + 1 \), and the second half contains descending integers starting from \( n - i \) where \( i \) ranges from 0 to \( n//2 - 1 \). If the length of the list is odd, the last element is set to \( n // 2 + 1 \). The function then prints the constructed list for each test case.

