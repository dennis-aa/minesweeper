class Board:
    ID = 0                            # static variable
    def __init__(self):
        self.grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]
    def update_grid(self,update_grid):
        k=0
        for i in range(9):
            for j in range(9):
                if(not(self.grid[i][j] == -1)):
                    self.grid[i][j]= update_grid[k]
                k += 1


    def get_neighbors(self,i,j):
        neighbors = []
        if(i == 0 and j == 0):
            neighbors.append((i,j + 1))# Right
            neighbors.append((i + 1,j))# Bottom
            neighbors.append((i + 1,j + 1))# Bottom Right
        elif(i == 0 and j == 8):
            neighbors.append((i,j - 1))# Left
            neighbors.append((i + 1,j))# Bottom
            neighbors.append((i + 1,j - 1))#Bottom Left
        elif(i == 8 and j == 0):
            neighbors.append((i - 1,j))# Top
            neighbors.append((i - 1,j + 1))# Top Right
            neighbors.append((i,j + 1))# Right
        elif(i == 8 and j == 8):
            neighbors.append((i - 1,j))# Top
            neighbors.append((i - 1,j - 1))   #Top Left
            neighbors.append((i,j - 1))# Left
        elif(i == 0):
            neighbors.append((i,j - 1))# Left
            neighbors.append((i,j + 1))# Right
            neighbors.append((i + 1,j - 1))#Bottom Left
            neighbors.append((i + 1,j))# Bottom
            neighbors.append((i + 1,j + 1))# Bottom Right
        elif(i == 8):
            neighbors.append((i - 1,j - 1))   #Top Left
            neighbors.append((i - 1,j))# Top
            neighbors.append((i - 1,j + 1))# Top Right
            neighbors.append((i,j - 1))# Left
            neighbors.append((i,j + 1))# Right
        elif(j == 0):
            neighbors.append((i - 1,j))# Top
            neighbors.append((i - 1,j + 1))# Top Right
            neighbors.append((i,j + 1))# Right
            neighbors.append((i + 1,j))# Bottom
            neighbors.append((i + 1,j + 1))# Bottom Right
        elif(j == 8):
            neighbors.append((i - 1,j))# Top
            neighbors.append((i - 1,j - 1))   #Top Left
            neighbors.append((i,j - 1))# Left
            neighbors.append((i + 1,j))# Bottom
            neighbors.append((i + 1,j - 1))#Bottom Left
        else:
            neighbors.append((i - 1,j - 1))  #Top Left
            neighbors.append((i - 1,j))# Top
            neighbors.append((i - 1,j + 1))# Top Right
            neighbors.append((i,j - 1))# Left
            neighbors.append((i,j + 1))# Right
            neighbors.append((i + 1,j - 1))#Bottom Left
            neighbors.append((i + 1,j))# Bottom
            neighbors.append((i + 1,j + 1))# Bottom Right
        return neighbors
    def count_flags(self,i,j):
        neighbors = self.get_neighbors(i,j)
        flags = 0
        for n in neighbors:
            i , j = n
            if self.grid[i][j] == -1:
                flags += 1 
        return flags
    def count_uknown_blocks(self,i,j):
        neighbors = self.get_neighbors(i,j)
        u_blocks = 0
        for n in neighbors:
            i , j = n
            if self.grid[i][j] == 9:
                u_blocks += 1
        return u_blocks
    def print(self):
        for i in range(9):
            print("")
            for j in range(9):
                print(self.grid[i][j], end = " ")


b1 = Board()
b1.print()
flags = b1.get_neighbors(4,4)
print()
print("Top Left Corner: ",b1.get_neighbors(0,0))
print("Top Right Corner: ",b1.get_neighbors(0,8))
print("Middle Left Corner: ",b1.get_neighbors(0,4))
print("Middle Right Corner: ",b1.get_neighbors(8,4))
print("Bottom Left Corner: ",b1.get_neighbors(8,0))
print("Bottom Right Corner: ",b1.get_neighbors(8,8))
print(b1.count_flags(4,4))
print(b1.count_uknown_blocks(4,4))
b1.print()
'''
STEPS FOR SOLUTION
b1 = Board()
1.READ BOARD
    - READ ONES, TWOS, THREES,BLANKS
    - UPDATE INTERNAL BOARD
    b1.update()
2.FLAG KOWN BOMBS
3.CLICK SAFE SQUARES
4.REPEAT 2-3 UNTIL WIN
'''