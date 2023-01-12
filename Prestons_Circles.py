import random

class Notes:
    def __init__(self, canvas, horizontal, vertical, letter):
        self.canvas = canvas
        self.horizontal = horizontal
        self.vertical = vertical
        self.letter = letter
        self.shape = self.canvas.create_oval(self.horizontal, self.horizontal, self.vertical, self.vertical,
                                             fill="blue")
        self.xspeed = random.randint(4, 6)
        self.yspeed = 0
        self.next_animate = None
        self.HEIGHT = 720

    def move(self):
        position = self.canvas.coords(self.shape)
        # setting border for ball to bounce horizontally if reached left or right of screen
        # if position[2] + self.xspeed >= self.canvas.winfo_width():
        if position[2] + self.xspeed >= self.HEIGHT + 10:
            # self.clear()
            return True
        self.canvas.move(self.shape, self.xspeed, self.yspeed)
        return False

    # def animate(self):
    #     self.move()
    #     self.next_animate = self.canvas.after(25, self.animate)

    def go(self):
        # If we aren't already animating, start animation
        if self.next_animate is None:
            self.animate()

    def stop(self):
        # If any animation is pending, cancel it to stop animation
        if self.next_animate is not None:
            self.canvas.after_cancel(self.next_animate)
            self.next_animate = None

    def clear(self):
        self.canvas.delete(self.shape)

    def give_letter(self):
        return self.letter

