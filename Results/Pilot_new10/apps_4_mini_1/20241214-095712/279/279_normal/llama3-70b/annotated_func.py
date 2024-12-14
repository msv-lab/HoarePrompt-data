#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 200000), p is a list of integers representing a permutation of numbers from 1 to n, and b is a list of integers consisting of zeros and ones with the same length as p.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `p` is a list of integers representing a new permutation from the input, `b` is a list of integers consisting of zeros and ones based on user input, `ans` is equal to the count of indices where either `p[i]` is not equal to `i + 1` or `b[i]` is equal to 0.
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `n`, a permutation list `p`, and a binary list `b`, counts the elements where the permutation deviates from its original order or where elements in `b` are zeros, and prints this count as the output.

