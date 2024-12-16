def sequential_search(array, element):
    try:
        index = array.index(element)
        return (True, index)
    except ValueError:
        return (False, -1)
