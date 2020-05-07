# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.treasure = []
        self.n_to  =  None
        self.s_to  =  None
        self.e_to  =  None
        self.w_to  =  None
        
    # def treasure(self):
    #     if len(self.treasure) == 0:
    #         print('No treasure here \n')
    #     else:
    #         print('You see')
    #         for treasure in self.treasure:
    #             print(treasure.name)

    def __str__(self):
        print(f" {self.name} \n{self.description}")

    def add_treasure(self, *new_treasure):
        for treasure in new_treasure:
            self.treasure.append(treasure)
        
    def remove_treasure(self, treasure):
        if treasure in self.treasure:
            self.treasure.remove(treasure)
        else:
            print(f'{treasure} is not here.')    
        