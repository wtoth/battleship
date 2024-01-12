
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
    
    def has_ship(self):
        return self.ship
    
    def attack(self):
        if self.attacked == True:
            print("This space has already been attacked")
            return [False]
        self.attacked = True
        if self.ship == True:
            return [True, 1]
        else:
            return [True, 0]
        
        