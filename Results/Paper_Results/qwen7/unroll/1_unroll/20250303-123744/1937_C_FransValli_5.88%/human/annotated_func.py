#State of the program right berfore the function call: None of the input variables are explicitly defined in the provided function signature. However, the problem description indicates that you can interact with a hidden permutation \( p_0, p_1, \ldots, p_{n-1} \), which is a permutation of \(\{0, 1, \ldots, n-1\}\). You can ask up to \(3n\) queries in the form of four indices \(a, b, c, d\) to compare the bitwise OR of pairs of elements in the permutation.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        k = 1
        
        for i in range(2, n):
            print('?', 0, k, 0, i, flush=True)
            res = input()
            if res == '<':
                k = i
        
        best = 0
        
        for i in range(1, n):
            print('?', k, best, k, i, flush=True)
            res = input()
            if res == '<':
                best = i
        
        print('!', k, best, flush=True)
        
    #State: Output State: The variable `k` will hold the maximum value of `i` such that `p_0` OR `p_i` < `p_k` OR `p_i`, and `best` will hold the maximum value of `i` such that `p_k` OR `p_i` < `p_k` OR `p_best`. Finally, the program prints the values of `k` and `best`.
#Overall this is what the function does:The function determines two specific indices `k` and `best` in a hidden permutation \( p_0, p_1, \ldots, p_{n-1} \) by asking up to \(3n\) queries. It identifies `k` as the index where the bitwise OR comparison with other indices results in the smallest value, and `best` as the index where the bitwise OR comparison involving `k` results in the smallest value. Finally, it outputs the values of `k` and `best`.

