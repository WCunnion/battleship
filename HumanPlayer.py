from Player import Player

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def takeTurn(self, otherPlayer):
        while True: # runs until break statement
            rowNum = 0
            colNum = 0
            while colNum < 1 or colNum > 10: # chooses column to attack
                colNum = int(input("Please enter the column you would like to attack"))
                if colNum < 1 or colNum > 10: # makes sure colNum is in bounds
                    print("error, please enter a value between 1 and 10 for the column")
            while rowNum < 1 or rowNum > 10: # chooses row to attack
                rowNum = int(input("Please enter the row you would like to attack"))
                if rowNum < 1 or rowNum > 10: # makes sure rowNum is in bounds
                    print("error, please enter a value between 1 and 10 for the row")
            rowNum = rowNum - 1
            colNum = colNum - 1
            if not self.gridShips.isSpaceWater(rowNum, colNum): # makes sure the player does not shoot the same space twice
                print("Error, you have already shot that space")
                continue
            if self.gridShots.isSpaceWater(rowNum, colNum): # current space has not yet been shot
                if otherPlayer.gridShips.isSpaceWater(rowNum, colNum): # space being shot is water
                    self.gridShots.changeSingleSpace(rowNum, colNum, "0")
                    otherPlayer.gridShips.changeSingleSpace(rowNum, colNum, "0")
                    print("Miss")
                else: # space being shot has a ship
                    destroyedShip = otherPlayer.gridShips.returnLocation(rowNum, colNum)
                    self.gridShots.changeSingleSpace(rowNum, colNum, "X")
                    otherPlayer.gridShips.changeSingleSpace(rowNum, colNum, "X")
                    isDestroyed = True
                    for r in range(10):  # traverses 2D grid
                        for c in range(10):
                            if otherPlayer.gridShips.returnLocation(r, c) is destroyedShip:  # checks each space if any parts of the ship aren't sunk
                                isDestroyed = False
                                break
                        if not isDestroyed:
                            break
                    if isDestroyed: # ship was hit and sank
                        print("You sank the", destroyedShip, "battleship")
                    else: # ship was hit but not sank
                        print("Hit!")
                break

    def placeShip(self, ship, size):
        orientation = "word"
        rowNum = 0
        colNum = 0
        while True: # runs infinite loop, only broken once a valid spot has been chosen to place the ship
            while orientation != 'v' and orientation != 'h': # loop only broken once a proper input for orientation has been entered
                orientation = str(input("Would you like the ship to be vertical (enter v) or horizontal (enter h)"))
                if orientation != 'v' and orientation != 'h': # orientation value is not valid, loop runs again
                    print("error, please enter v or h to indicate the orientation of the ship")
            if orientation == 'h': # ship is horizontal
                while rowNum < 1 or rowNum > 10: # loop only broken once rowNum is between 1 and 10, inclusive
                    rowNum = int(input("Please enter the row you would like the ship to start in"))
                    if rowNum < 1 or rowNum > 10: # rowNum is out of bounds, loop runs again
                        print("error, please enter a value between 1 and 10 for the row")
                while colNum < 1 or colNum > 10-size: # loop only broken once colNum is between 1 and 10-size, inclusive
                    colNum = int(input("Please enter the column you would like the ship to start in"))
                    if colNum < 1 or colNum > 10-size: # colNum is out of bounds, loop runs again
                        print("error, please enter a value between 1 and", 10-size, "for the column")
            if orientation == 'v': # ship is vertical
                while colNum < 1 or colNum > 10: # loop only broken once colNum is between 1 and 10, inclusive
                    colNum = int(input("Please enter the column you would like the ship to start in"))
                    if colNum < 1 or colNum > 10: # colNum is out of bounds, loop runs again
                        print("error, please enter a value between 1 and 10 for the column")
                while rowNum < 1 or rowNum > 10-size: # loop only broken once rowNum is  between 1 and 10-size, inclusive
                    rowNum = int(input("Please enter the row you would like the ship to start in"))
                    if rowNum < 1 or rowNum > 10-size: # rowNum out of bounds, loop runs again
                        print("error, please enter a value between 1 and", 10-size, "for the row")
            r = rowNum - 1
            c = colNum - 1
            if orientation == 'v': # ship is vertical
                for i in range(size): # checks the rest of the spaces based on the orientation and starting point of the ship
                    if not self.gridShips.isSpaceWater(r, c): # one of the spaces is occupied by another ship
                        print("Error, ship cannot be placed there")
                        continue
                    r += 1
                self.gridShips.changeRow(self, c, ship, rowNum-1, size)
            if orientation == 'h': # ship is horizontal
                for i in range(size): # checks the rest of the spaces based on the orientation and starting point of the ship
                    if not self.gridShips.isSpaceWater(r, c): # one of the spaces is occupied by another ship
                        print("Error, ship cannot ne placed there")
                        continue
                    c += 1
                self.gridShips.changeCol(self, r, ship, colNum-1, size)
            break

    def stillHasShips(self):
        for r in range(10): # nested for loops traverse 2D array
            for c in range(10):
                if self.gridShips.returnLocation(r, c) is not "X" and self.gridShips.returnLocation(r,c) is not "0" and not self.gridShips.isSpaceWater(r, c):
                    return True # if statement returns True if the returnLocation method gives a ship (not an X, 0, or ~)
        return False # a ship was not detected on the map, so there are no ships left





