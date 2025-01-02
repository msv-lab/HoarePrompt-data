#State of the program right berfore the function call: n and m are non-negative integers such that 1 ≤ n, m ≤ 12. The first line contains n pairs of integers representing pairs communicated from the first participant to the second, and the second line contains m pairs of integers representing pairs communicated from the second participant to the first. Each pair consists of two distinct integers between 1 and 9.
def func():
    n, m = map(int, raw_input().split())
    p1 = list(map(int, raw_input().split()))
    p2 = list(map(int, raw_input().split()))
    cand = set()
    cc = [set() for i in range(n)]
    dd = [set() for i in range(m)]
    for i in range(n):
        for j in range(m):
            a, b = p1[2 * i], p1[2 * i + 1]
            c, d = p2[2 * j], p2[2 * j + 1]
            if a not in (c, d) and b not in (c, d):
                continue
            if a in (c, d) and b in (c, d):
                continue
            if a in (c, d):
                kandidat = a
            else:
                kandidat = b
            cand.add(kandidat)
            cc[i].add(kandidat)
            dd[j].add(kandidat)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `m` is a positive integer, `p1` is a list of integers, `p2` is a list of integers, `cand` is a set containing all unique `kandidat` values that meet the specified conditions during all iterations, `cc` is a list of `n` sets where each set contains all unique `kandidat` values for the specific `i` where the loop ends for the last iteration, `dd` is a list of `m` sets where each set contains all unique `kandidat` values for the specific `j` where the loop ends for the last iteration.
    if (len(cand) == 1) :
        print(cand.pop())
    else :
        if (max(len(cc[i]) for i in range(n)) <= 1 and max(len(dd[i]) for i in range(m
    )) <= 1) :
            print(0)
        else :
            print(-1)
        #State of the program after the if-else block has been executed: `n` is a positive integer, `m` is a positive integer, `p1` is a list of integers, `p2` is a list of integers, `cand` is a set containing all unique `kandidat` values that meet the specified conditions during all iterations, `cc` is a list of `n` sets where each set contains all unique `kandidat` values for the specific `i` where the loop ends for the last iteration, `dd` is a list of `m` sets where each set contains all unique `kandidat` values for the specific `j` where the loop ends for the last iteration, and the length of `cand` is not equal to 1, and either the maximum length of any set in `cc` is less than or equal to 1 and the maximum length of any set in `dd` is less than or equal to 1, or at least one of the following is true: `max((len(cc[i]) for i in range(n))) > 1` or `max((len(dd[i]) for i in range(m))) > 1; -1 is printed.
    #State of the program after the if-else block has been executed: *`n` is a positive integer, `m` is a positive integer, `p1` is a list of integers, `p2` is a list of integers, `cand` is a set containing all unique `kandidat` values that meet the specified conditions during all iterations, `cc` is a list of `n` sets where each set contains all unique `kandidat` values for the specific `i` where the loop ends for the last iteration, `dd` is a list of `m` sets where each set contains all unique `kandidat` values for the specific `j` where the loop ends for the last iteration. If `len(cand) == 1`, a value from `cand` is printed. Otherwise, if the length of `cand` is not equal to 1, either the maximum length of any set in `cc` is less than or equal to 1 and the maximum length of any set in `dd` is less than or equal to 1, or at least one of the following is true: `max((len(cc[i]) for i in range(n))) > 1` or `max((len(dd[i]) for i in range(m))) > 1; -1 is printed.
#Overall this is what the function does:The function reads two sets of pairs of integers from the standard input. Each set of pairs represents communications between two participants. For each pair from the first participant, it checks if there is a common element with any pair from the second participant. It then collects these common elements into a set called `cand`. After processing all pairs, the function determines whether there is exactly one common element in `cand`. If there is, it prints this element. Otherwise, it checks if any of the participant's sets (`cc` or `dd`) have more than one common element. If all sets have at most one common element, it prints 0. In all other cases, it prints -1. The function does not accept any explicit parameters but relies on the input provided through `raw_input()`.

