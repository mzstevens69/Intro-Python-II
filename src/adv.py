import textwrap
import sys
import os
import time
import cmd
from room import Room
from loot import Loot
from player import Player


BLUE = '\033[36m'
RED ='\033[91m'
GREEN = '\033[92m'
#Intro Start 

def intro_start():
    option = input('\n→ ')
    if option.lower() == ('start'):
        set_up()
    elif option.lower() == ('help'):
        help_me()
    elif option.lower() == ('q'):
        sys.exit()
    while option.lower() not in ['start', 'help', 'q']:
        print('Enter a valid command.')
        option = input('→ ')

 
# Game prompts 
        
def start_intro():
    os.system('clear')
    typed_text('🔆' * 16)
    typed_text(GREEN +'\n🔆 Welcome to my Adventure❕  🔆\n')
    typed_text('🔆' * 16)
    typed_text('\n          ➤start               ')
    typed_text('\n          ➤help                ')
    typed_text('\n          ➤q to quit               ')
    typed_text('\n Copyright 2020 Bighead Games  \n')
    typed_text('🔆' * 16)
    intro_start()
        
def help_me():
    typed_text('🔆' * 16)
    typed_text(RED +'\n🔆     Welcome to Help❕     🔆\n')
    typed_text('🔆' * 16)
    typed_text('\n→ Use n, s, e, w to move.')
    typed_text('\n→ Type the command at prompt ')
    typed_text('\n→ If you want to look in room ')
    typed_text('\n→ Type "l" or "look" at locations')
    typed_text('\n→ Type "pick up" to get loot.')
    typed_text('\n→ Type "i" or "inventory" to see')
    typed_text('\n→ what loot you are carrying. ')
    typed_text('\n→ Type the command at prompt ')
    typed_text('\n→ Good Luck and have fun!\n')
    typed_text('🔆' * 16)

    intro_start()
    
    
# the Loot

ruby = Loot( 'ruby', 'A sparkling gem, Red in color' )
tomahawk = Loot('Tomahawk', 'A medium sized Tomahawk made from Bones')
gold_chest = Loot('gold chest', 'A large ches full of Gold')
broken_dagger = Loot('broken dagger', 'A slightly bent dagger with the tip broken off')    
gold_coin = Loot('Gold coin', 'A Spainish coin made from pure gold.')       
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"), 

    'in foyer':    Room("Foyer","""Dim light filters in from the south. Dusty
passages run north and east."""),

    'by overlook': Room("Grand Overlook","""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, to the north a dilapidated bridge stretchs across the chasm."""),
    
    'by a hanging bridge': Room("Hanging Bridge","""Broken and missing boards make up 
this bridge to the other side of the chasm. You can see familiar objects on 
the horizion across the bridge to the north"""), 

    'in the narrow':   Room("Narrow Passage","""The narrow passage bends here from west
to north. The smell of gold permeates the air."""), 

    'in the treasure chamber': Room("Treasure Chamber","""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""), 
}


# Link rooms together

room['outside'].n_to = room['in foyer']
room['in foyer'].s_to = room['outside']
room['in foyer'].n_to = room['by overlook']
room['by overlook'].n_to = room['by a hanging bridge']
room['in foyer'].e_to = room['in the narrow']
room['by overlook'].s_to = room['in foyer']
room['in the narrow'].w_to = room['in foyer']
room['in the narrow'].n_to = room['in the treasure chamber']
room['in the treasure chamber'].s_to = room['in the narrow']

#treasure added

room['by overlook'].add_treasure(tomahawk)
room['in foyer'].add_treasure(ruby)
room['outside'].add_treasure(gold_coin)
room['in the treasure chamber'].add_treasure(gold_chest)





#Movement

    
def prompt():
    
    print('\n'+ '→' * 67) 
    print(' ') 
    typed_text(f'You are standing {new_player.location.name}\n\n{new_player.location.description}\n\n') 
    print('\n'+ '→' * 67)
    typed_text(f'{new_player.name} what do you want to do? \n') 
    typed_text('Directions: n, s, e, w \n')
    typed_text('Actions: i, l, pickup, drop \n')  
    action = input('➤ ')
    
    actions_to_do = ['n', 's', 'e', 'w', 'q', 'i', 'inventory', 'l', 'look', 'pickup', 'drop']
      
    while action.lower() not in actions_to_do:
        typed_text('Unknown action???, try again. \n')
        action = input('➤ ')
        
    if action.lower() == 'q':
        typed_text('😈 Maybe you can try again later. 😈')
        sys.exit()
        
    elif action.lower() in ['n', 's', 'e', 'w']:
        new_player.player_move(action.lower())
    
    elif action.lower() in ['i', 'inventory']:
        new_player.look()
        
    elif action.lower() == 'pickup':
        new_player.pickup(treasure)
        
    elif action.lower() == 'drop':
        new_player.drop(treasure)            
    
   

        
        
def main_loop():
    while True:
        prompt()

def end_game():
    if len(new_player.inventory) >= 4:
        end_game == True
        typed_text('You have WON this game!!!')

new_player = Player( 'Player1', room['outside'])   
location = new_player.location

        
# Set up the game
def set_up():
    os.system('clear')   
    your_name = "What is your name? \n"   
    typed_text(your_name)
    player_name = input('➤')
    new_player.name = player_name
        
    main_loop()     

def typed_text(print_this):
    for character in print_this:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.015)           

start_intro()
