def frequency_lists(lists):
    flattened_list = [element for sublist in lists for element in sublist]
    frequency_dict = {}
    for element in flattened_list:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    return frequency_dict
