import turtle

class LTurtle:
    def __init__(self, initial_position = (0, -200), initial_angle = 90, angle = 90, length=100):
        turtle.penup()
        turtle.goto(initial_position)
        turtle.setheading(initial_angle)

        self.length = length
        self.initial_position = initial_position
        self.initial_angle = initial_angle
        self.angle = angle
        self.stack = []

    def set_length(self, length):
        self.length = length

    def mainloop(self):
        turtle.mainloop()

    def reset(self):
        turtle.reset()
        turtle.goto(self.initial_position)
        turtle.setheading(self.initial_angle)
        turtle.penup()

    def hide(self):
        turtle.hideturtle()

    def draw(self):
        turtle.pendown()
        turtle.forward(self.length)
        turtle.penup()

    def forward(self):
        turtle.forward(self.length)

    def turnleft(self):
        turtle.left(self.angle)

    def turnright(self):
        turtle.right(self.angle)

    def push(self):
        self.stack.append((turtle.position(), turtle.heading()))

    def pop(self):
        pos, heading = self.stack.pop()
        turtle.goto(pos)
        turtle.setheading(heading)

if __name__ == "__main__":
    lturtle = LTurtle()
    lturtle.push()
    lturtle.draw()
    lturtle.push()
    lturtle.turnleft()
    lturtle.draw()
    lturtle.pop()
    lturtle.turnright()
    lturtle.draw()
    lturtle.pop()
    lturtle.turnleft()
    lturtle.draw()
    turtle.mainloop()
