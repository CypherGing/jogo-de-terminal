import os, json, curses
import nen, entities


linha = " "
coluna = '''

'''

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def build_character():
     clear_screen()
     print(coluna*3)
     name = input(f'''{linha*50}Qual é o seu nome? ''',)
     clear_screen()

     age = int(input('''
                       -------------------------------------------------
                       ![Sua idade pode influenciar em eventos do jogo]!
                       -------------------------------------------------
                       Quantos anos você tem?  '''))
     clear_screen()
     sex = input('''
                       ![Digite M para Masculino e F para Feminino]!
                       Qual é o seu sexo? (M/F)
                 ''')

     print("Bla", )

build_character()
