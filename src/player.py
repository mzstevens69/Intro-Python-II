# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, player_name, current_room):
        self.player_name = player_name
        self.current_room = current_room 
        
        def move(self, room):
            self.room = room[room_name]