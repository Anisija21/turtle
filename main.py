import turtle
t = turtle.Turtle()
t.color('green')
t.circle(50)
t.color('white')
t.forward(70)
t.color('black')
t.circle(50, steps=3)
t.color('white')
t.forward(50)
t.color("red")
t.right(75)
t.forward(100)
 
for i in range(4):
    t.right(144)
    t.forward(100)
     
turtle.done()