#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. Each of the following t lines contains two integers n and k (2 ≤ n ≤ 10^8, 1 ≤ k ≤ 4n - 2) — the size of the square grid and the minimum number of diagonals that should have at least one colored cell.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        print((k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k ==
            4 * n - 2))
        
    #State: The output state consists of t lines, each representing the result of the computation for the corresponding test case. Each line contains an integer value determined by the given formula based on the values of n and k from the input. Specifically, for each test case, the output is calculated as follows:
    #- If k is less than 4n - 3, the output is (k // 2 + k % 2).
    #- If k is equal to 4n - 2, the output is 1 added to the previous result.
    #- If k is equal to or greater than 4n - 3, the output is 2 * n.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of two integers `n` and `k`. It calculates and outputs an integer value for each test case based on the given conditions: if `k` is less than `4n - 3`, it outputs `(k // 2 + k % 2)`, if `k` is equal to `4n - 2`, it outputs `1` more than the previous result, and if `k` is equal to or greater than `4n - 3`, it outputs `2 * n`.

