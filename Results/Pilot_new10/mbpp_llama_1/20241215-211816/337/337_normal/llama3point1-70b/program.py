def find_sum(lst):
    return sum(i for i in lst if lst.count(i) == 1)
