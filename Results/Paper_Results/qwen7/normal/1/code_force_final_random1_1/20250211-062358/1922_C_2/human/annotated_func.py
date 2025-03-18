#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 10^5, a is a list of n integers in strictly increasing order (0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9), m is an integer such that 1 ≤ m ≤ 10^5, and x_i and y_i are integers such that 1 ≤ x_i, y_i ≤ n and x_i ≠ y_i.
def func():
    for i in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        d1 = defaultdict(int)
        
        d2 = defaultdict(int)
        
        d1[2] = 1
        
        for i in range(1, n - 1):
            if l[i + 1] - l[i] < l[i] - l[i - 1]:
                d1[i + 2] = 1 + d1[i + 1]
            else:
                d1[i + 2] = l[i + 1] - l[i] + d1[i + 1]
        
        d2[n - 1] = 1
        
        for i in range(n - 2, 0, -1):
            if l[i] - l[i - 1] < l[i + 1] - l[i]:
                d2[i] = 1 + d2[i + 1]
            else:
                d2[i] = l[i] - l[i - 1] + d2[i + 1]
        
        m = int(input())
        
        for j in range(m):
            x, y = map(int, input().split())
            if y > x:
                print(d1[y] - d1[x])
            else:
                print(d2[y] - d2[x])
        
    #State: After all iterations of the loop have finished, `m` will hold the total number of test cases, `j` will be equal to `m-1` (since `j` starts from 0 and increments by 1 in each iteration), and `x` and `y` will be the values of the last pair of integers provided by the user during the last test case. The dictionaries `d1` and `d2` will remain unchanged as they are not modified within the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( n \), a strictly increasing list of \( n \) integers \( a \), an integer \( m \), and two lists \( x \) and \( y \) each containing \( m \) integers. It then calculates and prints the difference in values from the list \( a \) between indices specified by corresponding pairs in lists \( x \) and \( y \). The function does not return any value but outputs the results for each pair.

