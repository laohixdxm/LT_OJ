#leetcode isValidSodoku

def isValidSodoku(board):
    dist1, dist2 = {}, {}
    
    for i in range(len(board)):
        dist1, dist2 = {}, {}

        for j in range(len(board[i])):
            if(board[i][j]!='.'):
                if(board[i][j] not in dist1):
                    dist1[board[i][j]] = 1
                else:
                    return False
            if(board[j][i]!='.'):
                if(board[j][i] not in dist2):
                    dist2[board[j][i]] = 1
                else:
                    return False
    #return True

    print("***")
    base = []
    for x in range(0, len(board), 3):
        baseX = x
        for y in range(0,len(board), 3):
            baseY = y
            
            base.append([baseX, baseY]) 
            print(base)
    
    dist3 = {}
    for ii in range(len(base)):
        baseX, baseY = base[ii][0], base[ii][1]

        dist3.clear()
        for i in range(2):
            for j in range(2):
                if(board[i+baseX][j+baseY]!='.'):
                    if(board[i+baseX][j+baseY] not in dist3):
                        dist3[board[i+baseX][j+baseY]] = 1
                    else:
                        return False
    return True

board1 = [[5,3,'.'], [6, '.', '.'], ['.', 9, 8]]
print(isValidSodoku(board1))
board2 = [[5,3,'.'], [6, '.', '.'], ['.', 9, 9]]
print(isValidSodoku(board2))

board3 = [  [5,3,'.', '.', 7, '.'],
            [6, '.', '.', 1,9,5], 
            ['.', 9, 8, '.', '.', '.'],
            [8, '.', '.', '.', 6, '.'],
            [4, '.', '.',8, '.', 3],
            [7, '.', '.', '.', 2, '.'],
            
            ]
#print(board3)

print(isValidSodoku(board3))            





