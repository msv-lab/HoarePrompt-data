#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, x and y are integers such that 1 ≤ x < 10^100 and 1 ≤ y < 10^100, and both x and y consist only of digits from 1 to 9. Additionally, x and y have the same length for each test case.
def func_1():
    a = list(input())
    b = list(input())
    f = 0
    for i in range(len(a)):
        if f == 0:
            if a[i] < b[i]:
                a[i], b[i] = b[i], a[i]
                f = 1
            elif a[i] > b[i]:
                f = 1
        elif a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
        
    #State: `t` remains the same, `x` and `y` remain the same, `a` and `b` are modified based on the swapping rules, and `f` is 1 if any swap occurred or if `a[i] > b[i]` was encountered.
    for i in range(len(a)):
        print(a[i], end='')
        
    #State: t remains the same, x and y remain the same, a remains the same, b remains the same, i is 2, f is 0.
    print()
    #This is printed: (newline)
    for i in range(len(b)):
        print(b[i], end='')
        
    #State: t remains the same, x remains the same, y remains the same, a remains the same, b remains the same, i is 5, f is 0.
    print()
    #This is printed: (an empty line)
#Overall this is what the function does:The function `func_1` reads two integers `x` and `y` of the same length, consisting only of digits from 1 to 9, and prints them after potentially swapping corresponding digits based on specific rules. It ensures that after processing, the first digit of the first number is not less than the first digit of the second number, and for subsequent digits, it swaps them if the digit in the first number is greater than the corresponding digit in the second number. The function prints the modified numbers on two separate lines.

