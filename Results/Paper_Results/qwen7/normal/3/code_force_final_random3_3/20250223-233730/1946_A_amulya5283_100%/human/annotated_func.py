#State of the program right berfore the function call: t is a positive integer, and for each test case, n is a positive integer such that 1 ≤ n ≤ 10^5 and the array a contains n integers where each integer is in the range 1 ≤ a_i ≤ 10^9. Additionally, the sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    t = int(input())
    while t > 0:
        t -= 1
        
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        if n == 1:
            print(1)
        else:
            res = 0
            mdx = n // 2 + n % 2 - 1
            for i in range(mdx, n):
                if a[mdx] == a[i]:
                    res += 1
            print(res)
        
    #State: t is equal to 0, n is an input integer, a is a sorted list of integers, and res is the count of consecutive occurrences of the middle element (a[mdx]) from the middle index towards the end of the list a. mdx is calculated as n // 2 + n % 2 - 1, and i is the last index value that was checked in the loop.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it reads a positive integer \( n \) and a list of \( n \) integers \( a \). It then sorts the list \( a \) and calculates the count of consecutive occurrences of the middle element (if \( n \) is odd) or the second middle element (if \( n \) is even) from the middle index towards the end of the list. Finally, it prints the count for each test case.

