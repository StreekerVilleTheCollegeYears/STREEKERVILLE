import random

class Revolver:
    def __init__(self):
        self.chambers = [0] * 6  # Six chambers, initially empty
        self.bullet_position = None

    def load_bullet(self):
        self.bullet_position = random.randint(0, 5)
        self.chambers[self.bullet_position] = 1

    def spin_cylinder(self):
        self.current_position = random.randint(0, 5)

    def pull_trigger(self):
        result = self.chambers[self.current_position]
        self.current_position = (self.current_position + 1) % 6
        return result

def play_russian_roulette():
    revolver = Revolver()
    revolver.load_bullet()
    revolver.spin_cylinder()

    print("Welcome to Russian Roulette!")
    input("Press Enter to pull the trigger...")

    result = revolver.pull_trigger()
    if result == 1:
        print("Bang! You're dead.")
    else:
        print("Click. You survived.")

if __name__ == "__main__":
    play_russian_roulette()