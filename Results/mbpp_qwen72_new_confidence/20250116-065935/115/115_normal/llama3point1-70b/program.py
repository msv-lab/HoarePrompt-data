def insert_element(lst, elem):
    result = []
    for item in lst:
        result.append(elem)
        result.append(item)
    return result
