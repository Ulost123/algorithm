def main():
    first_line = input()
    N = int(first_line.strip().split(" ")[0])
    M = int(first_line.strip().split(" ")[1])
    board = [] 
    for i in range(N):
        board_line = input()
        board.append(board_line.strip().split(" "))
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                R_pos = [i, j]

            if board[i][j] == 'O':
                O_pos = [i, j]
    
    print(R_pos, O_pos)
    


if __name__ == "__main__":
    main()

#GG
