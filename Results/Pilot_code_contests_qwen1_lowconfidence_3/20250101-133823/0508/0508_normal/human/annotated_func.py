#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 12. The input consists of three lines: the first line contains n pairs of integers representing pairs communicated from the first participant to the second, the second line contains m pairs of integers representing pairs communicated from the second participant to the first. All pairs within each set are distinct and contain two different numbers between 1 and 9. It is guaranteed that there is at least one pair from the first set and one pair from the second set that share exactly one number.
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
        
    #State of the program after the  for loop has been executed: `n` must be greater than 0, `i` is the index such that `2 * i` is the last valid index in `p1`, `m` must be a non-negative integer, `a` and `b` are elements from `p1` that satisfied the conditions, `c` and `d` are elements from `p2` that correspond to the current iteration, `kandidat` is the last `kandidat` value added to `cand`, `cc[i]`, and `dd[j]`, `cand` is a set containing all unique `kandidat` values from all iterations, `cc[i]` is a set containing all `kandidat` values from all iterations where `j` is such that `2 * j < m`, and `dd[j]` is a set containing all `kandidat` values from all iterations where `j` is such that `2 * j < m`.
    if (len(cand) == 1) :
        print(cand.pop())
    else :
        if (max(len(cc[i]) for i in range(n)) <= 1 and max(len(dd[i]) for i in range(m
    )) <= 1) :
            print(0)
        else :
            print(-1)
        #State of the program after the if-else block has been executed: *`n` must be greater than 0, `i` is the index such that `2 * i` is the last valid index in `p1`, `m` must be a non-negative integer, `a` and `b` are elements from `p1` that satisfied the conditions, `c` and `d` are elements from `p2` that correspond to the current iteration, `kandidat` is the last `kandidat` value added to `cand`, `cc[i]` is a set containing all `kandidat` values from all iterations where `j` is such that `2 * j < m`, and `dd[j]` is a set containing all `kandidat` values from all iterations where `j` is such that `2 * j < m`. The length of `cand` is not equal to 1. If the maximum length of sets `cc[i]` for all `i` in range `n` is less than or equal to 1 and the maximum length of sets `dd[i]` for all `i` in range `m` is less than or equal to 1, then 0 is printed to the console. Otherwise, -1 is printed to the console.
    #State of the program after the if-else block has been executed: *`n` must be greater than 0, `i` is the index such that `2 * i` is the last valid index in `p1`, `m` must be a non-negative integer, `a` and `b` are elements from `p1` that satisfied the conditions, `c` and `d` are elements from `p2` that correspond to the current iteration, `kandidat` is the last `kandidat` value added to `cand`, `cc[i]` is a set containing all `kandidat` values from all iterations where `j` is such that `2 * j < m`, and `dd[j]` is a set containing all `kandidat` values from all iterations where `j` is such that `2 * j < m`. If the length of `cand` is 1, then `cand` remains an empty set. Otherwise, if the maximum length of sets `cc[i]` for all `i` in range `n` is less than or equal to 1 and the maximum length of sets `dd[i]` for all `i` in range `m` is less than or equal to 1, then 0 is printed to the console. Otherwise, -1 is printed to the console.
#Overall this is what the function does:The function processes two sets of pairs of integers, where each pair from the first set is communicated from the first participant to the second, and each pair from the second set is communicated from the second participant to the first. The function identifies if there is a number that is shared uniquely between these two sets of pairs. Specifically, it checks for a number that appears exactly once in the first set and also exactly once in the second set. If such a number is found, it prints the number. If no such number exists, it further checks if the maximum count of any number in either set is less than or equal to 1. If this condition is met, it prints 0, indicating that no number is shared uniquely. Otherwise, it prints -1, indicating that no unique shared number was found or that the condition failed. The function does not modify the input sets and returns nothing explicitly.

