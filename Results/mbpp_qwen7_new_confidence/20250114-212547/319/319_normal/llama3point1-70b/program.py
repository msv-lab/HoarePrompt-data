def extract_index_list(l1, l2, l3):
    result = []
    for i in range(min(len(l1), len(l2), len(l3))):
        if l1[i] == l2[i] == l3[i]:
            result.append(l1[i])
    return result
