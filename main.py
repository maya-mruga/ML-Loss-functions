from sudoku_connections import SudokuConnections
import copy

class SudokuBoard : 
    def __init__(self) : 
        self.board = self.getBoard()
        self.sudokuGraph = SudokuConnections()
        self.mappedGrid = self.__getMappedMatrix() 

    def __getMappedMatrix(self) : 
        # Maps all the ids to the position in the matrix
        mappedGrid = copy.deepcopy(self.board)
        id = 1
        for i in range(len(self.board)) : 
            for j in range(len(self.board[0])):
                mappedGrid[i][j] = id
                id += 1
        return mappedGrid

    def getBoard(self) : 

        board = [
            [0,0,0,2,6,0,7,0,1],
            [6,8,0,0,7,0,0,9,0],
            [1,9,0,0,0,4,5,0,0],
            [8,2,0,1,0,0,0,4,0],
            [0,0,4,6,0,2,9,0,0],
            [0,5,0,0,0,3,0,2,8],
            [0,0,9,3,0,0,0,7,4],
            [0,4,0,0,5,0,0,3,6],
            [7,0,3,0,1,8,0,0,0]
        ]
        return board

    def printBoard(self) : 
        
        print("    1 2 3     4 5 6     7 8 9")
        for i in range(len(self.board)) : 
            if i%3 == 0  :#and i != 0:
                print("  - - - - - - - - - - - - - - ")

            for j in range(len(self.board[i])) : 
                if j %3 == 0 :#and j != 0 : 
                    print(" |  ", end = "")
                if j == 8 :
                    print(self.board[i][j]," | ", i+1)
                else : 
                    print(f"{ self.board[i][j] } ", end="")
        print("  - - - - - - - - - - - - - - ")

    def is_Blank(self) : 
        # check if the location is blank. Note that blank here means "0"

        ## your code here:
        pass
        

    def graphColoringInitializeColor(self):
        """
        Through def graphColoringInitializeColor(self) we are assigning the colors to index (id) which are given by the puzzle.
        fill the already given colors
        """
        color = [0] * (self.sudokuGraph.graph.totalV+1)
        given = [] # list of all the ids whose value is already given. Thus cannot be changed

        ## your code here:

        # loop through rows
        # loop through columns
        # conditon
        # first get the idx of the position       
        # update the color
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] != 0:
                    idx = self.mappedGrid[row][col]
                    color[idx] = self.board[row][col]
                    given.append(idx)
        return color, given
        

    def __isSafe2Color(self, v, color, c) : 

        """
        v: vertices 
        color: the list of colors
        c: color
        """
        ## your code here:
        # safe to color if none of the neighbors have the same color
        # return True/False
        for i in range(1, self.sudokuGraph.graph.totalV+1):
            if v!=i:
                if self.sudokuGraph.graph.isNeighbour(v,i):
                    if color[i]==c:
                        return False
        return True


    def solveGraphColoring(self, m, color, given, v) : 
        """
        Use the functions above as per your convenience and complete this function.
        After running this file, The answer to the sudoku will be printed.
        m = grid
        """
        ## your code here:
        # Graph coloring wih backtracking
        if v == self.sudokuGraph.graph.totalV+1:
            return True
        
        for c in range(1, m+1):
            if self.__isSafe2Color(v, color, c):
                if v not in given:
                  color[v] = c
                if self.solveGraphColoring(m, color, given, v+1) == True:
                  return True
                if v not in given : 
                  color[v] = 0
            
        return False
        # return color (optional)
        
    
def main() : 
    s = SudokuBoard()
    v = 1
    m = 9
    print("BEFORE SOLVING ...")
    print("\n\n")
    s.printBoard()
    print("\nSolving ...")
    print("\n\n\nAFTER SOLVING ...")
    print("\n\n")
    color, given = s.graphColoringInitializeColor()
    s.solveGraphColoring(m, color, given, v)
    color.remove(0)
    print(color)
    c = 0
    for i in range(m):
      for j in range(m):
        s.board[i][j] = color[c]
        c += 1 
    s.printBoard()

if __name__ == "__main__" : 
    main()
