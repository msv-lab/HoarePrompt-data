#State of the program right berfore the function call: The function `func` is expected to take a binary string `s` as input, where `s` consists only of characters '0' and '1', and its length is within the range 1 ≤ |s| ≤ 500.
def func():
    t = int(input())
    for _ in range(t):
        a = input()
        
        cut = 0
        
        for i in range(len(a) - 1):
            if a[i] == '1' and a[i + 1] == '0':
                cut += 1
        
        print(cut + 1)
        
    #State: `s` is a binary string of length 1 ≤ |s| ≤ 500, `t` is 0 (indicating the loop has completed all iterations), `_` is a placeholder, `a` is the last input string with length greater than 0, `i` is `len(a) - 2`, and `cut` is the number of occurrences where a '1' is immediately followed by a '0' in the string `a`.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads a binary string `a` and calculates the number of times a '1' is immediately followed by a '0' in the string, then prints this count plus one. After processing all test cases, the function completes without returning any value. The final state includes `t` being 0 (indicating all test cases have been processed), and the last processed binary string `a` remains in memory.

