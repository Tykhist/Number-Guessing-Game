
user_input = int(input())

correct_guess = 12

tries = 0

def guesser():
  if user_input == correct_guess and tries == 0:
    print("Wow, on the first try? You are amazing!")
  elif user_input > correct_guess and tries <= 3:
    print("Try again, nerdo. Too high!")
    tries += 1
  elif user_input < correct_guess and tries <= 3:
    print("Try again, bumbo. Too low!")
    tries += 1
  elif user_input == correct_guess and tries <= 3:
    print("Correct! Want a cookie?")
  elif tries == 4:
    print("Alright, you're done. The answer was " + str(correct_guess) + ". Get outta here!")
    print("You were about, uhhhh... " + str(user_input - correct_guess) " off")
    tries += 1
  elif tries > 4:
    print("Why are you still guessing? Re-run the file if you want to try again.")
    tries += 1
  else:
    print("What did you do?...")
   
print("Guess what number I'm thinking of!")
guesser()
 
