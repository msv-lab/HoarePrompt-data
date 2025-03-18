#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a and m < b:
            print(2)
        elif m < a and m > b:
            print(2 + m // b)
        elif m < b and m > a:
            print(2 + m // a)
        else:
            print(m // a + m // b + 2)
        
    #State: The loop has executed `t` times, and for each of the `t` test cases, the values of `a`, `b`, and `m` have been read from the input and processed according to the given conditions. The program has printed the appropriate output for each test case based on the relationship between `m`, `a`, and `b`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `m`. It then calculates and prints a specific integer value based on the relationships between `a`, `b`, and `m` for each test case.

