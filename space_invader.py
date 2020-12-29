# Python game for space invaders
# Python 3.6

import turtle
import os
import math
import random

# Set up screen
scrn = turtle.Screen()
scrn.bgcolor("black")
scrn.title("Space Invaders")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.penup()
player.speed(0)
player.color("blue")
player.shape("triangle")
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# Create the enemies
enemy_num = 5
enemies = []
for i in range(enemy_num):
    enemy = turtle.Turtle()
    enemy.penup()
    enemy.speed(0)
    enemy.color("red")
    enemy.shape("circle")
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

    enemies.append(enemy)
enemyspeed = 2

# Create player's bullet
bullet = turtle.Turtle()
bullet.penup()
bullet.speed(0)
bullet.color("yellow")
bullet.shape("triangle")
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20
bulletstate = "ready"

# Move player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"

        # Move bullet position
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    dist = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if dist < 15:
        return True
    else:
        return False

def gameover(t1, t2):
    if t1.ycor() == t2.ycor():
        return True

# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
while True:
    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            y = enemy.ycor()
            y -= 40
            enemyspeed *= -1  # turns around
            enemy.sety(y)

        if enemy.xcor() < -280:
            y = enemy.ycor()
            y -= 40
            enemyspeed *= -1
            enemy.sety(y)

        # Check if collision
        if isCollision(bullet, enemy):
            # Reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)

            # Reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)

        # Check if player died
        if gameover(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over!")
            break

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check if bullet is on top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"




