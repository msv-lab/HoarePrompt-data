from sys import stdin, stdout

def get_maximized_matrix(n):
    sum = 0
    
    permutation = [i for i in range(1, n+1)]
    
    permutation_sum = 0
    
    for val in permutation:
        permutation_sum += val
        
    moves = []
    
    for i in range(n):
        current_move = []
        current_move.append(1)
        current_move.append(i+1)
        current_move.extend(permutation)
        moves.append(current_move)
        
        sum += permutation_sum
    
    current_column_value = 1
    
    while permutation_sum > n*current_column_value:
        current_move = []
        current_move.append(2)
        current_move.append(current_column_value)
        current_move.extend(permutation)
        moves.append(current_move)
        
        sum += (permutation_sum - (n*current_column_value))
        
        current_column_value += 1
        
    return sum, moves 

def main():
    # input text
    t = list(map(int, stdin.readline().split()))[0]
    
    maximized_sums = []
    maximized_matrix_moves = []
    
    for _  in range(t):
        n = list(map(int, stdin.readline().split()))[0]
        current_max_sum, current_moves = get_maximized_matrix(n)
        
        maximized_sums.append(current_max_sum)
        maximized_matrix_moves.append(current_moves)
        
    for index in range(len(maximized_sums)):
        stdout.writelines(str(maximized_sums[index]) + ' ' + str(len(maximized_matrix_moves[index])) + '\n')
        for move_items in maximized_matrix_moves[index]:
            for item in move_items:
                stdout.writelines(str(item) + ' ')
            stdout.writelines('\n')

if __name__ == "__main__":
    main()