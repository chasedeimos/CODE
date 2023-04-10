import random
import turtle
t = turtle.Turtle()

while True:
    x=random.randint(1,100)
    y=random.randint(1,360)
    left_right=random.randint(0,1)
    if left_right == 1:
        t.right(y)
    else:
        t.left(y)
    t.forward(x)
    continue

