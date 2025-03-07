#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n non-negative integers such that 0 ≤ a_i < n.
def func():
    a = 'abcdefghijklmnopqrstuvwxyz'
    for t in range(int(input())):
        b = [0] * 26
        
        n = int(input())
        
        s = list(map(int, input().split()))
        
        r = ''
        
        for i in s:
            x = b.index(i)
            r += a[x]
            b[x] += 1
        
        print(r)
        
    #State: After the loop executes all iterations, `r` will be a string formed by appending 'a[x]' for each element `i` in `s`, where `x` is the index of the current element `i` in the list `b`. The list `b` will have each of its elements incremented for each occurrence of each unique element in `s`. The variable `t` will be equal to the total number of iterations, `i` will be the last element in the list `s` after all iterations, `n` will remain as the input integer, and `s` will be the list of integers obtained from input but modified during each iteration according to the loop's logic.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a list of `n` non-negative integers `s`. It then maps each integer in `s` to a corresponding character from a predefined string `a` based on the index of the integer in a count list `b`. The function increments the count of each integer in `b` for each occurrence in `s`. Finally, it prints a string composed of these characters. The function does not return any value but modifies and processes the input lists and strings as described.

