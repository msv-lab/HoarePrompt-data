def count_Primes_nums(n: int) -> int:
    """
    Returns the number of prime numbers less than the given non-negative number.
    
    Parameters:
    n (int): A non-negative integer.
    
    Returns:
    int: The number of prime numbers less than n.
    """
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime.
        
        Parameters:
        num (int): The number to check.
        
        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count
