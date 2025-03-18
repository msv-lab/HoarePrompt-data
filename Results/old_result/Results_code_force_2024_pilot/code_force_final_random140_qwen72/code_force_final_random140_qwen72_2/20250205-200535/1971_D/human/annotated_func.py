#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and s is a string of length 1 ≤ |s| ≤ 500 consisting of characters '0' and '1'.
def func():
    t = int(input())
    for _ in range(t):
        a = input()
        
        cut = 0
        
        for i in range(len(a) - 1):
            if a[i] == '1' and a[i + 1] == '0':
                cut += 1
        
        print(cut + 1)
        
    #State: `t` is 0, `a` is the last input string with a length greater than 1, `i` is `len(a) - 2`, and `cut` is the number of occurrences of the substring "10" in the last input string `a`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, followed by `t` strings `s` each consisting of characters '0' and '1'. For each string, it calculates the number of occurrences of the substring "10" and prints this count plus one. After processing all test cases, the function terminates without returning any value. The final state of the program is that `t` is 0, `a` is the last input string processed, `i` is the index of the second-to-last character of `a`, and `cut` is the number of occurrences of "10" in the last input string `a`.

