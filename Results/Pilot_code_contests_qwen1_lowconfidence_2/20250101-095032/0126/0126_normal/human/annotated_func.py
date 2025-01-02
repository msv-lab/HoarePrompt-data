#State of the program right berfore the function call: h and w are positive integers such that 1 <= h <= 300 and 1 <= w <= 300.
def func_1(h, w):
    for i in range(h):
        for j in range(w):
            print('#' if (i + j) % 2 == 0 else '.')
        
        print('')
        
    #State of the program after the  for loop has been executed: `h` is a positive integer such that \(1 \leq h \leq 300\), `w` is a positive integer such that \(1 \leq w \leq 300\), `i` is `h`, `j` is `w`, and the output consists of `h` lines where each line alternates between `#` and `.` based on the parity of `i + j`.
#Overall this is what the function does:The function `func_1` accepts two parameters `h` and `w`, which are positive integers between 1 and 300 inclusive. It prints an `h x w` grid where each cell contains either a `#` or a `.`, depending on the parity of the sum of its row index `i` and column index `j`. Specifically, cells where `i + j` is even contain `#`, and those where `i + j` is odd contain `.`. After the function concludes, the program state includes an output consisting of `h` lines, each containing `w` characters alternating between `#` and `.`, based on the parity of `i + j`. This pattern ensures a checkerboard-like distribution of `#` and `.` characters across the grid.

