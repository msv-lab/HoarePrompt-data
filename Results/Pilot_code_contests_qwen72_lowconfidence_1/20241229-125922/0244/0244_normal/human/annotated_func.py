#State of the program right berfore the function call: a, b, h, w, and n are integers such that 1 ≤ a, b, h, w, n ≤ 100,000. The list of extensions [a1, a2, ..., an] contains n integers where 2 ≤ ai ≤ 100,000.
def func():
    f = lambda : map(int, raw_input().split())
    a, b, h, w, n = f()
    c = sorted(list(f()), key=lambda x: -x)
    d = {(h, w), (w, h)}
    for (i, q) in enumerate([1] + c):
        for u, v in d.copy():
            h, w = u, v * q
            if a <= w and b <= h or a <= h and b <= w:
                print(i)
                exit()
            d.add((h, w))
            d.add((w, h))
        
    #State of the program after the  for loop has been executed: `a`, `b`, `n` are integers such that 1 ≤ a, b, n ≤ 100,000; the list of extensions `[a1, a2, ..., an]` contains `n` integers where 2 ≤ ai ≤ 100,000; `c` is a list of integers sorted in descending order from the list returned by `f()`. `d` is a set containing all unique tuples `(h, w)` and `(w, h)` generated from the initial tuples and the transformations within the loop. `i` is the number of iterations completed (including the initial value 0), or the value at the point of termination if the loop exits early due to the condition `a <= w and b <= h or a <= h and b <= w`. `q` is the last element in the list `[1] + c` used during the iteration. If the loop terminates early, `i` is printed and the program exits. If the loop completes all iterations without terminating early, `i` is the length of the list `[1] + c`, and `d` contains all possible tuples `(h, w)` and `(w, h)` generated through the loop.
    print(-1)
#Overall this is what the function does:The function `func` reads two lines of space-separated integers from the standard input. The first line consists of five integers `a`, `b`, `h`, `w`, and `n`, where `1 ≤ a, b, h, w, n ≤ 100,000`. The second line consists of `n` integers, each in the range `2 ≤ ai ≤ 100,000`. These integers are sorted in descending order and stored in the list `c`. The function then iterates over the list `[1] + c`, attempting to find a combination of dimensions `(h, w)` such that either `a <= w and b <= h` or `a <= h and b <= w`. If such a combination is found, the function prints the index `i` (number of iterations completed) and exits. If no such combination is found after iterating through all elements in `[1] + c`, the function prints `-1`. The function does not return any value; it only prints the result and exits.

