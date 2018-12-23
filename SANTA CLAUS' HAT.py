

from turtle import *
from shapes import *
from random import randint

myPen = Turtle()
myPen.shape("turtle")
myPen.speed(1)

window = turtle.Screen()
window.bgcolor("#FFFFFF")


draw_circle(myPen, "#69D9FF", 0, -200, 200)


#Complete your code here...
draw_triangle(myPen,'red',-120,-110,250)
draw_circle(myPen, "white", 4.3, 100, 18)
draw_circle(myPen, "white", -115, -120, 18)
draw_circle(myPen, "white", -85, -120, 18)
draw_circle(myPen, "white", -55, -120, 18)
draw_circle(myPen, "white", -25, -120, 18)
draw_circle(myPen, "white", 5, -120,18)
draw_circle(myPen, "white", 35, -120, 18)
draw_circle(myPen, "white", 65, -120, 18)
draw_circle(myPen, "white", 95, -120, 18)
draw_circle(myPen, "white", 125, -120, 18)

myPen.hideturtle()
