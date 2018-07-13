## Jacinta Moore
##This is a Connect Four Game where two players take it in turn
## to choose a column number in the aim of getting four in a row on the game board

class ConnectFour:   
    def __init__(self):
        self.cols = 7
        self.rows = 6 
        self.board = [['.' for i in range(self.cols)] for j in range(self.rows)]
   
    def print_b(self):
        print("Column:",'   '.join(map(str,range(self.cols))))
        for i in range(self.rows):
            print(' '*7,'   '.join(str(self.board[i][j])for j in range(self.cols)))

    def move(self, player, colnum):
        col = colnum
        play = player
        if play == 1:
            move = 'X'
        else: move = 'O'
        for i in range(self.rows-1,-1,-1):
           if self.board[i][col] == '.':
                self.board[i][col] = move
                return

    def vert(self):
        for j in range(self.cols):
           for i in range(3):
                if self.board[i][j] != '.' and self.board[i][j]==self.board[i+1][j]and self.board[i][j]==self.board[i+2][j]and self.board[i][j]==self.board[i+3][j]:
                    count = 4
                    return count

    def horz(self):
        for i in range(self.rows):
            for j in range(4):
                if self.board[i][j] != '.' and self.board[i][j]==self.board[i][j+1]and self.board[i][j]==self.board[i][j+2]and self.board[i][j]==self.board[i][j+3]:
                    count2 =4
                    return count2
    
    def diag (self):
        for i in range(3):
            for j in range(4):
                if self.board[i][j] != '.' and self.board[i][j]==self.board[i+1][j+1] and self.board[i][j]== self.board[i+2][j+2] and self.board[i][j]==self.board[i+3][j+3]:
                    counts = 4
                    return counts

    def diagr (self):
        for i in range(self.rows-1,-1,-1):
            for j in range (4):
                if self.board[i][j] != '.' and self.board[i][j]==self.board[i-1][j+1]and self.board[i][j]==self.board[i-2][j+2] and self.board[i][j]==self.board[i-3][j+3]:
                    counter = 4
                    return counter

    def winner_check(self):
        winv = self.vert()
        winh = self.horz()
        wind1 = self.diag()
        wind2 = self.diagr()
        if winv ==4 or winh==4 or wind1==4 or wind2==4:
            return False
        
    def check_col(self,colnum):
       col = colnum
       for i in range(self.rows):
           if self.board[i][col] == '.':
               return False
           else: return True

    def full_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]=='.':
                    return True
            return False
        

def main():
    print ("welcome to Connect Four!")
    print ("Player one is X and Player two is O")
    print ("Are you ready....")
    game = ConnectFour()
    game.print_b()
    win = True
    player = 1
    while win:
        
        print ("Player ", player)
        colnum = int(input("Please enter a column number: ",))
        col_empty = True
        while col_empty:
            col_empty = game.check_col(colnum)
            if col_empty == True:
                colnum = int(input("Sorry column is full please try another column...",)) 
                col_empty = game.check_col(colnum)
           
        game.move(player,colnum)
        game.print_b()
        if (game.winner_check()==False):
            print ("Connect Four !! Player ", player, "has won!!") 
            win = False
        if (game.full_board()== False):
            print ("Game is a draw!!")
            win = False
        if (player == 2): player =0
        player +=1

main()
        
