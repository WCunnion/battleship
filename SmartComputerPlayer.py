from computer_player import ComputerPlayer
from random import random


class SmartComputerPlayer(ComputerPlayer):

    def __init__(self):
        super.__init__()
        self.lastShot = [0, 0]
        self.activeTarget = False
        self.previousHit = False
        self.directionOfNextShot = 0
        self.firstShipHit = [-1, -1]

    def takeTurn(self, otherPlayer):
        if self.firstShipHit[0] != -1 and self.firstShipHit[1] != -1:
            if not self.previousHit:
                r = self.firstShipHit[0]
                c = self.firstShipHit[1]
                self.directionOfNextShot += 2
                if self.directionOfNextShot >= 4:
                    self.directionOfNextShot -= 4
            else:
                r = self.lastShot[0]
                c = self.lastShot[1]
            if self.lastShot[0] == 0 or self.gridShots.isSpaceWater(r, c - 1):
                cannotMoveUp = True
            if self.lastShot[1] == 0 or self.gridShots.isSpaceWater(r + 1, c):
                cannotMoveLeft = True
            if self.lastShot[0] == 9 or self.gridShots.isSpaceWater(r, c + 1):
                cannotMoveDown = True
            if self.lastShot[1] == 9 or self.gridShots.isSpaceWater(r - 1, c):
                cannotMoveRight = True

            originalDirection = self.directionOfNextShot
            while True:
                if self.directionOfNextShot == 0 and not cannotMoveUp:
                    self.shoot(otherPlayer, r, c - 1)
                    self.lastShot = [r, c - 1]
                    return
                elif self.directionOfNextShot == 1 and not cannotMoveRight:
                    self.shoot(otherPlayer, r + 1, c)
                    self.lastShot = [r+1, c]
                    return
                elif self.directionOfNextShot == 2 and not cannotMoveDown:
                    self.shoot(otherPlayer, r, c + 1)
                    self.lastShot = [r, c+1]
                    return
                elif self.directionOfNextShot == 3 and not cannotMoveLeft:
                    self.shoot(otherPlayer, r - 1, c)
                    self.lastShot = [r-1, c]
                    return
                else:
                    self.directionOfNextShot += 1
                    if self.directionOfNextShot == 4:
                        self.directionOfNextShot = 0
                    if self.directionOfNextShot == originalDirection:
                        self.firstShipHit = [-1, -1]
                        break

            while True:
                r = random.randint(0, 9)
                c = random.randint(0, 9)
                if self.gridShots.isSpaceWater(r, c):  # repeats previous step if it has already shot in that space
                    self.shoot(otherPlayer, r, c)
                    break

    def shoot(self, otherPlayer, r, c): # shoot helper method, determines a miss, hit, or sink
        if otherPlayer.gridShips.isSpaceWater(r, c):  # the shot is a miss
            self.gridShots.changeSingleSpace(r, c, "0")
            otherPlayer.gridShips.changeSingleSpace(r, c, "0")
            print("Miss")
            self.previousHit = False
        else:  # the shot is a hit
            destroyedShip = otherPlayer.gridShips.returnLocation(r, c)  # store ship type for later
            self.gridShots.changeSingleSpace(r, c, "X")
            otherPlayer.gridShips.changeSingleSpace(r, c, "X")
            isDestroyed = True
            for r in range(10):  # traverses 2D grid
                for c in range(10):
                    if otherPlayer.gridShips.returnLocation(r,
                                                            c) is destroyedShip:  # checks each space if any parts of the ship aren't sunk
                        isDestroyed = False
                        break
                if not isDestroyed:
                    break
            if isDestroyed:
                print("You sank the", destroyedShip, "battleship")
                self.firstShipHit = [-1, -1]
            else:
                print("Hit!")
                self.previousHit = True
