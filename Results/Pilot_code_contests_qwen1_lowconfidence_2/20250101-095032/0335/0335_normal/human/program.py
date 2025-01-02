def main():
	n, m = list(map(int, raw_input("").split()))

	matrix = []
	selected_words = ""

	for i in range(n):
		letters = raw_input("")
		row = []
		for letter in letters:
			row.append(letter)
		matrix.append(row)

	for i in range(n):
		for j in range(m):
			if not(word_not_repeated(matrix, i, j)):
				selected_words += matrix[i][j]
	print(selected_words)

def word_not_repeated(matrix, i, j):
	letter = matrix[i][j]
	matrix[i][j] = '_'
	result = letter in matrix[i] or letter in zip(*matrix)[j]
	matrix[i][j] = letter
	return result


if __name__ == '__main__':
	main()
	    		 	  						 	 		 				