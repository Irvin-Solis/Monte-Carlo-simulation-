import random
import time

def rand_hand(sim, hand):
  for x in range(13):
    card = random.choice(deck)
    hand.append(card)
    if(not sim):
      deck.remove(card)

def card_value(card):
  num = card[0]
  value = 0
  if('A' == num):
    value = 4
  elif('K' == num):
    value = 3
  elif('Q' == num):
    value = 2
  elif('J' == num):
    value = 1
  return value

def distribution(hand, dist, point): # dist(2, 1, 0), point(1, 2, 5)
  value = 0
  suits = {
    "H": 0,
    "S": 0,
    "D": 0,
    "C": 0
  }
  for card in hand:
    card_suit = card[-1]
    suits[card_suit]+=1
  for suit in suits:
    if(suits[suit] == dist):
      value+=point
  return value

def hand_value(hand):
  value = 0
  for card in hand:
    value+=card_value(card)
  # doubleton
  value+=distribution(hand, 2, 1)
  # singleton
  value+=distribution(hand, 1, 2)
  # void
  value+=distribution(hand, 0, 5)
  return value

def sim_partner_hand_value():
  p_hand = []
  rand_hand(True, p_hand)
  p_hand_value = hand_value(p_hand)
  return p_hand_value

def simulation(num_of_sim, hand_value):
  scores = {
    "Pass": 0,
    "Part score": 0,
    "Game": 0,
    "Small slam": 0,
    "Grand slam": 0
  }
  for x in range(num_of_sim):
    sim_hand_value = sim_partner_hand_value()
    value  = sim_hand_value + hand_value
    if(value >= 36):
      scores["Grand slam"]+=1
    elif(value >= 32):
      scores["Small slam"]+=1
    elif(value >= 26):
      scores["Game"]+=1
    elif(value >= 20):
      scores["Part score"]+=1
    else:
      scores["Pass"]+=1

  # Print Results
  for key, value in scores.items():
    print(key, ': ', (value/num_of_sim)*100, '%')

# Main Program
hand = []
DECK = ["2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S","JS", "QS", "KS", "AS",
        "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H","JH", "QH", "KH", "AH",
        "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D","JD", "QD", "KD", "AD",
        "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C","JC", "QC", "KC", "AC"]

deck = DECK.copy()
repeat = True

while repeat:
  # Player Hand
  rand_hand(False, hand)
  print("Here is your hand:")
  print(hand)
  player_hand_value = hand_value(hand)
  print("This Hand is worth: ", player_hand_value, "points")
  print("Running Simulation...")
  time.sleep(1.5)

  simulation(1000, player_hand_value)
  ans = input("Another hand [Y/N]?")
  if(ans == "Y"):
    hand = []
    deck = DECK.copy()
    repeat = True
  else:
    repeat = False
