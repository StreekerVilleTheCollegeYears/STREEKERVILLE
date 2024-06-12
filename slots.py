import random

# Define the symbols that will appear on the slot machine
symbols = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar", "Seven"]

# Define the payout for each combination (simple example, usually more complex)
payouts = {
    ("Seven", "Seven", "Seven"): 100,
    ("Bar", "Bar", "Bar"): 50,
    ("Bell", "Bell", "Bell"): 25,
    ("Plum", "Plum", "Plum"): 10,
    ("Orange", "Orange", "Orange"): 5,
    ("Lemon", "Lemon", "Lemon"): 3,
    ("Cherry", "Cherry", "Cherry"): 2,
    ("Cherry", "Cherry"): 1,
    ("Cherry",): 0.5,
}

def spin_reels():
    return [random.choice(symbols) for _ in range(3)]

def calculate_payout(result):
    if tuple(result) in payouts:
        return payouts[tuple(result)]
    elif tuple(result[:2]) in payouts:
        return payouts[tuple(result[:2])]
    elif tuple(result[:1]) in payouts:
        return payouts[tuple(result[:1])]
    return 0

def main():
    balance = 10  # Starting balance for the player
    while balance > 0:
        print(f"Current balance: ${balance}")
        input("Press Enter to spin...")
        
        result = spin_reels()
        print(f"Reels: {result}")
        
        payout = calculate_payout(result)
        balance += payout
        
        print(f"Payout: ${payout}\n")
        
        if balance <= 0:
            print("Game Over! You have no more money left.")
            break
        
        continue_playing = input("Do you want to play again? (yes/no): ").strip().lower()
        if continue_playing != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()