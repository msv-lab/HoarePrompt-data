#State of the program right berfore the function call: n is a positive integer, and the array elements are non-negative integers less than 230.**
def func():
    n = int(raw_input())
    s = raw_input().split()
    a = [0] + [int(s[i]) for i in range(0, n)]
    for i in range(1, n + 1):
        a[i] ^= a[i - 1]
        
    #State of the program after the  for loop has been executed: Output State: `n` is a positive integer, `a` is a list of integers with size `n+1` containing the final values after XOR operations, `i` is equal to `n`
    ans = 0
    for i in range(1, n + 1):
        for j in range(0, i):
            ans = max(ans, a[i] ^ a[j])
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `a` is a list of integers with size `n+1`, `i` is between 1 and n+1, `ans` contains the maximum XOR value calculated between all elements of `a`, `j` is n for the loop to finish
    print(ans)
#Overall this is what the function does:The function reads a positive integer `n` and an array of non-negative integers with values less than 230. It then performs XOR operations on the elements of the array `a` based on the given rules. The function calculates the maximum XOR value between all pairs of elements in the array and prints the result.

