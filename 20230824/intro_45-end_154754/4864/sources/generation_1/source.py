R, C, Z_R, Z_C = map(int, input().split())

article = []
for _ in range(R):
    row = input()
    article.append(row)

for i in range(R):
    enlarged_row = ""
    for j in range(C):
        char = article[i][j]
        enlarged_char = char * Z_C
        enlarged_row += enlarged_char
    for _ in range(Z_R):
        print(enlarged_row)
