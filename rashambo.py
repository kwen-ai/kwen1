import random

random1 = random.randint(0, 2)
paper ="""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""
choose = int(input('what you choose? 0 for rock, 1 for paper, 2 for scissors: '))

if choose == 0 :
    print(rock)
    if random1 == 0:
        print("computer chose:")
        print(rock)
        print("it's a draw")
    elif random1 == 1:
        print("computer chose:")
        print(paper)
        print("you lose")
    else:
        print("computer chose:")
        print(scissors)
        print("you win")

elif choose == 1:
    print(paper)
    if random1 == 0:
        print("computer chose:")
        print(rock)
        print("you win")
    elif random1 == 1:
        print("computer chose:")
        print(paper)
        print("it's a draw")
    else:
        print("computer chose:")
        print(scissors)
        print("you lose")
elif choose == 2:
    print(scissors)
    if random1 == 0:
        print("computer chose:")
        print(rock)
        print("you lose")
    elif random1 == 1:
        print("computer chose:")
        print(paper)
        print("you win")
    else:
        print("computer chose:")
        print(scissors)
        print("it's a draw")



