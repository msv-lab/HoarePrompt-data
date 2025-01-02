#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 150000, and a list of n integers a_1, a_2, ..., a_n where each a_i satisfies 1 ≤ a_i ≤ 150000.
def func():
    n = int(raw_input())
    a = list(sorted(map(int, raw_input().split())))
    team = set()
    for boxer in a:
        if boxer - 1 > 0 and boxer - 1 <= 150001 and boxer - 1 not in team:
            team.add(boxer - 1)
        elif boxer > 0 and boxer <= 150001 and boxer not in team:
            team.add(boxer)
        elif boxer + 1 > 0 and boxer + 1 <= 150001 and boxer + 1 not in team:
            team.add(boxer + 1)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that \(1 \leq n \leq 150000\), `a` is a sorted list of `n` integers where each element \(a_i\) satisfies \(1 \leq a_i \leq 150000\), `team` is a set containing unique integers that are either one less than, equal to, or one more than the elements of `a`, provided they satisfy the conditions \(1 \leq x \leq 150001\) and are not already in `team`. If `a` is empty, `team` remains an empty set.
    print(len(team), team)
#Overall this is what the function does:The function reads an integer `n` and a list of `n` integers `a` from the standard input, where `1 ≤ n ≤ 150000` and each `a_i` satisfies `1 ≤ a_i ≤ 150000`. It then creates a set `team` containing unique integers that are either one less than, equal to, or one more than the elements of `a`, provided they satisfy the conditions `1 ≤ x ≤ 150001` and are not already in `team`. After processing, the function prints the size of the `team` set followed by the elements of the set. If the input list `a` is empty, the function prints `0` and an empty set. The function does not return any value.

