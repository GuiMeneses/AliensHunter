import pygame
import sqlite3

from code.GameOverScreen import GameOverScreen
from code.GameScreen import GameScreen
from code.MenuScreen import MenuScreen
from code.ScoreScreen import ScoreScreen

# Cria o banco e tabela se não existir
conn = sqlite3.connect('jogo.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS score_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        score INTEGER NOT NULL,
        time TEXT NOT NULL,
        nick TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

menu = MenuScreen()

while True:
    menu_return = menu.run()
    if menu_return == 0:
        game_return = GameScreen().run()   # Exemplo: [170, '00:07']
        game_over_return = GameOverScreen(game_return[0], game_return[1]).run()  # Exemplo: 'AAAA'

        list_return = [game_return[0], game_return[1], game_over_return]

        # Salva no banco
        conn = sqlite3.connect('jogo.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO score_data (score, time, nick)
            VALUES (?, ?, ?)
        ''', (list_return[0], list_return[1], list_return[2]))
        conn.commit()
        conn.close()

    elif menu_return == 1:
        ScoreScreen().run()
    elif menu_return == 2:
        pygame.quit()
        quit()
