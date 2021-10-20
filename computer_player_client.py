from computer_player import ComputerPlayer

cpu = ComputerPlayer()
cpu.createShipGrid()
print("cpu: \n")
cpu.printGrids()

cpu2 = ComputerPlayer()
cpu2.createShipGrid()
print("\n cpu2: \n")
cpu2.printGrids()

while cpu2.stillHasShips() and cpu.stillHasShips():
    cpu2.takeTurn(cpu)
    cpu.takeTurn(cpu2)
print("\n game over")
print("cpu: \n")
cpu.printGrids()
print("\n cpu2 \n")
cpu2.printGrids()