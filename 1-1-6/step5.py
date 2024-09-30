#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider= trtl.Turtle()
spider.pensize(40)
spider.circle(20)
legs = 8
leg_length = 70
head = 360 / legs
print("head=", head)
spider.pensize(5)
counter = 0
while (counter < legs):
  spider.goto(0,20)
  spider.setheading(head*counter)
  spider.forward(leg_length)
  counter = counter + 1
  print("head*counter=", head * counter)
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()