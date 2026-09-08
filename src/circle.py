@pytch.when_green_flag_clicked
def main()
    self.go_to_xy(-100, -100)

    directions = [
        (1, 0),
        (0.5, 0.5),
        (0, 1),
        (-0.5, 0.5),
        (-1, 0),
        (-0.5, -0.5),
        (0, -1),
        (0.5, -0.5)]
        
    for dx, dy in directions:
        for i in range(100):
            self.change_x(dx)
            self.change_y(dy)
            self.create_clone()

@pytch.when_I_start_as_a_clone
def cloned()
    self.set_size(0.1)

