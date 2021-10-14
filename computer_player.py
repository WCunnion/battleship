from Player import Player
from Grid import Grid
import random


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()

    def takeTurn(self, otherPlayer):
        while True:
            r = random.randint(0, 10)
            c = random.randint(0, 10)
            if self.gridShots.isSpaceWater(r, c):
                if otherPlayer.gridShips.isSpaceWater(r, c):
                    self.gridShots.changeSingleSpace(r, c, "0")
                    otherPlayer.gridShips.changeSingleSpace(r, c, "0")
                else:
                    destroyedShip = otherPlayer.gridShips.returnLocation(r, c).clone()
                    self.gridShots.changeSingleSpace(r, c, "X")
                    otherPlayer.gridShips.changeSingleSpace(r, c, "X")
                    isDestroyed = True
                    for x in otherPlayer.gridShips:
                        if destroyedShip in x:
                            isDestroyed = False
                            pass
                    if isDestroyed:
                        print("Ship", destroyedShip, "has been destroyed")

    def placeShip(self, ship, size):
        legal = False
        r = 0
        c = 0
        vertical = True
        while not legal:
            vertical = random.choice([True, False])
            legal = True
            if vertical:
                r = random.randint(0, 10 - size)
                c = random.randint(0, 10)
                for x in range(size):
                    if not self.gridShips.isSpaceWater(r + x, c):
                        legal = False
                        pass
            else:
                r = random.randint(0, 10)
                c = random.randint(0, 10 - size)
                for x in range(size):
                    if not self.gridShips.isSpaceWater(r, c + x):
                        legal = False
                        pass
        if vertical:
            self.gridShips.changeCol(c, ship, r, size)
        else:
            self.gridShips.changeRow(r, ship, c, size)
