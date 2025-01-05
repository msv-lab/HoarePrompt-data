#State of the program right berfore the function call: n is a positive integer.**
def func():
    n = int(raw_input())
    s = raw_input().split()
    a = [0] + [int(s[i]) for i in range(0, n)]
    for i in range(1, n + 1):
        a[i] ^= a[i - 1]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `s` is a list of strings, `a` is a list of integers with updated values after XOR operations for all elements of the list, `i` is equal to `n`
    ans = 0
    for i in range(1, n + 1):
        for j in range(0, i):
            ans = max(ans, a[i] ^ a[j])
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `s` is a list of strings, `a` is a list of integers with updated XOR values, `i` is `n + 1`, `ans` is the maximum value of XOR operation between `a[n+1]` and all previous elements in the list, `j` is `n + 1`
    print(ans)
#Overall this is what the function does:The function `func` reads a positive integer `n` from the user, reads a list of strings `s`, converts them to integers, performs XOR operations on the elements of the list `a`, and then finds the maximum XOR value between elements of `a`. The function does not accept any parameters and prints the maximum XOR value as output.

