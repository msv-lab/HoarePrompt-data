#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5; a is a list of n non-negative integers such that 0 ≤ a_i < n.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = [0] * 26
    for t in range(int(input())):
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4; n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5; a is a list of n non-negative integers such that 0 ≤ a_i < n; b is a list of 26 zeros; r is a string that is constructed based on the input lists s and a according to the given logic inside the loop. For each integer i in list s, the corresponding character from list a at index i is appended to r, and the count of i in list b is incremented.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer \( n \), followed by a list of \( n \) integers \( s \). It then constructs a string \( r \) by mapping each integer in \( s \) to a corresponding character in a predefined string \( a \) (containing lowercase English letters), and updates a count list \( b \) accordingly. Finally, it prints the constructed string \( r \) for each test case.

