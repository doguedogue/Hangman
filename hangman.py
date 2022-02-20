import platform, os, random

def hangman_seq():
    game= {
        0: 
            "  +---+"+'\n'
            "  |   |"+'\n'
            "      |"+'\n'
            "      |"+'\n'
            "      |"+'\n'
            "      |"+'\n'
            "=========",
        1: 
            "  +---+"+'\n'
            "  |   |"+'\n'
            "  O   |"+'\n'
            "      |"+'\n'
            "      |"+'\n'
            "      |"+'\n'
            "=========",
        2:
            "  +---+"+'\n'
            "  |   |"+'\n'
            "  O   |"+'\n'
            "  |   |"+'\n'
            "      |"+'\n'
            "      |"+'\n'
            "=========",
        3:
            "  +---+"+'\n'
            "  |   |"+'\n'
            "  O   |"+'\n'
            " /|   |"+'\n'
            "      |"+'\n'
            "      |"+'\n'
            "=========",
        4:
            "  +---+"+'\n'
            "  |   |"+'\n'
            "  O   |"+'\n'
            " /|\  |"+'\n'
            "      |"+'\n'
            "      |"+'\n'
            "=========",
        5:
            "  +---+"+'\n'
            "  |   |"+'\n'
            "  O   |"+'\n'
            " /|\  |"+'\n'
            " /    |"+'\n'
            "      |"+'\n'
            "=========",
        6:
            "  +---+"+'\n'
            "  |   |"+'\n'
            "  O   |"+'\n'
            " /|\  |"+'\n'
            " / \  |"+'\n'
            "      |"+'\n'
            "========="
    }
    return game

def readFile():
    words = []
    file = open('data.txt', encoding="utf-8")
    lines = file.readlines()
    for line in lines:
        words.append(line)
    return words

def ramdom_word(words):
    n = random.randint(0,len(words))
    return words[n]

def empty_list(n):
    empty = []
    for i in range(1,n):
        empty.append('_')
    return empty


def is_solve(word):
    for i in word:
        if i == '_':
            return False
    return True

def print_discover(disc):
    text = ''
    for i in disc:
        text += i + ' '
    print (text+'\n')

def main():
    game = hangman_seq()

    so = platform.system().lower()
    if 'windows' in so:
        cmd = "cls"
    else:
        cmd = "clear"    
    
    words = readFile()

    word = ramdom_word(words)

    discover = empty_list(len(word))
    for value in game.values():
        while True:
            os.system(cmd)
            print ('Bienvenido al Juego de Hangman 🐍🤠🐴 @doguedogue\n')
            print (value,'\n')
            #print ('Palabra:',word,'\n') #Hint
            print_discover(discover)
            if is_solve(discover):
                break
            letra = input ("Escoge una letra: ").lower()
            if letra in word:        
                for i in range(0,len(word)):    
                    if word[i] == letra:
                        discover[i]=letra
            else:
                break
        if is_solve(discover):
            break
    if is_solve(discover):
        print('Ganaste')
    else:
        print('Perdiste')
        print('La palabra era:', word)


if __name__ == '__main__':
    main()