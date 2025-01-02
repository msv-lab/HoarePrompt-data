def func_1(line):
    """Read example from stdin and parse it into the appropriate data structure
    
    Use in the following way:
    
    example = example_generator(stdin_generator)
    while True:
        numbers, target = next(example)
        .
        .
        .
    
    """
    while True:
        n = int(next(line).strip())
        P = [int(p_i) - 1 for p_i in next(line).split()]
        yield (n, P)

def func_2(n, p):
    """Print out the number of times Vasya needs to use portals to get to room n+1
    
    dp[i] is the number of portal jumps required to start off at room i with an odd
    number of crosses and get back to room i with an even number of crosses.
    
    Hence the recurrence relation is as follows:
    
    dp[i] = 1 + [Sum_{j = p(i)}^{i-1} dp[j] + 1]
    
    This can be read as "the number of portal jumps to get from room i with an odd
    number of crosses to an even number of crosses is equivalent to taking a portal
    jump to room p(i) into an odd number of crosees (+1), getting back into that
    state with an even number of crosses (Sum part).
    
    """
    dp = [0] * n
    for i in range(n):
        portal_jumps = 1
        for j in range(p[i], i):
            portal_jumps += dp[j] % (1000000000.0 + 7)
            portal_jumps += 1 % (1000000000.0 + 7)
        dp[i] = int(portal_jumps % (1000000000.0 + 7))
    total_pjumps = 0
    for i in range(n):
        total_pjumps += dp[i] % (1000000000.0 + 7)
        total_pjumps += 1 % (1000000000.0 + 7)
    print(total_pjumps)
example = func_1(sys.stdin)
if __name__ == '__main__':
    (n, P) = next(example)
    func_2(n, P)