import os
import turtle
import time
import random


delay = 0.1


#scores
score = 0
high_score = 0


#Set up screen
wn = turtle.Screen()
wn.title("Snake_Game_by_@Nips")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
#Turns off screen updates 
wn.tracer(0)


#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"


#Snake_food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


#Snake_body
segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  Highscore: 0", align = "center", font =("Courier", 24, "normal"))



#functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


#Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


#Main game loop
while True:
    wn.update()

    #Collision_Tests
    #Collision with wall
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        #Hide the segments
        for segment in segments:
            segment.goto(1000,1000)
        
        #Clear segments
        segments.clear()
        
        #reseting score
        score = 0

        pen.clear()
        pen.write("Score: {}  Highscore: {}".format(score, high_score), align = "center", font =("Courier", 24, "normal"))

        

    #Collision with food
    if head.distance(food) < 20:
        #Change position of food
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        #Adding_a_segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #Increasing score
        score += 1

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  Highscore: {}".format(score, high_score), align = "center", font =("Courier", 24, "normal"))


    
    #Moving end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    #move segment 0 to were the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #Collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.drection = "stop"

            #Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            #Clear the segments list
            segments.clear()

    
    time.sleep(delay)

wn.mainloop(0)


