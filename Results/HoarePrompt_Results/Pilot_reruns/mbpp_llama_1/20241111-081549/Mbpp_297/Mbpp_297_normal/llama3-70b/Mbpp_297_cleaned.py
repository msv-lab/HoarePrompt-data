def func_1(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(func_1(element))
        else:
            flat_list.append(element)
    return flat_list