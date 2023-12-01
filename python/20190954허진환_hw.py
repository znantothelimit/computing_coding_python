# 20190954 허진환 컴퓨팅사고와 코딩기초 

import turtle

# 거북이 설정
t = turtle.Turtle()
t.shape("turtle")
t.left(90)  # 초기 방향을 위쪽으로 설정

### 6회 반복 -> 각 반복마다 left 60 degree rotate ###
for i in range(0, 6):
    # 초기 130 길이 전진 후 좌우 가지 그리기위해 30 길이 후진
    t.forward(130) 
    t.forward(-30)

    # 좌측 가지 그리기 위해 left 60 degree rotate 후 30길이 전/후진 
    t.left(60) 
    t.forward(30) 
    t.forward(-30)

    # 우측 가지 그리기 위해 right 120 degree rotate 후 30길이 전/후진 
    t.right(120)
    t.forward(30)
    t.forward(-30)

    # 각 반복 당 시행했던 초기방향으로 정렬 후 원점으로 후진
    t.left(60)
    t.forward(-100)

    # 총 6개의 긴 선 그려야 하므로 반복 시마다 left 60degree rotate
    t.left(60)