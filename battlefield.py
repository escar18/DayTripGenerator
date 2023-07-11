

from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self, robot, dinosaur):
        self.robot = robot
        self.dinosaur = dinosaur
    
    def run_game(self):
        print("The battle begins!")
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            print(f"The robot \"{self.robot.name}\" attacks the dinosaur \"{self.dinosaur.name}\" with the {self.robot.active_weapon.name}!")
            print(f"The dinosaur \"{self.dinosaur.name}\" health: {self.dinosaur.health}")
            if self.dinosaur.health <= 0:
                print(f"The robot \"{self.robot.name}\" defeated the dinosaur \"{self.dinosaur.name}\"!")
                break
            
            self.dinosaur.attack(self.robot)
            print(f"The dinosaur \"{self.dinosaur.name}\" attacks the robot \"{self.robot.name}\"!")
            print(f"The robot \"{self.robot.name}\" health: {self.robot.health}")
            if self.robot.health <= 0:
                print(f"The dinosaur \"{self.dinosaur.name}\" defeated the robot \"{self.robot.name}\"!")
                break
        print("The battle has ended!")