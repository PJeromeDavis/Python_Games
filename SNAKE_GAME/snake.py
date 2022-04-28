import turtle as t
POSITIONS = [(0,0), (-20,0),(-40,0)]

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_body = t.Turtle()
        snake_body.penup()
        snake_body.shape("square")
        snake_body.color("white")
        snake_body.setposition(position)
        self.snake.append(snake_body)

    def snake_reset(self):
        for snake_body in self.snake:
            snake_body.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()


    def increase_in_body(self):
        self.add_segment(self.snake[-1].position())

    def movement(self):
        n = len(self.snake) - 1
        while n != 0:
            self.snake[n].setposition(self.snake[n - 1].position())
            n -= 1
        self.snake[0].forward(20)

    def move_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
            #self.movement()
        # for n in (range(len(snake))):

    def move_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)
            #self.movement()
            # for n in (range(len(snake))):

    def move_up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)
            #self.movement()
                # for n in (range(len(snake))):

    def move_down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)
            #self.movement()

