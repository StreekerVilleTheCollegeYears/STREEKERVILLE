import random

class Pinata:
    def __init__(self, durability):
        self.durability = durability

    def hit(self, force):
        if self.durability > 0:
            self.durability -= force
            if self.durability < 0:
                self.durability = 0
            return True
        return False

    def is_broken(self):
        return self.durability == 0

class Player:
    def __init__(self, name):
        self.name = name

    def hit_pinata(self, pinata):
        force = random.randint(1, 10)  # Random force between 1 and 10
        successful_hit = pinata.hit(force)
        if successful_hit:
            print(f"{self.name} hits the piñata with force {force}. Piñata durability is now {pinata.durability}.")
        else:
            print(f"The piñata is already broken!")

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)

    initial_durability = random.randint(20, 50)  # Random initial durability between 20 and 50
    pinata = Pinata(initial_durability)

    print(f"{player.name}, you have a piñata with {pinata.durability} durability. Start hitting it to get a reward!")

    while not pinata.is_broken():
        input("Press Enter to hit the piñata...")
        player.hit_pinata(pinata)

    rewards = ["Candy", "Toy", "Sticker", "Chocolate", "Balloon"]
    reward = random.choice(rewards)
    print(f"Congratulations, {player.name}! You broke the piñata and got a {reward}!")

if __name__ == "__main__":
    main()