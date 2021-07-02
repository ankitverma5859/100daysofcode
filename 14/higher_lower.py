import random
import game_data
import art
import os

data = game_data.data
data_length = len(game_data.data) - 1
for_player_index = -1
against_player_index = -1
continue_game = True
score = 0

def get_player():
  player_index = random.randint(0,data_length)
  while player_index == for_player_index:
    player_index = random.randint(0,data_length)
  return player_index

def print_player_details(player_index, is_against):
  name = data[player_index]["name"]
  description = data[player_index]["description"]
  country = data[player_index]["country"]
  if bool(is_against):
    print(f"Against B: {name}, {description}, from {country}")
  else:
    print(f"Compare A: {name}, {description}, from {country}")

while continue_game:
  os.system('clear')
  print(art.logo)
  if score == 0:
    for_player_index = get_player()
  else:
    for_player_index = against_player_index
  print_player_details(for_player_index, False)
  A_follower_count = data[for_player_index]["follower_count"]

  print(art.vs)

  against_player_index = get_player()
  print_player_details(against_player_index, True)
  B_follower_count = data[against_player_index]["follower_count"]

  player_option = input("Who has more followers?Type 'A' or 'B':")

  if player_option == 'A':
    if A_follower_count > B_follower_count:
      score += 1
      print(f"You are right. Current score: {score}")
    else:
      continue_game = False
  else:
    if B_follower_count > A_follower_count:
      score += 1
      print(f"You are right. Current score: {score}")
    else:
      continue_game = False

  print(f"Sorry that's wrong. Your final score is {score}")
