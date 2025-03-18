#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, x and y are integers such that 1 <= x < 10^100 and 1 <= y < 10^100, and both x and y consist only of digits from 1 to 9. Additionally, x and y have the same length for each test case.
def func_1():
    a = list(input())
    b = list(input())
    for i in range(len(a)):
        if i <= len(a) // 2 - 1:
            n = min(a[i], b[i])
            m = max(a[i], b[i])
            a[i] = m
            b[i] = n
        else:
            n = min(a[i], b[i])
            m = max(a[i], b[i])
            a[i] = n
            b[i] = m
        
    #State: `a` is a list where the first half contains the maximum values and the second half contains the minimum values from the original `a` and `b` pairs; `b` is a list where the first half contains the minimum values and the second half contains the maximum values from the original `a` and `b` pairs.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: the concatenation of all elements in `a`.
    print()
    #This is printed: (an empty line)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: the concatenation of all elements in `b`.
    print()
    #This is printed: (an empty line)
#Overall this is what the function does:The function `func_1` reads two integers `x` and `y` of the same length, where each digit is between 1 and 9, and rearranges their digits such that the first half of each resulting number consists of the maximum digits from the corresponding positions of `x` and `y`, while the second half consists of the minimum digits. It then prints the two rearranged numbers, each on a new line.

