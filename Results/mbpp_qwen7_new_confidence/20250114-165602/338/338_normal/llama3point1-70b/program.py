def pack_consecutive_duplicates(lst):
    result = []
    current_group = [lst[0]]
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            current_group.append(lst[i])
        else:
            result.append(current_group)
            current_group = [lst[i]]
            
    result.append(current_group)
    return result
