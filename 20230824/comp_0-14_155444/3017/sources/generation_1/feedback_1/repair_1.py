def count_numbers(n, e):
    count = 0
    power_digits = str(2 ** e)
    power_length = len(power_digits)
    
    for num in range(n + 1):
        num_digits = str(num)
        num_length = len(num_digits)
        
        if num_length < power_length:
            continue
        
        for i in range(num_length - power_length + 1):
            if num_digits[i:i + power_length] == power_digits:
                count += 1
                break
    
    return count


n, e = map(int, input().split())
result = count_numbers(n, e)
print(result)