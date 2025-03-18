#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers such that 1 ≤ n, k ≤ 10^18.
def func_1():
    n, k = map(int, input().split())
    if (n < k) :
        print('NO')
        #This is printed: 'NO'
    else :
        if (n == k) :
            print('YES')
            #This is printed: YES
            print(1)
            #This is printed: 1
            print(n)
            #This is printed: n
        else :
            if (k - 1 < n - k + 1) :
                print('YES')
                #This is printed: YES
                print(2)
                #This is printed: 2
                print(n - k + 1, 1)
                #This is printed: n - k + 1 1
            else :
                print('NO')
                #This is printed: 'NO'
            #State: t is an integer such that 1 ≤ t ≤ 1000, n and k are positive integers such that 1 ≤ n, k ≤ 10^18, n is the first integer input split from input, k is the second integer input split from input, and n is greater than k. If k - 1 < n - k + 1 holds true, no changes are made to n and k. Otherwise, no changes are made to n and k.
        #State: t is an integer such that 1 ≤ t ≤ 1000, n and k are positive integers such that 1 ≤ n, k ≤ 10^18. If n equals k, no changes are made to n and k. Otherwise, if k - 1 < n - k + 1 holds true, no changes are made to n and k. If none of these conditions apply, n and k remain unchanged.
    #State: t is an integer such that 1 ≤ t ≤ 1000, n and k are positive integers such that 1 ≤ n, k ≤ 10^18. If n is less than k, n remains unchanged and k remains unchanged. If n equals k, n and k remain unchanged. If n is greater than k and k - 1 < n - k + 1 does not hold, n and k remain unchanged. Otherwise, n and k remain unchanged.
#Overall this is what the function does:The function processes test cases where it takes two integers \( n \) and \( k \) as inputs. It checks if \( n \) is less than, equal to, or greater than \( k \). Depending on the comparison, it prints either "YES" or "NO" along with some integers. After processing, \( n \) and \( k \) remain unchanged.

