def is_woodall(n):
    def check_woodall(n):
        sum = 0
        for i in range(1, n+1):
            sum += i**i
        return sum == n
    
    return check_woodall(n)
