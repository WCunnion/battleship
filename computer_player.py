from Player import Player
from Grid import Grid
import random


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()

    def takeTurn(self, otherPlayer):
        while True:
            r = random.randint(0, 9)
            c = random.randint(0, 9)
            if self.gridShots.isSpaceWater(r, c):  # repeats previous step if it has already shot in that space
                if otherPlayer.gridShips.isSpaceWater(r, c):  # the shot is a miss
                    self.gridShots.changeSingleSpace(r, c, "0")
                    otherPlayer.gridShips.changeSingleSpace(r, c, "0")
                    print("Miss")
                else:  # the shot is a hit
                    destroyedShip = otherPlayer.gridShips.returnLocation(r, c)  # store ship type for later
                    self.gridShots.changeSingleSpace(r, c, "X")
                    otherPlayer.gridShips.changeSingleSpace(r, c, "X")
                    isDestroyed = True
                    for r in range(10):  # traverses 2D grid
                        for c in range(10):
                            if otherPlayer.gridShips.returnLocation(r, c) is destroyedShip:  # checks each space if any parts of the ship aren't sunk
                                isDestroyed = False
                                break
                    if isDestroyed:
                        print("You sank the", destroyedShip, "battleship")
                    else:
                        print("Hit!")
                break

    def placeShip(self, ship, size):
        legal = False  # set variables to exist outside of while loop
        r = 0
        c = 0
        vertical = True
        while not legal:  # repeats until legal ship position has been found
            vertical = random.choice([True, False])
            legal = True
            if vertical:  # runs if ship points upward or downward
                r = random.randint(0, 10 - size)
                c = random.randint(0, 9)
                for x in range(size):  # traverses potential ship coordinates
                    if not self.gridShips.isSpaceWater(r + x, c):  # restarts the larger loop if any of the potential
                        # spaces is taken
                        legal = False
                        break
            else:  # runs if ship points left or right
                r = random.randint(0, 9)
                c = random.randint(0, 10 - size)
                for x in range(size):  # traverses potential ship coordinates
                    if not self.gridShips.isSpaceWater(r, c + x):  # restarts the larger loop if any of the potential
                        # spaces is taken
                        legal = False
                        break
        if vertical:
            self.gridShips.changeCol(c, ship, r, size)  # sets the ship on the grid
        else:
            self.gridShips.changeRow(r, ship, c, size)  # sets the ship on the grid

    def stillHasShips(self):
        for r in range(10):  # nested for loops traverse 2D array
            for c in range(10):
                if self.gridShips.returnLocation(r, c) != "X" and self.gridShips.returnLocation(r, c) != "0" and not self.gridShips.isSpaceWater(r, c):
                    return True  # something other than a shot, miss, or water was detected which must be a ship
        return False  # no ships found
