#State of the program right berfore the function call: **Precondition**: 
- n is an integer such that 1 ≤ n ≤ 2·10^5.
- The sequences p1, p2, ..., pn and b1, b2, ..., bn consist of integers.
- For the sequence p: 1 ≤ pi ≤ n for all 1 ≤ i ≤ n.
- For the sequence b: bi is either 0 or 1 for all 1 ≤ i ≤ n.
def func():
    n = int(raw_input())
    p = [(int(v) - 1) for v in raw_input().split()]
    b = map(int, raw_input().split())
    comps = [(0) for i in xrange(n)]
    col = 0
    for i in xrange(n):
        if comps[i] == 0:
            col += 1
            comps[i] = col
            j = i
            while comps[p[j]] == 0:
                j = p[j]
                comps[j] = col
        
    #State of the program after the  for loop has been executed: `n` is an integer satisfying 1 ≤ n ≤ 2*10^5, `comps` is a list of `n` elements where each element corresponds to the value of `col`, `col` is the total number of unique colors used, `i` is n-1, `j` is the index of the last element in `comps` list that was updated. All elements in the `comps` list have been updated with the value of `col` after all iterations of the loop have finished.
    print(0 if col == 1 else col) + (1 if sum(b) == 0 else 0)
#Overall this is what the function does:The function `func` reads input values and processes them to assign colors to elements based on certain conditions. It then prints the total number of unique colors used if it's greater than 1, otherwise, it prints 0. The function does not return any specific value.

