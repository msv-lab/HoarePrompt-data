import sys

def tuple_size(tup):
    """
    This function calculates the size in bytes of a given tuple.

    Args:
        tup (tuple): The input tuple.

    Returns:
        int: The size of the tuple in bytes.
    """
    return sys.getsizeof(tup)
