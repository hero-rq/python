import turtle

#turtle.forward(25)
#turtle.left(90)
#turtle.forward(25)
#turtle.left(90)
#turtle.forward(25)
#turtle.left(90)
#turtle.forward(25)
#turtle.left(90)

#정사각형
for i in range(0, 4):
  turtle.forward(75)
  turtle.left(90)

  #사다리꼴
for i in range(0, 2):
  turtle.forward(120)
  turtle.left(120)
  turtle.forward(80)
  turtle.left(60)

#별 그리기
turtle.up()
turtle.goto(-200, 50)
turtle.down()

for i in range(0, 5):
  turtle.forward(100)
  turtle.right(360*2//5)

#꽃 그려봐
turtle.up()
turtle.goto(-150, -50)
turtle.down()

turtle.pen(pencolor="blue", pensize=3)
turtle.begin_fill()

while(1):
  turtle.forward(93)
  turtle.left(155)
  
turtle.end_fill()
turtle.done()
