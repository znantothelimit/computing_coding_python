# 1. 입력한 정수의 합
'''
num = int(input("초기 정수 입력(0 이하 입력 시 종료) : "))
s=0 
while(num>0):
    s += num
    num = int(input("정수값 다시 입력(0 이하 입력 시 종료) :"))
print("입력된 정수 합 : ", s)
'''

'''
num = int(input("초기 정수 입력(0 이하 입력 시 종료) : "))
s=0
while(1):
    if(num<=0):
        break
    s += num
    num = int(input("정수값 다시 입력(0 이하 입력 시 종료) :"))
print("입력된 정수 합 : ", s)
'''

# 2. 1~100까지 랜덤 수 맞추기
'''
import random
rand_num = random.randint(1, 100)
input_num = 0
cnt = 0
while(True):
    input_num = int(input("값 입력 : "))
    cnt += 1 
    if(rand_num < input_num):
        print("down!")
    elif(rand_num > input_num):
        print("up!")
    else:
        print(rand_num, "correct! count=", cnt)
        break
'''    
'''
import random
rand_num = random.randint(1, 100)
input_num = 0
cnt = 0
while(rand_num != input_num):
    input_num = int(input("값 입력 : "))
    cnt += 1 
    if(rand_num < input_num):
        print("down!")
    elif(rand_num > input_num):
        print("up!")
    else:
        print(rand_num, "correct! count=", cnt)
'''

# 3. 1~50까지 반복, 10에서 강제종료, for문 이용 홀/짝수만 출력, 10까지 출력하느냐 마느냐
# for문 이용 
'''
for i in range(1, 51, 1):
    if(i >= 10): # 10부터 반복 끝
        break
    if(i % 2 == 0): # 홀수 출력
        continue
    print(i, end = " ")
'''
'''
# while문 이용 
i = 0
while(i<=50): 
    i += 1
    if(i > 10): # 짝수 10까지 출력
        break
    if(i % 2 != 0):
        continue
    print(i, end = " ")
'''

# 4. 1~20까지 반복, 10에서 break 짝수의 합계 마지막에 출력
'''
# for문 이용
s = 0
for i in range(1, 21, 1):
    if(i > 10): # 10포함 반복
        break
    if(i % 2 != 0): # 홀수 출력
        continue
    else:
        s += i
print("1~10까지 짝수 합계 : ", s)
'''
'''
# while문 이용 
i = 0
s = 0
while(i<=20): 
    i += 1
    if(i > 10): # 짝수 10까지 출력
        break
    if(i % 2 != 0):
        continue
    else:
        s+=i
print("1~10까지 짝수 합계 : ", s)
'''

'''
# 5. 신호등
while(1):
    light = input("색깔 입력(R, G, 종료시 B 입력) : ")
    if(light == "R"):
        flag = 1
        if(flag == 1):
            print("STOP")
            flag = 0
    elif(light == "G"):
        flag = 1
        if(flag == 1):
            print("GO")
            flag = 0
    elif(light == "B"):
        break
    else:
        print("R, G 중에 입력하시오")
'''

# 6. 1~10 사이 난수 발생하여 덧셈 문제 맞춰보시오
import random
while(1):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(a, "+", b, "=", end = " ")
    val = int(input())
    if((a+b) == val):
        print("correct!")
    else:
        print("incorrect... shutdown...")
        break