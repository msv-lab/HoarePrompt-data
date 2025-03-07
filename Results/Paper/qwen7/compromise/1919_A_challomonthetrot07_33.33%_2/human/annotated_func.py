#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    T = int(input())
    for i in range(T):
        a, b = map(int, input().split())
        
        if a == b:
            print('Bob')
        elif a == 1:
            print('Alice')
        elif b == 1:
            print('Bob')
        elif a % 2 == 1:
            print('Bob')
        elif a % 2 == 0 and b % 2 == 1:
            print('Alice')
        elif a > b:
            print('Bob')
        else:
            print('Alice')
        
    #State: Output State: The output will consist of T lines, each line containing either 'Alice' or 'Bob'. The specific output on each line depends on the values of `a` and `b` provided by the user for each iteration of the loop. If `a` equals `b`, it prints 'Bob'. If `a` is 1, it prints 'Alice'. If `b` is 1, it prints 'Bob'. If `a` is odd, it prints 'Bob'. If `a` is even and `b` is odd, it prints 'Alice'. If `a` is greater than `b`, it prints 'Bob', otherwise it prints 'Alice'.
#Overall this is what the function does:The function processes up to 1000 test cases, each consisting of two positive integers \(a\) and \(b\). Based on the values of \(a\) and \(b\), it outputs either 'Alice' or 'Bob' for each test case. Specifically, if \(a\) equals \(b\), it outputs 'Bob'. If \(a\) is 1, it outputs 'Alice'. If \(b\) is 1, it outputs 'Bob'. If \(a\) is odd, it outputs 'Bob'. If \(a\) is even and \(b\) is odd, it outputs 'Alice'. If \(a\) is greater than \(b\), it outputs 'Bob', otherwise it outputs 'Alice'.

