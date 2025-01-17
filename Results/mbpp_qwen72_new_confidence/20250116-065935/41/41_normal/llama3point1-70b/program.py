def freq_count(lst):
    return {i: lst.count(i) for i in set(lst)}
