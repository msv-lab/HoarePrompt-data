#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are positive integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and y = 0. The input also includes a list of x distinct integers from 1 to n, representing the vertices Bessie has chosen, and the sum of x over all test cases does not exceed 2⋅10^5.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: t equals 0, n is an integer, x is an integer; arr is a list of integers where each element is the integer conversion of the corresponding element in the input string split by spaces, and t is no longer greater than 0.
    #State: t is a positive integer such that 1 ≤ t ≤ 10^4. After the execution of the if else block, if t equals 0, n and x are integers, and arr is a list of integers where each element is the integer conversion of the corresponding element in the input string split by spaces. Otherwise, t is still a positive integer such that 1 ≤ t ≤ 10^4, and no changes are made to n, x, or arr.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads values of \( n \), \( x \), and \( y \) (with \( y \) always being 0), and a list of \( x \) distinct integers from 1 to \( n \). It then prints the value \( x - 2 \) for each test case. After processing all test cases, it ensures that the variable \( t \) is set to 0, indicating the end of all test cases.

