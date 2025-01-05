#State of the program right berfore the function call: 
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function reads two integers n and m from the user input, then prints a specific pattern based on the values of n and m. It does not return any value.

