'''
import turtle

turtle.shape("turtle")
'''
'''

turtle.circle(100)
turtle.circle(100,steps=6)

for i in range(3):
    turtle.forward(100)
    turtle. left(120)

turtle.forward(100)
turtle. left(90)

turtle.forward(100)
turtle. left(90)

turtle.forward(100)

turtle.clear()
'''
'''
# 노란 원 그리기
turtle.fillcolor("yellow") 
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# 다음 도형 그리기 위한 이동
turtle.up()                 
turtle.goto(100,0)
turtle.down()

# 빨간 원 그리기
turtle.fillcolor("red") 
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# 다음 도형 그리기 위한 이동
turtle.up()                 
turtle.goto(200,0)
#turtle.forward(100)
turtle.down()

#파란 원 그리기
turtle.fillcolor("blue") 
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
'''

'''
### 집그리기 ###

# 삼각형 - 지붕
turtle.forward(200)
turtle. left(120)
turtle.forward(200)
turtle.left(120)
turtle. forward(200)

#사각형
turtle.left(30)        
for i in range(4):
    turtle.forward(200)
    turtle.left(90)

# 문
turtle.forward(200)
turtle. left(90)
turtle.forward(100)
turtle. left(90)
turtle.forward(100)
turtle. left(90)
turtle.forward(60)
turtle. left(90)

# 문 손잡이
turtle.forward(50) 
turtle.circle(10)
turtle.forward(50)
'''



import turtle
import random

# 첫 번째 거북이
t1 = turtle. Turtle()
# 두 번째 거북이 
t2 = turtle.Turtle() 

t1.color("pink")
t1.shape("turtle")
t1.shapesize(5)
t1.pensize(5)

t2.color("blue")
t2.shape("turtle")
t2.shapesize(5)
t2.pensize(5)

t1.penup()
t1.goto(-400, 100)

t2.penup()
t2.goto(-400, -100)

# 난수발생으로 거북이 경주
for i in range(30):             
    d1 = random.randint(1, 50) 
    t1.forward(d1)             
    d2 = random.randint(1, 50)  
    t2.forward(d2)
