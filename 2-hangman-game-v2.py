### Projeto 1 ###

### Game Development in Python ###

### Hangman Game ###
### Version 2 ###

import random
from os import system, name

# Function to Clear the Screen on Each Execution
def clear_screen ():
    
    if name == "nt":         #windows
        _ = system("cls")
        
    else:                    # mac, linux
        _ = system("clear")

# Function that draws the gallows on the screen
def display_hangman(chances):

    # List of stages of the gallows
    stages = [  # stage 6 (final)
"""
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |     / \\
    --
""",
                # stage 5
"""
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |     / 
    --
""",
                # stage 4
"""
    --------
    |      |
    |      O
    |     \\|/
    |      |
    |      
    --
""",
                # stage 3
"""
    --------
    |      |
    |      O
    |     \\|
    |      |
    |     
    --
""",
                # stage 2
"""
    --------
    |      |
    |      O
    |      |
    |      |
    |     
    --
""",
                # stage 1
"""
    --------
    |      |
    |      O
    |    
    |      
    |     
    --
""",
                # stage 0
"""
    --------
    |      |
    |      
    |    
    |      
    |     
    --
"""
    ]
    return stages[chances]

# Main Game Function
def game():
    
    clear_screen()
       
    # Defining Categories and Their Words
    def word_game():
        
        category = {
            "frutas": ["morango", "banana", "laranja", "uva", "abacaxi", "kiwi"],
            "animais": ["leão", "tigre", "elefante", "cachorro", "gato", "golfinho"],
            "países": ["brasil", "canadá", "japão", "austrália", "alemanha", "méxico"],
            "cores": ["vermelho", "azul", "verde", "amarelo", "roxo", "laranja"],
            "objetos": ["cadeira", "mesa", "computador", "telefone", "lápis", "mochila"]
        }
        
        # Randomly Choosing Category and Their Words
        category_chosen = random.choice(list(category.keys()))
                # Escolhendo uma palavra aleatória dentro da categoria escolhida
        word_chosen = random.choice(category[category_chosen])
        
        return [category_chosen, word_chosen]

    list_chosen = word_game()
    category = list_chosen[0]
    word = list_chosen[1]
        
    # Initial Messages
    print("\nBem-vindo(a) ao jogo a forca!")
    
    # Initializing Game Variables
    letters_found = ['_' for letter in word]
    chances = 6
    letters_wrong = []
    
    # Loop While Chances Are Greater Than Zero
    while chances > 0:
        print(f"\nA categoria é {category.upper()}. Adivinhe a palavra abaixo:\n")
        print(display_hangman(chances))
        print(" ".join(letters_found))
        print(f"\nChances restantes: {chances}")
        print(f"\nLetras erradas: {' '.join(letters_wrong)}")
                
        # Checks if the input contains exactly one character and if it is a letter.
        def askletter():
            while True:
                enter = input("\nDigite uma letra: ").lower()
                if len(enter) == 1 and enter.isalpha():
                    return enter
                else:
                    print("\nEntrada inválida. Digite apenas uma letra.")
        letter_try = askletter()
        print("\n")

        if letter_try in word:
            index = 0
            
            for letter in word:
                if letter_try == letter:
                    letters_found[index] = letter
                index += 1
        else:
            if letter_try not in letters_wrong:
                chances -= 1
                letters_wrong.append(letter_try)
            
        # Check if the Player Has Found All Letters
        if "_" not in letters_found:
            print(f"\nVocê venceu, a palavra era: {word.upper()}.")
            break
    
    # Check if the Player Has Not Found All Letters
    if "_" in letters_found:
        print(f"\nVocê perdeu, a palavra era {word.upper()}.")
        
# Bloco main
if __name__ == "__main__":
    game()
    print("\nJogo encerrado.\n")