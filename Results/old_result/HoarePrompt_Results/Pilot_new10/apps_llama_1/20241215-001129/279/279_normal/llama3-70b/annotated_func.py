#State of the program right berfore the function call: n is a positive integer, p is a permutation of integers from 1 to n, and b is a sequence of zeros and ones of length n.
def func():
    n = int(input())
    p = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] != i + 1:
            ans += 1
        
        if b[i] == 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is the original input integer, `p` is the list of original input integers, `b` is the list of original binary digits, `ans` is the sum of the number of indices where `p[i]` is not equal to `i + 1` and the number of indices where `b[i]` is 0.
    print(ans)
#Overall this is what the function does:The function accepts user input for a positive integer `n`, a permutation `p` of integers from 1 to `n`, and a binary sequence `b` of length `n`, calculates the sum of indices where `p[i]` does not match `i + 1` and where `b[i]` is 0, and prints this sum, without explicit error handling for invalid inputs.

