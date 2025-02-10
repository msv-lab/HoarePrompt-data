#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, s is a binary string with a length between 1 and 500, inclusive.
def func():
    t = int(input())
    for _ in range(t):
        a = input()
        
        cut = 0
        
        for i in range(len(a) - 1):
            if a[i] == '1' and a[i + 1] == '0':
                cut += 1
        
        print(cut + 1)
        
    #State: After the loop executes all its iterations, `i` is `-1`, `cut` holds the total count of occurrences where an element is '1' followed by an element '0' in the string `a`, and `_` is `t` (the number of times the outer loop ran).
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) and a binary string \( s \). For each test case, it counts the number of occurrences where a '1' is immediately followed by a '0' in the string \( s \), then prints the count incremented by one for each test case.

