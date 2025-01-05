#State of the program right berfore the function call: n is a positive integer.**
def func():
    n = int(raw_input())
    s = raw_input().split()
    a = [0] + [int(s[i]) for i in range(0, n)]
    for i in range(1, n + 1):
        a[i] ^= a[i - 1]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `s` is a list of strings with at least one element, `a` is a list of integers obtained by converting elements of `s` to integers and adding 0 at the beginning, `i` is `n`, element at index `i` in list `a` is updated by performing a bitwise XOR operation with the element at index `i-1`.
    ans = 0
    for i in range(1, n + 1):
        for j in range(0, i):
            ans = max(ans, a[i] ^ a[j])
        
    #State of the program after the  for loop has been executed: `ans` is the maximum value of XOR operations between all pairs of elements in list `a` after all the iterations of the loop have finished, `n` is the total number of iterations of the outer loop, `i` is equal to `n`, `j` is equal to `i-1`, for the loop to execute another time `i` should be less than the length of list `a`
    print(ans)
#Overall this is what the function does:The function reads an integer `n` from the user input, then reads a list of strings `s` and converts them to integers, storing them in list `a`. It performs XOR operations on adjacent elements in list `a`. Finally, it calculates the maximum XOR value between all pairs of elements in list `a` and prints the result. The function does not accept any parameters and returns the maximum XOR value calculated.

