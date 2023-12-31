import random
import time
import turtle

delay = 0.1
score = 0
highestscore = 0
bodies = []


#Creating Screen
s = turtle.Screen()
s.bgcolor("black")
s.setup(width=600, height=600)
s.title("Snake Game")
s.tracer(0)

#creating border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-320,317)
turtle.pendown()
turtle.color('red')
turtle.forward(645)
turtle.right(90)
turtle.forward(645)
turtle.right(90)
turtle.forward(645)
turtle.right(90)
turtle.forward(645)
turtle.penup()
turtle.hideturtle()

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("red")
head.goto(0, 0)
head.penup()
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.fillcolor("yellow")
food.penup()
food.ht()
food.goto(0, 150)
food.st()



#scoring
scoring=turtle.Turtle()
scoring.speed(0)
scoring.color('green')
scoring.penup()
scoring.hideturtle()
scoring.goto(0,318)
scoring.write("Score: 0   Highest Score: 0",align='center',font=('Courier',22,'bold'))


def moveup():
    if head.direction != "down":
        head.direction = "up"


def movedown():
    if head.direction != "up":
        head.direction = "down"


def moveleft():
    if head.direction != "right":
        head.direction = "left"


def moveright():
    if head.direction != "left":
        head.direction = "right"


def movestop():
    head.direction = "stop"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")

while True:
    s.update()

    if head.xcor() > 290:
        head.setx(-290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)
    if head.xcor() < -290:
        head.setx(290)

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("white")
        body.fillcolor("green")
        body.penup()
        bodies.append(body)

        score += 10

        delay += 0.004

        if score > highestscore:
            highestscore = score
        scoring.clear()
        scoring.write("Score:{}   Highest Score: {}".format(score, highestscore),align='center',font=('Courier',22,'bold'))


    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)
    move()

    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for body in bodies:
                body.goto(1000, 1000)

            bodies.clear()

            score = 0
            delay = 0.1

            scoring.clear()
            scoring.write("Score:{}   Highest Score: {}".format(score, highestscore),align='center',font=('Courier',22,'bold'))

    time.sleep(delay)

