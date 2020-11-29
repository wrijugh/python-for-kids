import turtle
import time

time.sleep(2)
turtle.color("red", "yellow")
turtle.begin_fill()

for i in range(18):    
    turtle.circle(120)
    turtle.right(20)

turtle.end_fill()
turtle.done()