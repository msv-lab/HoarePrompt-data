n, t = map(int, input().split())
books = list(map(int, input().split()))

total_books = 0
total_time = 0
max_books = 0

for i in range(n):
    total_time += books[i]
    
    if total_time <= t:
        total_books += 1
        max_books = total_books
    
    else:
        total_time -= books[i-max_books]
        
print(max_books)