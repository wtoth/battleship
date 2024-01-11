
class Square:
    def __init__(self):
        self.ship = False
        self.attacked = False
    
    def add_ship(self):
        self.ship = True

    def attacked(self):
        self.attacked = True

    def print_board(self):
        return f"square, ship: {self.ship}, attacked: {self.attacked}"