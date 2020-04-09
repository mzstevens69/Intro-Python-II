# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, room_name, room_descrp, n_to=None, s_to=None, e_to=None, w_to=None):
        self.room_name = room_name
        self.room_descrp = room_descrp
        
        self.n_to = [] if n_to is None else n_to
        self.s_to = [] if s_to is None else s_to
        self.e_to = [] if e_to is None else e_to
        self.w_to = [] if w_to is None else w_to