def check_occurences(tuples):
    freq_dict = {}
    for tup in tuples:
        sorted_tup = tuple(sorted(tup))
        if sorted_tup in freq_dict:
            freq_dict[sorted_tup] += 1
        else:
            freq_dict[sorted_tup] = 1
    return freq_dict
