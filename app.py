#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

print("Para iniciar el juego, selecciona entre, piedra, papel o tijera")


import random

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    if (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        return "Player wins!"
    else:
        return "Computer wins!"

def play_game():
    valid_choices = ["rock", "paper", "scissors"]
    play_again = "yes"
    player_score = 0
    computer_score = 0

    while play_again.lower() == "yes":
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if player_choice not in valid_choices:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = random.choice(valid_choices)
        print(f"Computer chose {computer_choice}")
        winner = get_winner(player_choice, computer_choice)
        print(winner)
        if winner == "Player wins!":
            player_score += 1
        elif winner == "Computer wins!":
            computer_score += 1
        play_again = input("Do you want to play again? (yes/no): ")

    print(f"Final scores: Player - {player_score}, Computer - {computer_score}")

play_game()