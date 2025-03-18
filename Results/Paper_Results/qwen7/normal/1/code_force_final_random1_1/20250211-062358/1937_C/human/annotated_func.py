#State of the program right berfore the function call: None of the input variables are explicitly defined in the function signature. However, the problem requires interacting with an external entity to determine the permutation \( p_0, p_1, \ldots, p_{n-1} \) through a series of queries. The interaction involves asking questions in the form of four indices \(a, b, c, d\) and receiving a comparison result based on bitwise OR operations. The goal is to find indices \(i\) and \(j\) such that \(p_i \oplus p_j\) is maximized within 3n queries.
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
        
    #State: Output State: `best` is `n-1`, `i` is `n`, `k` is `n-1`, `res` is an input string, and `n` is the input integer provided by the user.
    #
    #Explanation: After the loop completes all its iterations, the variable `i` starts from `n-1` and decreases by 1 in each iteration until it reaches `1`. Therefore, after `n-1` iterations, `i` will become `1` and then increment to `n` after the loop ends. The variable `best` is updated to the current value of `i` if `res` is `<`, and since `res` is always `<` as per the given states, `best` will be set to `n-1` after `n-2` iterations and will not change further. The variable `k` remains `n-1` as it is not modified within the loop. The value of `res` is the input received during the last iteration of the loop, which could be either `<` or any other string. The value of `n` remains unchanged as it is the input integer provided by the user.
#Overall this is what the function does:The function interacts with an external entity to determine a permutation \( p_0, p_1, \ldots, p_{n-1} \) through a series of up to 3n queries. It finds indices \(i\) and \(j\) such that \(p_i \oplus p_j\) is maximized. After completing the queries, it outputs the indices \(i\) and \(j\) that achieve this maximum XOR value.

