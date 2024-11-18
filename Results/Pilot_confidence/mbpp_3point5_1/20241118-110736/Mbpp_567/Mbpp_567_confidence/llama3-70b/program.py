def issort_list(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
