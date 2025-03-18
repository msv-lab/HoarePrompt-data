#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 100.
def func_1():
    n, m = map(int, input().split())
    if (n >= m) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: 'No'
    #State: t is a positive integer such that 1 ≤ t ≤ 100, n and m are integers obtained from the input split by space. If n is greater than or equal to m, the current value of n remains unchanged. If n is less than m, the value of n is updated to m.
#Overall this is what the function does:The function processes a test case consisting of two positive integers \( n \) and \( m \) (where \( 1 \leq n, m \leq 100 \)) and prints either 'Yes' or 'No' based on whether \( n \) is greater than or equal to \( m \). After executing, the function does not return any value but outputs 'Yes' or 'No' to indicate the relationship between \( n \) and \( m \).

