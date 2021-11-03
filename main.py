import database
import random
import game

def _choose_random_word():
    num_words = len(database.words)
    index_random_word = random.randint(0, num_words-1)
    return database.words[index_random_word]

while True:
    start = input('Você deseja iniciar um jogo de forca? [S/N]').upper().strip()

    if start == 'S':
        word = _choose_random_word()
        game.play(word.upper())

    elif start == 'N':
        print('Fechando o jogo...')
        exit()
