class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []
        
         

    def __str__(self):
        return f" {self.name} {self.location}"
        
    
    def player_move(self, direction):
        moved = getattr(self.location, f'{direction}_to')
        
        if moved == None:
            print('you can not go that way.\n') 
                   
        else:
            self.location = moved
            
    
        
    def pickup(self, treasure):
        print(f'you picked up {treasure}')
        for treasure in self.location.treasure:
            if treasure.name == treasure:
                self.inventory.append(treasure)
                self.location.remove_treasure(treasure)
            else:
                print(f'{self.name} cannot find {treasure} ')
            
    def drop(self, treasure):
        print(f'you have dropped {treasure} ')
        for treasure in self.location.treasure:
            if treasure.name == treasure:
                self.inventory.remove(treasure)
                self.location.add_treasure(treasure)
            else:
                print(f' cannot drop {treasure} ')
            
    def look(self):
        self.location.treasure