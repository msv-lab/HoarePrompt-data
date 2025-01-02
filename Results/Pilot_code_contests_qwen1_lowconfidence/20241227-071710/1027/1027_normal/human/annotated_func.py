#State of the program right berfore the function call: N and M are integers such that 2≤N,M≤50, and a_i and b_i are integers such that 1≤a_i,b_i≤N and a_i ≠ b_i for all 1≤i≤M.
def func():
    n, m = map(int, raw_input().split())
    count = [0] * n
    for i in xrange(m):
        a, b = map(int, raw_input().split())
        
        count[a - 1] += 1
        
        count[b - 1] += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 50, `m` is an integer between 2 and 50, `count` is a list of `n` integers where each element is the count of how many times the corresponding index (plus one) was selected as either `a` or `b` in the input pairs, `i` is `m-1`, `a` is the last `a` input by the user, `b` is the last `b` input by the user.
    for i in xrange(n):
        print(count[i])
        
    #State of the program after the  for loop has been executed: `total` is unspecified, `n` is an integer between 2 and 50, `m` is an integer between 2 and 50, `count` is a list of `n` integers where each element is the count of how many times the corresponding index (plus one) was selected as either `a` or `b` in the input pairs, `i` is `n-1`, `a` is the last `a` input by the user, `b` is the last `b` input by the user, and `count[i]` is printed.
#Overall this is what the function does:The function reads two integers \( N \) and \( M \) from user input, where \( 2 \leq N, M \leq 50 \). It then processes \( M \) pairs of integers \( (a, b) \) such that \( 1 \leq a, b \leq N \) and \( a \neq b \) for each pair. For each pair, it increments the count of both \( a \) and \( b \) by 1. After processing all pairs, it prints the count of how many times each index (from 0 to \( N-1 \)) was selected as either \( a \) or \( b \). The function does not return any value.

