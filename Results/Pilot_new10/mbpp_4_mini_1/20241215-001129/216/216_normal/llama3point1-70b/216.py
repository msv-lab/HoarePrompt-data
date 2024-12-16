def check_Consecutive(lst):
    lst.sort()
    return all(lst[i] - lst[i-1] == 1 for i in range(1, len(lst))) and len(lst) == len(set(lst))
