import random

def guessnumber():
  count = 0
  lowerbound = int(input("Enter The lower bound"))
  upperbound = int(input("Enter The upper bound"))
  target = random.randint(lowerbound,upperbound)
  flag = True
  while(flag):
    guess = int(input("Guess the Number"))
    if guess == target:
      print(f'Guess {count}: {guess} → Correct!')
      flag = False
    elif guess < target:
      count += 1
      print(f'Guess {count}: {guess} → To low!')
      
    else:
      count += 1
      print(f'Guess {count}: {guess} → To high!')
      
    
guessnumber()
