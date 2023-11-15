import random

word = ""
letters = []
guessed = []
tries = 0

with open("words.txt", "r") as words_file:
    words = words_file.readlines()
    
    if words:
        word = str(random.choice(words)).strip()

def draw_body(fails: int):
    
    lose = 6
    
    body = {
        1: "O",
        2: "|",
        3: "---",
        4: "|", 
        5: "/",
        6: "\\"
    }
    
    print("- - - -")
    print("-   |")
    y = 0
    for _ in range(6):
        y += 1
        if y <= fails:
            print("-", end="")
            if y <= 5:
                if y == lose - 1 and fails == lose:
                    print(" " * 2 + "/ \\")
                else:
                    spaces = 3 if len(body[y]) == 1 else 2
                    print(" " * spaces, end="")
                    print(body[y])
        else:
            print("-")
    print("- - - - \n")
    
#Hola
def find_coincidence(letter: str = ""):   
    if letter in word:
        for i, w in enumerate(word):
            if w == letter and letters[i] == '_':
                letters[i] = letter
                guessed.append(letter)
                return True
        return False

for _ in range(len(word)):
    letters.append('_')
    
while True:
    
    draw_body(tries)
    
    print(f"Tu palabra es: {' '.join(letters)}")

    print(f"Letras adivinadas: {' '.join(guessed)}")
    
    letter = input("Ingresa una letra: ")
    
    #Search coincidences
    guess = find_coincidence(letter)

    if not guess:
        print(f"La letra {letter} no se encuentra en la palabra")
        tries += 1
    else:
        if ''.join(letters) == word: 
            print(f"Haz ganado!! La palabra es {word}")
            break
        else:
            print("¡Haz encontrado una letra!")

    if tries == 6:
        draw_body(tries)
        print("Juego perdido")
        break
    
    print("\n")