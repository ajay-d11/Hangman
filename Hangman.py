import random
words = ["Zimmerman", "Rai", "Kwantlen", "PoloG", "LilTjay","hello-hello","b o b", "Scorey", "FivioForeign", "KingVon", "PopSmoke", "ABoogie", "France", "Canada", "Chicago", "NewYork", "Syracuse", "Surrey", "BritishColumbia", "NorthAmerica", "Cloverdale", "Guildford"]
lives_visual_dict = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }

import string
import time

def get_valid_word(words):
    word = random.choice(words)
    while "Rai" in word or "Zimmerman" in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase) 
    used_letter = set()

    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters: ", ' '.join(used_letter))
        time.sleep(1)
        
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print(lives_visual_dict[lives])
        print("Current word: ", " ".join(word_list))
        time.sleep(1)
        
        user_letter = input("Guess a letter for this place or person: ").upper()
        if user_letter in alphabet - used_letter:
                used_letter.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    print('')
                    time.sleep(1)
                
                else:
                    lives = lives - 1
                    print("Congradulations! The letter you chose..... is NOT in the word, HAHAHA")
                    time.sleep(1)

        elif user_letter in used_letter:
            print("Are you blind? You have already used this letter BOZO")
            time.sleep(1)

        else:
                print("WRONG, guess again loser")
                time.sleep(1)

    if lives == 0:
        print(lives_visual_dict[lives])
        print("Wow you suck, you couldn't even guess the word", word)
        time.sleep(1)

    else:
        print("Look who's kind of smart, you actually guessed the word", word)
        time.sleep(1)

hangman()
play_again = input("Does yo dumb ah want to play again? yes or no.")

if play_again == "yes":
    hangman()
    time.sleep(1)
else:
    print("I knew you wouldn't, adios")
    time.sleep(1)
