#State of the program right berfore the function call: a and b are non-negative integers such that 1 <= a, b <= 10^9.
def func():
    t = int(input())
    for _rep in range(t):
        n, k = list(map(int, input().split()))
        
        if n > k:
            print('Bob')
        elif n < k:
            print('Alice')
        else:
            print('Bob')
        
    #State: rep is 2, _rep is 2, n is an input integer, k is an input integer, the values of n and k are the integers entered by the user separated by space in the third iteration. Regardless of whether n is greater than k or not, the values of rep and _rep remain unchanged.
#Overall this is what the function does:The function reads multiple pairs of integers \(n\) and \(k\) from the user, compares each pair, and prints 'Bob' if \(n > k\), 'Alice' if \(n < k\), and 'Bob' again if \(n = k\). The function does not return any value.

