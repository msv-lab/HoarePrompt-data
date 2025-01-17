def find_tuples(tuples_list, k):
    """
    Find tuples which have all elements divisible by k from the given list of tuples.
    
    Args:
        tuples_list (list): A list of tuples.
        k (int): The divisor.
    
    Returns:
        list: A list of tuples where all elements are divisible by k.
    """
    return [tup for tup in tuples_list if all(num % k == 0 for num in tup)]
