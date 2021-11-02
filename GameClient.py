from Game import Game
from HumanPlayer import HumanPlayer
from computer_player import ComputerPlayer
from SmartComputerPlayer import SmartComputerPlayer


s = SmartComputerPlayer()
c = ComputerPlayer()
game = Game(s, c)
game.play()
