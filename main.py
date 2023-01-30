import turtle
import time
import random
import winsound

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second

# Create the screen and set the title
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("#C0C0C0")
window.bgpic("background.png")
window.setup(width=600, height=600)
window.tracer(0)

# Create the snake and set its properties
snake = turtle.Turtle()
snake.speed(0)
snake_color = "red"
snake.shape("square")
snake.color(snake_color)
snake.penup()
snake.goto(0, 100)

# Score
score = 0
high_score = 0

# Create the food and set its properties
score_table = turtle.Turtle()
score_table.speed(0)
score_table.shape("square")
score_table.color("white")
score_table.penup()
score_table.goto(0, 260)
score_table.hideturtle()
score_table.write("Score : {} High Score : {} ".format(
    score, high_score), align="center", font=("candara", 24, "bold"))

# Create the food and set its properties
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.penup()
food.shapesize(2, 2)
food.goto(0, 0)

# Snake body created
body = []


def add_body():
    new_part = turtle.Turtle()
    new_part.speed(0)
    new_part.shape('square')
    new_part.color('black')
    new_part.penup()
    body.append(new_part)


def refresh_food():
    colors = random.choice(['red', 'green', 'black'])
    shapes = random.choice(['square', 'triangle', 'circle'])
    food.shape(shapes)
    food.color(colors)
    food.shapesize(1, 1)
    return food


# Set the direction of the snake
snake.direction = "stop"


# Create a function to move the snake
def move():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 15)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 15)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 15)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 15)


# Create a function to change the direction of the snake
def go_up():
    if snake.direction != "down":
        snake.direction = "up"


def go_down():
    if snake.direction != "up":
        snake.direction = "down"


def go_left():
    if snake.direction != "right":
        snake.direction = "left"


def go_right():
    if snake.direction != "left":
        snake.direction = "right"


# Speed Properties
speed_increased = False
speed = 0.2


def speed_up():
    global speed, speed_increased
    if not speed_increased:
        print("Speed boost ACTIVE !")
        speed -= 0.1
        snake.color("red")
        speed_increased = True


def speed_down():
    global speed, speed_increased
    if speed_increased:
        print("Speed boost PASSIVE !")
        speed += 0.1
        snake.color("white")
        speed_increased = False


def new_speed(_speed):
    return _speed - 0.01


turtle.onkeypress(speed_up, 'space')
turtle.onkeyrelease(speed_down, 'space')

# Bind the functions to the arrow keys
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

while True:
    window.update()
    # WHEN THE SNAKE DIES
    if snake.xcor() > 300 or snake.xcor() < -300 or snake.ycor() > 300 or snake.ycor() < -300:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = 'stop'
        winsound.Beep(frequency, (duration + 500))
        for body_part in body:
            body_part.goto(1000, 1000)

        body = []
        score = 0
        speed = 0.2
        score_table.clear()
        score_table.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("caddr", 24, "bold"))

    # Check for collision with food and recreate food and relocate it
    if snake.distance(food) < 20:

        winsound.Beep(frequency, duration)

        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        print(speed)
        refresh_food().goto(x, y)
        add_body()
        speed = new_speed(speed)

        score = score + 10
        if score > high_score:
            high_score = score
        score_table.clear()
        score_table.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("caddr", 24, "bold"))

    for i in range(len(body) - 1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)

    if len(body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)

    move()
    time.sleep(speed)
