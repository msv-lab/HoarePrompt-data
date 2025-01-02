#State of the program right berfore the function call: n, p, w, and d are integers such that 1 ≤ n ≤ 10^12, 0 ≤ p ≤ 10^17, 1 ≤ d < w ≤ 10^5.
def func():
    [n, p, w, d] = [int(i) for i in sys.stdin.readline().split()]
    x = -1
    y = -1
    z = -1
    done = 0
    for i in range(w):
        if (p - i * d) % w == 0:
            j = (p - i * d) // w
            if i + j <= n:
                x, y, z = j, i, n - j - i
                done = 1
                break
        
    #State of the program after the  for loop has been executed: `n`, `p`, `w`, and `d` are integers read from the input such that 1 ≤ `n` ≤ 10^12, 0 ≤ `p` ≤ 10^17, 1 ≤ `d` < `w` ≤ 10^5. After the loop, if there exists an integer `i` (0 ≤ `i` < `w`) such that `(p - i * d) % w == 0` and `i + (p - i * d) // w ≤ n`, then `x` is set to `(p - i * d) // w`, `y` is set to `i`, `z` is set to `n - (p - i * d) // w - i`, and `done` is set to 1. If no such `i` exists, `x`, `y`, `z` remain -1, and `done` remains 0.
    if (done == 1) :
        print(str(x) + ' ' + str(y) + ' ' + str(z))
    else :
        print(-1)
    #State of the program after the if-else block has been executed: *`n`, `p`, `w`, and `d` are integers read from the input such that 1 ≤ `n` ≤ 10^12, 0 ≤ `p` ≤ 10^17, 1 ≤ `d` < `w` ≤ 10^5. If there exists an integer `i` (0 ≤ `i` < `w`) such that `(p - i * d) % w == 0` and `i + (p - i * d) // w ≤ n`, then `x` is set to `(p - i * d) // w`, `y` is set to `i`, `z` is set to `n - (p - i * d) // w - i`, and `done` is set to 1. Otherwise, `x`, `y`, and `z` remain -1, and `done` remains 0.
#Overall this is what the function does:The function reads four integers `n`, `p`, `w`, and `d` from the standard input, where `1 ≤ n ≤ 10^12`, `0 ≤ p ≤ 10^17`, `1 ≤ d < w ≤ 10^5`. It attempts to find non-negative integers `x`, `y`, and `z` such that `x * w + y * d = p` and `x + y + z = n`. If such integers exist, the function prints `x`, `y`, and `z` separated by spaces. If no such integers exist, the function prints `-1`. After the function executes, the values of `n`, `p`, `w`, and `d` remain unchanged, and the variables `x`, `y`, `z`, and `done` will either reflect the found solution or remain `-1` and `0` respectively if no solution was found.

