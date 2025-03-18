#State of the program right berfore the function call: The function takes no arguments but operates on multiple test cases provided via standard input. Each test case consists of two integers a and b (1 ≤ a, b ≤ 10^9) representing the dimensions of Bob's rectangle. The number of test cases, t, satisfies 1 ≤ t ≤ 10^4.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            if a % 2 == 0:
                a1, a2 = a // 2, a // 2
                if a1 != b:
                    print('Yes')
                    continue
            if b % 2 == 0:
                b1, b2 = b // 2, b // 2
                if b1 != a:
                    print('Yes')
                    continue
            print('No')
        else:
            print('No')
        
    #State: All test cases processed with no remaining iterations.
#Overall this is what the function does:The function processes multiple test cases from standard input, where each test case consists of two integers representing the dimensions of a rectangle. It checks if either dimension is even and whether the rectangle can be split into two non-equal parts by halving one of the even dimensions. If such a split is possible, it prints "Yes"; otherwise, it prints "No".

