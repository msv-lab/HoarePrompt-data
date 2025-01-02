#State of the program right berfore the function call: h and w are positive integers such that 1 <= h <= 300 and 1 <= w <= 300.
def func_1(h, w):
    for i in range(h):
        for j in range(w):
            print('#' if (i + j) % 2 == 0 else '.')
        
        print('')
        
    #State of the program after the  for loop has been executed: `h` is a positive integer such that \(1 \leq h \leq 300\), `w` is a positive integer such that \(1 \leq w \leq 300\), `i` is `h-1`, `j` is `w-1`, and the printed output consists of a pattern of `#` and `.` where each row alternates between even and odd sums of indices `(i + j)` modulo 2, with an empty line after each row.
#Overall this is what the function does:The function `func_1` accepts two parameters `h` and `w`, which are positive integers between 1 and 300 inclusive. It prints a pattern consisting of `#` and `.` characters to the console. Each row contains `w` characters, alternating between `#` and `.` based on the sum of the row index `i` and column index `j` being even or odd. After executing the function, the console will display `h` rows of this pattern, with an empty line separating each row. The function does not return any value.

