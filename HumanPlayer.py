from Player import Player

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def createShipGrid(self):
        super().createShipGrid()

    def placeShip(self, ship, size):
        orientation = 0
        colNum = 0
        rowNum = 0
         while orientation != 'v' & orientation != 'h':
            orientation = str(input("Would you like the ship to be vertical (enter v) or horizontal (enter h)"))
            if orientation != 'v' and orientation != 'h':
                print("error, please enter v or h to indicate the orientation of the ship")
        while colNum < 1 or colNum > 10:
            colNum = int(input("Please enter the column you would like the ship to start in"))
            if colNum < 1 or colNum > 10 or (orientation == 'h' and colNum > 10-size):
                print("error, ")
        while rowNum < 1 or rowNum > 10:
            rowNum = int(input("Please enter the row you would like the ship to start in"))
            if rowNum < 1 or rowNum > 10:
                print("error, please enter a value between 1 and 10 for the column")

        self.gridShips.isSpaceWater(rowNum-1, colNum-1)
            if(orientation == 'v'):
                row += 1
            else: # orientation == 'h'
                col += 1


