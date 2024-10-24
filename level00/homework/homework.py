from turtle import * 


#we wont to paint a house

#step1: draw a square

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("brown")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(55,65)
pendown()
color("yellow")
begin_fill()

back(60)
left(90)
back(40)
left(90)
back(60)
left(90)
back(40)
left(90)
end_fill()


penup()
goto(185,65)
pendown()

begin_fill()
back(60)
left(90)
back(40)
left(90)
back(60)
left(90)
back(40)
left(90)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()






exitonclick()