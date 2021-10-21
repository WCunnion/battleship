from Game import Game
from HumanPlayer import HumanPlayer
from computer_player import ComputerPlayer


h = HumanPlayer()
c = ComputerPlayer()
game = Game(h, c)
game.play()
