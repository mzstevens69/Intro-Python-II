

class Loot:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
        def pick_up(self):
            print(f'you picked up {self.name}')
        
        def drop():
            print(f'you just dropped {self.name} ')