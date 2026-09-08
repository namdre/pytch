@pytch.when_green_flag_clicked
def main()
    Snake.directions = [
        [1, 0],
        [1, 0],
        [0.5, 0.5],
        [0.5, 0.5],
        [0, 1],
        [0, 1],
        [-0.5, 0.5],
        [-0.5, 0.5],
        [-1, 0],
        [-1, 0],
        [-0.5, -0.5],
        [-0.5, -0.5],
        [0, -1],
        [0, -1],
        [0.5, -0.5],
        [0.5, -0.5],
        ]

@pytch.when_I_start_as_a_clone
def cloned()
    self.set_size(0.2)


self.broadcast("cleanup")


self.delete_this_clone()
self.go_to_xy(-50, -150)
scale = 10
for dx, dy in Snake.directions:
    for i in range(round(40 / scale)):
        self.change_x(dx * scale)
        self.change_y(dy * scale)
        self.create_clone()




"""slider"""
slider.i = -1
slider.base = 130
slider.scale = 20
self.hide()
self.set_y(slider.base)
for x in Snake.directions:
    self.create_clone()


"""start as clone"""
self.set_size(0.3)
self.show()
slider.i += 1
self.i = slider.i
self.set_x(-200 + slider.i * 25)
self.change_y(Snake.directions[self.i][0] * slider.scale)


""" clicked"""
d = self.mouse_y - self.y_position

while self.mouse_down:
    v = (self.y_position - slider.base) / slider.scale
    self.say(v)
    self.set_y(self.mouse_y - d)
    Snake.directions[self.i][0] = v

self.say("")
print(Snake.directions)
