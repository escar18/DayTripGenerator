

from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon
from battlefield import Battlefield

def main():
    # Create instances of Robot, Dinosaur, and Weapon
    weapon = Weapon("Sword", 20)
    robot = Robot("Robo1", 100, weapon)
    dinosaur = Dinosaur("Dino1", 150, 30)

    # Create an instance of Battlefield
    battlefield = Battlefield(robot, dinosaur)

    # Run the game
    battlefield.run_game()

if __name__ == '__main__':
    main()