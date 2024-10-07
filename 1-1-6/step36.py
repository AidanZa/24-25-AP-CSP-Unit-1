import turtle as trtl

painter = trtl.Turtle()
painter.pensize(5)

# draw curved arc
painter.penup()
painter.goto(0, -20)
painter.pendown()
painter.circle(100, 360)

# draw segmented arc
painter.penup()
painter.goto(0, 20)
painter.pendown()
painter.circle(100, 180, 8)

wn = trtl.Screen()
wn.mainloop()