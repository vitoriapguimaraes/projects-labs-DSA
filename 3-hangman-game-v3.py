### Game Development in Python ###

### Hangman Game ###

### Version 3 ###
# Object Oriented Programming #

# Import
import random
from os import system, name


# Function to Clear the Screen on Each Execution
def clear_screen ():
    
    if name == "nt":         #windows
        _ = system("cls")
        
    else:                    # mac, linux
        _ = system("clear")


# Board
board = ['''      
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========''']


# Class
class Hangman:

    # Constructor Method
    def __init__(self, word):
        self.word = word
        self.letter_wrong = []
        self.letter_choisen = []
    
    # Method to guess the letter
    def guess(self, letter):
    
        if letter in self.word and letter not in self.letter_choisen:
            self.letter_choisen.append(letter)
            return True
        
        if letter not in self.word and letter not in self.letter_wrong:
            self.letter_wrong.append(letter)
            return True
        
        else:
            return False
    
    # Method to check if the game has finished
    def hangman_over(self):
        return self.hangman_won() or (len(self.letter_wrong) == 6)
		
	# Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.word_hide():
            return True

	# Method to not show the lyrics on the board
    def word_hide(self):
        return ''.join([letter if letter in self.letter_choisen else '_' for letter in self.word])
    
	# Method to check the game status and print the board on the screen
    def print_game_status(self):
        
        print(board[len(self.letter_wrong)])
        
        print(f"\nPalavra {self.word_hide()}")
        
        print("\nLetras erradas:",' '.join(self.letter_wrong))
        
        print("Letras corretas:",' '.join(self.letter_choisen))
        
# Method to read a word randomly from the word bank
def word_random():
       
    category_op = {
        "frutas": ["morango", "banana", "laranja", "uva", "abacaxi", "kiwi"],
        "animais": ["leão", "tigre", "elefante", "cachorro", "gato", "golfinho"],
        "países": ["brasil", "canadá", "japão", "austrália", "alemanha", "méxico"],
        "cores": ["vermelho", "azul", "verde", "amarelo", "roxo", "laranja"],
        "objetos": ["cadeira", "mesa", "computador", "telefone", "lápis", "mochila"]
    }
        
    # Randomly Choosing Category and Their Words
    category_c = random.choice(list(category_op.keys()))
    
    # Choosing a random word within the chosen category
    word_c = random.choice(category_op[category_c])
      
    return [category_c, word_c]
    
list_chosen = word_random()
category = list_chosen[0]
word = list_chosen[1]

# Método Main - Program Execution
def main():
    
    clear_screen()

	# Create the object and select a word randomly
    game = Hangman(word)
    print("\nBem-vindo(a) ao jogo a forca!")
    print(f"\nA categoria é {category.upper()}. Adivinhe a palavra abaixo.")

	# While the game is not finished, print the status, ask for a letter and read the character
    while not game.hangman_over():
        
        # Game status
        game.print_game_status()
               
        # Terminal input + checks if the input contains exactly one character
        def user_ask():
            while True:
                enter = input("\nDigite uma letra: ").lower()
                if len(enter) == 1 and enter.isalpha():
                    return enter
                else:
                    print("\nEntrada inválida. Digite apenas uma letra.")
                    
        user_input = user_ask()
        print("-"*30)

        # Checks if the typed letter is part of the word
        game.guess(user_input)


    # Check the game status

    game.print_game_status()
    
    # According to the status, print message on the screen for the user
    if game.hangman_won():
        print("\nParabéns! Você venceu!!!")
    
    else:
        print("\nGame over! Você perdeu.")
        print(f"A palavra era {word}")
    
    print ('\nFoi bom jogar com você! Agora vá estudar!\n')


# Run the program
if __name__ == "__main__":
    main()