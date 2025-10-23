import random 

fruits = ["apple", "melon", "watermelon", "strawberry", "grape", "avocado", "orange"]
fruit = random.choice(fruits)
guess_letter = []
display = ["_"] * len(fruit)
life = 6
def phangman ():
    hangman =r"""
        +---+
        |   |
            |
            |
            |
            |
        =========
    """
    hangman1 =r"""
        +---+
        |   |
        o   |
            |
            |
            |
        =========
    """
    hangman2 =r"""
        +---+
        |   |
        o   |
       /    |
            |
            |
    =========
    """
    hangman3 =r"""
        +---+
        |   |
        o   |
       / \  |
            |
            |
        =========
    """
    hangman4 =r"""
        +---+
        |   |
        o   |
       /|\  |
            |
            |
        =========
    """
    hangman5 =r"""
        +---+
        |   |
        o   |
       /|\  |
       /    |
            |
        =========
    """
    hangman6 =r"""
        +---+
        |   |
        o   |
       /|\  |
       / \  |
            |
            |
        =========
    """
    global life
    
    if life == 6:
       print(hangman)
    elif life == 5:
       print(hangman1)
    elif life == 4:
       print(hangman2)
    elif life == 3:
        print(hangman3)
    elif life == 2:
        print(hangman4)
    elif life == 1:
        print(hangman5)
    elif life == 0:
        print(hangman6)




print(r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
''')
print('Category fruit')

while '_' in display :
    if life > 0:
        print("\nword to guess \t: " + "".join(display))
        guess_user = input("guess a letter \t: ")

        for position in range(len(fruit)):
            letter = fruit[position]
            if letter == guess_user:
                display[position] = letter

        if guess_user in guess_letter:
            print(f'you already guest {guess_user}, try another')
            continue
        else:
            guess_letter.append(guess_user)

        if guess_user not in fruit :
            life -=1
            print('The Letter not in word, try another')
        else:
            print('correct')

        phangman()
        print(f"************* Live {life}/6 ****************")

    else:
        phangman()
        print(f"you lose, the word is {fruit}")
        exit()




print(f"you win with {life} life, and the word is {fruit}  🎉🎉 ")



