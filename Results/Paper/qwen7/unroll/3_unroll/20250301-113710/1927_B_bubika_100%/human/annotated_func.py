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
        
    #State: t is a positive integer such that 1 ≤ t ≤ 10^4, n is a positive integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a remains as the list ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']; b is a list of 26 zeros; r is an empty string.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a list of `n` non-negative integers `s`. It then maps each integer in `s` to a corresponding character in the alphabet (starting from 'a') based on the count of occurrences of each integer in `s`. Finally, it prints a string composed of these characters.

