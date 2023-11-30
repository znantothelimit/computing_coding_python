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
