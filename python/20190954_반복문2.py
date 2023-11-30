# 20190954 허진환 231130 lecture
"""
# continue문 이용하여 짝수 출력
print("for문 이용(range 1, 11)")
for i in range(1, 11):
    if((i%2) != 0):
        continue
    print(i, " 는 짝수입니다.")

print("while문 이용")
i=0
while(i<=10):
    i+=1
    if((i%2) != 0):
        continue
    print(i, " 는 짝수입니다.")
"""

"""
# break 활용하여 0 입력 시까지 입력된 정수의 합 출력
num = int(input("정수 입력 : "))
sum = 0
while(True):
    sum += num
    if num == 0:
        break
    num = int(input("다시 정수 입력(0 입력시 종료) : "))
print("입력한 정수의 합 : ", sum)
"""

"""
id = "znantothelimit" # 가입 시 입력한 id
id_input = input("id 입력 : ")
if(id == id_input):
    print("login succeses")
else:
    print("login failed")
"""

"""
id = "znantothelimit" # 가입 시 입력한 id
id_input = input("id 입력 : ")
if(id == id_input):
    print("login succeses")
else:
    print("login failed")
    while(True):
        id_input = input("다시 id 입력 : ")
        if(id == id_input):
            print("login succeses")
            break
"""

"""
# for문 이용하여 로그인 횟수 5번 제한
id = "znantothelimit" # 가입 시 입력한 id
id_input = input("id 입력 : ")
if(id == id_input):
    print("login succeses")
else:
    print("login failed")
    for i in range(2, 6):
        id_input = input("다시 id 입력 : ")
        if(id == id_input):
            print("login succeses")
            break
        else:
            print("틀린 횟수(5회 틀릴 시 종료) : ", i)
            continue
"""

"""            
fruit = ["복숭아", "귤", "사과", "수박", "포도"]
a = input("과일 입력 : ")
if(a in fruit):
    print(a, "는 리스트에 있습니다.")
else:
    print(a, "는 리스트에 없습니다.")
"""

"""
import random
choice = random.randint(1, 6)
a = input("엔터키를 눌러 주사위를 던집니다")
if(choice==1):
    print("주사위 수 ", choice)
elif(choice == 2):
    print("주사위 수 ", choice)
elif(choice == 3):
    print("주사위 수 ", choice)
elif(choice == 4):
    print("주사위 수 ", choice)
elif(choice == 5):
    print("주사위 수 ", choice)
else:
    print("주사위 수 ", choice)
"""

"""
# 리스트 학생별 점수 합격여부 출력
score = [87, 86, 50, 80, 99]
n = 0
for i in score:
    n+=1
    if(i>=70):
        print(n, "번 학생은 합격입니다.", i)
    else:
        print(n, "번 학생은 불합격입니다.", i)
"""

"""        
# 2-9 구구단 출력
for i in range(2, 10):
    print("-----", i, "단", "-----")
    for j in range(1, 10):
        print(i, "*", j, "=", i*j)
    print("")
"""

# 입력받은 n단 구구단만 출력
i = int(input("몇 단을 출력할지 입력 : "))
for j in range(1, 10):
    print(i, "*", j, "=", i*j)