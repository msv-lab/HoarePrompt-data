#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 10^5. Additionally, there are two lists A and B of length N, where each A_i and B_i are integers such that 0 ≤ A_i ≤ 10^9 and 1 ≤ B_i ≤ 10^9.
def func():
    n = int(raw_input())
    ab = [map(int, raw_input().split()) for _ in xrange(n)]
    cnt = 0
    for i in xrange(n - 1, -1, -1):
        a, b = ab[i][0], ab[i][1]
        
        if (a + cnt) % b == 0:
            continue
        
        cnt += b - (a + cnt) % b
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 10^5\), `i` is \(-1\), `ab` is a list of `n` tuples, each tuple containing two integers, `cnt` is the final updated value after all iterations, `a` is the first element of the tuple at index `i` (which is out of bounds, so it doesn't matter), `b` is the second element of the same tuple (also out of bounds).
    print(cnt)
#Overall this is what the function does:The function takes two lists `A` and `B` of length `N` (where `1 ≤ N ≤ 10^5`), with elements `A_i` ranging from `0` to `10^9` and `B_i` ranging from `1` to `10^9`. It calculates the minimum number of increments needed to ensure that for every pair `(a, b)` in the lists, `(a + cnt) % b == 0`, where `cnt` starts at `0`. The function iterates through the lists in reverse order, updating `cnt` when necessary. After the loop, the function prints the final value of `cnt`.

