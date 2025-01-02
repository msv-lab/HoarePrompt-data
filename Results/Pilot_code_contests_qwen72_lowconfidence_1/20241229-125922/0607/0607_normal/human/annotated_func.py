#State of the program right berfore the function call: n and q are positive integers where 1 ≤ n ≤ 1000000 and 1 ≤ q ≤ 100000. Each ai is an integer where 1 ≤ ai ≤ n, and each vi is an integer where -100 ≤ vi ≤ 100, representing the participant number and the number of fish caught or released, respectively.
def func_1(readline):
    n, q = (int(s) for s in readline().split())
    base = [0] * n
    midway = [0] * (n // 100 + 1)
    last = [0] * (n // 10000 + 1)
    for _ in range(q):
        a, v = (int(s) for s in readline().split())
        
        a -= 1
        
        base[a] += v
        
        b = a - a % 100
        
        index = b
        
        value = base[b]
        
        end = b + 100 if b + 100 < n else n
        
        for i in range(b, end):
            if value < base[i]:
                value = base[i]
                index = i
        
        midway[b // 100] = index
        
        c = a - a % 10000
        
        cc = c // 100
        
        index = c
        
        value = base[c]
        
        for i in midway[cc:cc + 100]:
            if value < base[i]:
                value = base[i]
                index = i
        
        last[c // 10000] = index
        
        index = last[0]
        
        value = base[index]
        
        for i in last:
            if value < base[i]:
                value = base[i]
                index = i
        
        print(index + 1, value)
        
    #State of the program after the  for loop has been executed: `n` and `q` are specific positive integers where \(1 \leq n \leq 1000000\) and \(1 \leq q \leq 100000\); `base` is a list of length `n` where each element `base[a]` has been updated by adding `v` for each query `(a, v)`; `midway` is a list of length `n // 100 + 1` where each element `midway[b // 100]` holds the index within the block of 100 elements starting at `b` where the maximum value in `base` is found; `last` is a list of length `n // 10000 + 1` where each element `last[c // 10000]` holds the index within the block of 10000 elements starting at `c` where the maximum value in `base` is found; `value` is the maximum value in `base` across all indices specified in `last`; `index` is the index in `base` where this maximum value is found, and `index + 1` and `value` are printed for each query. If `q` is 0, then `base`, `midway`, and `last` remain unchanged from their initial state, and no values are printed.
    exit()
#Overall this is what the function does:The function `func_1` processes a series of queries where each query consists of a participant number `ai` and a value `vi` representing the number of fish caught or released. The function maintains three lists: `base`, `midway`, and `last`. `base` tracks the cumulative fish count for each participant, `midway` tracks the index of the maximum fish count within blocks of 100 participants, and `last` tracks the index of the maximum fish count within blocks of 10,000 participants. For each query, the function updates the fish count in `base` and then updates the corresponding entries in `midway` and `last` to reflect the new maximum fish counts. After processing each query, the function prints the participant number and the maximum fish count found across all participants. If no queries are provided (`q = 0`), the function does not modify the lists and no output is produced. The function handles the constraints on `n` and `q` effectively, ensuring that the lists are appropriately sized and that the maximum fish counts are accurately tracked and updated.

