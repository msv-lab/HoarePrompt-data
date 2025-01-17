def max_run_uppercase(s):
    max_run = 0
    current_run = 0
    
    for char in s:
        if char.isupper():
            current_run += 1
            if current_run > max_run:
                max_run = current_run
        else:
            current_run = 0
    
    return max_run

# Test cases
assert max_run_uppercase('GeMKSForGERksISBESt') == 5
assert max_run_uppercase('PrECIOusMOVemENTSYT') == 6
assert max_run_uppercase('GooGLEFluTTER') == 4
