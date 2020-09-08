class GearbBox:

    def __init__(self, type, num_of_gears):
        self.type = type
        self.num_of_gears = num_of_gears
        self.current_gear = "N"

    def change_gear(self, gear):
        self.current_gear = gear
    
    