#!/usr/bin/python2.7
#
# Jacob Adams
import sys


def main():
	row1 = raw_input()
	row2 = raw_input()
	row3 = raw_input()
	row4 = raw_input()

	board = [[0 for row in range(4)] for col in range(4)]

	createBoard(board, row1, 0)
	createBoard(board, row2, 1)
	createBoard(board, row3, 2)
	createBoard(board, row4, 3)

	if(checkHoriz(board)):
		print("yay")
	else:
		print("no")
	#print(input)
	#print(sys.argv[1])
	#print("hello World")

def createBoard(board, input, row):
	count = 0
	for char in input:
		board[row][count] = char 
		++count
	return board

def checkHoriz(board):
	for i in range(0,3):
		oCount = 0
		temp = 0
		for k in range(0,3):
			if(board[i][k] == 'o'):
				++oCount
			elif(board[i][k] == '.'):
				if(temp):
					oCount = 0
				else:
					temp = 1
					++oCount

			elif(board[i][k] == 'x'):
				oCount = 0;

		if(oCount > 2):
			return 1
	return 0

main()