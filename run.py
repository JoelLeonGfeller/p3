import random

# Define the deck of cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']

# Initialize player and dealer hands
playerHand = []
dealerHand = []

# Function to deal a card
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# Function to calculate the total value of a hand
def total(turn):
    total_value = 0
    aces = 0  # To keep track of the number of Aces in the hand
    for card in turn:
        if card in range(2, 11):
            total_value += card
        elif card in ['J', 'Q', 'K']:
            total_value += 10
        elif card == 'A':
            aces += 1
            total_value += 11
    # Handle Aces to avoid busting
    while total_value > 21 and aces:
        total_value -= 10
        aces -= 1
    return total_value

# Function to reveal the dealer's hand
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0], 'X'
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]

# Initial dealing of cards
for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

# Game loop
while True:
    print(f"Dealer has {revealDealerHand()}")
    print(f"You have {playerHand} for a total of {total(playerHand)}")

    if total(playerHand) >= 21:
        break

    choice = input("1: Stay\n2: Hit\n")
    
    if choice == '1':
        break
    elif choice == '2':
        dealCard(playerHand)
    else:
        print("Invalid input. Please select 1 or 2.")

# Dealer's turn
while total(dealerHand) < 17:
    dealCard(dealerHand)

# Determine the winner
player_total = total(playerHand)
dealer_total = total(dealerHand)

print(f"\nYou have {playerHand} for a total of {player_total}")
print(f"Dealer has {dealerHand} for a total of {dealer_total}")

if player_total > 21:
    print("You bust! Dealer Wins!")
elif dealer_total > 21:
    print("Dealer busts! You Win!")
elif dealer_total == player_total:
    print("It's a tie!")
elif dealer_total > player_total:
    print("Dealer Wins!")
else:
    print("You Win!")





