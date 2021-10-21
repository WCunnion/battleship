from Player import Player
from computer_player import ComputerPlayer
from HumanPlayer import HumanPlayer


class Game:
    computer: Player
    human: Player

    def __init__(self, h, c):
        self.human = h
        self.computer = c

    def play(self):
        self.human.createShipGrid()
        self.computer.createShipGrid()
        print("Your boards: ")
        self.human.printGrids()
        while self.human.stillHasShips() and self.computer.stillHasShips():
            print("\n Your turn:")
            self.human.takeTurn(self.computer)
            print("\n Computer's Turn:")
            self.computer.takeTurn(self.human)
            print("\n Current Boards: ")
            self.human.printGrids()
        print("GAME OVER")
        if self.human.stillHasShips():
            print("YOU WIN")
        else:
            print("YOU LOSE")
