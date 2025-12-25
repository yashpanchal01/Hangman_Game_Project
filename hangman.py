import random 

words = ('apple', 'orange', 'banana', 'coconut', 'watermelon')

Hangman_art = {0:('   ',
                 '   ',
                 '   '),
               1:(' O ',
                 '   ',
                 '   '),
               2:(' O ',
                 ' | ',
                 '   '),
               3:(' O ',
                  '/| ',
                 '   '),
               4:(' O ',
                  '/|\\',
                 '    '), 
               5:(' O ',
                  '/|\\',
                  '  \\'), 
               6:('  O ',
                 ' /|\\',
                 ' / \\')}

def display_hangman(Wrong_guesses):
    print('\n----------------')
    for line in Hangman_art[Wrong_guesses]:
        print(line)
    print('----------------')
    

def display_hint(hint):
    result = ''.join(hint)
    print(result)


def main():
    answer = random.choice(words)
    # hint = '_' * len(answer)
    # hint = list(hint)
    hint = ['_'] * len(answer)

    Wrong_guesses = 0
    is_running = True 
    # print(hint)
    guessed_letters = set()

    
    while is_running:
        display_hangman(Wrong_guesses)
        display_hint(hint)
        
        guess = str(input('Enter your Guess: '))
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input!")
            continue
        
        if guess in guessed_letters:
            print('already guessed!')
            continue

        guessed_letters.add(guess)

        if guess in answer: 
             for i in range(len(answer)):
                  if guess == answer[i]:
                       hint[i] = guess
                       
        else: 
            Wrong_guesses += 1
            print(f"{guess} is not in the word.")

        if '_' not in hint:
            display_hint(hint)
            print("You Won!")
            is_running = False
        
        if Wrong_guesses == 6:
            display_hangman(Wrong_guesses)
            is_running = False 
            print("You Lost!")

                       
        
        
if __name__ == "__main__":
    main()


