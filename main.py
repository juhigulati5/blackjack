import random
from art import logo 
from replit import clear

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  new_card = random.choice(cards)
  return new_card

def score(list):
  """Totals the card values for the user and the dealer."""
  calculate_score = sum(list)
  if calculate_score > 21 and 11 in list:
    list.remove(11)
    list.append(1)
    new_score = sum(list)
    return new_score
  return calculate_score

def compare(user_score, comp_score):
  """Compares the final scores of the user and the dealer."""
  if comp_score > 21 and user_score > 21:
    return "You went over. You lose :("
  elif comp_score > 21:
    return "Dealer went over. You win :D"
  elif user_score > 21:
    return "You're over 21! You lose :("
  elif comp_score == 21:
    return "The computer has blackjack! You lose :("
  elif user_score == 21 and comp_score != 21:
    return "You have blackjack! You win :D"
  elif comp_score == user_score:
    return "Draw."
  elif comp_score < user_score:
    return "You win :D"
  elif comp_score > user_score:
    return "You lose :("
    
def play_game():    
    user_card_list = []
    user_card_list.append(deal_card())
    user_card_list.append(deal_card())
  
   
    comp_card_list = []
    comp_card_list.append(deal_card())
    comp_card_list.append(deal_card())
    
    keep_going = True
    
    while keep_going:   
      
      print(f"\nYour cards: {user_card_list}, current score: {score(user_card_list)}")
      print(f"Computer's first card: {comp_card_list[0]}")
      if score(comp_card_list) == 21 or score(user_card_list) == 21 or score(user_card_list) > 21:
        keep_going = False
      else:
        another_card = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
    
        if another_card == 'y':
          user_card_list.append(deal_card())
        else:
          keep_going = False
          
    while score(comp_card_list) < 17:
      comp_card_list.append(deal_card())
    
    print(f"\nYour final hand: {user_card_list}, final score: {score(user_card_list)}")
    print(f"Computer's final hand: {comp_card_list}, final score: {score(comp_card_list)}\n")
  
    print(compare(user_score = score(user_card_list), comp_score = score(comp_card_list)))


while input("\nDo you want to play a game of Blackjack? type 'y' or 'n': ") == 'y':
  clear()
  print(logo)
  play_game()
else:
  print("Okay, goodbye.")
  
