'''
# 1. 입력한 정수의 합
# while문 내 조건문
num = int(input("정수를 입력하시오 : "))
sum = 0
while(num>0):
    sum += num
    num = int(input("다시 정수를 입력하시오 : "))

print("입력된 정수 합 : ", sum)

# break문 이용
num = int(input("정수를 입력하시오 : "))
sum = 0
while(True):
    sum += num
    num = int(input("다시 정수를 입력하시오 : "))
    if(num<=0):
        break;

print("입력된 정수 합 : ", sum)
'''
'''
# 2. 1~100까지 랜덤 수 업다운
# while문 내 조건문
import random # 외우기
num = random.randint(1, 100)
input_num = 0
while(input_num != num):
    input_num = int(input("값을 입력하시오 : "))
    if(input_num > num):
        print("down")
    elif(input_num < num):
        print("up")
    else:
        print("정답은 ", num, "입니다. correct")

# break문 이용, cnt 출력
import random
num = random.randint(1, 100)
cnt = 0
input_num = 0
while(1):
    input_num = int(input("값을 입력하시오 : "))
    cnt += 1
    if(input_num < num):
        print("up")
    elif(input_num > num):
        print("down")
    else:
        print(num, "correct! cnt : ", cnt)
        break
'''

# 3. 1~50까지 반복, 10에서 강제종료 10 출력 미포함, for문 이용 홀/짝수만 출력, 10까지 출력하느냐 마느냐
# for문 이용 홀수만 출력 
'''
for i in range(1, 50):
    if(i >= 10):
        break
    if(i%2 != 0):
        print(i, end = " ")
'''        
'''
for i in range(1, 50, 2):
    if(i>=10): break
    print(i, end = " ") 
'''
'''
#continue 이용
for i in range(1, 10):
    if(i>10):
        break
    if(i%2 == 0):
        continue 
    print(i, end = " ")
'''
'''
# while문 이용 짝수만 출력
i = 0
while(True):
    i += 1
    if(i>=10): break
    if(i%2 == 1):
        print(i, end = " ")
'''
'''
i = 1 # 0미포함이므로0
while(i<=10):
    if(i%2 == 1):
        print(i, end = " ")
    i += 1
'''
'''
i = 0
while(True):
    i+=1
    if(i>=10):
        continue
    if(i%2 == 0):
        continue
    print(i, end = " ")
'''
'''
# 4. 1~20까지 반복, 10에서 break 짝수의 합계 마지막에 출력
sum = 0
for i in range(1, 20, 1):
    if(i>=10): break
    if(i%2 == 0):
        sum += i 
print(sum)      
'''
'''
sum = 0
for i in range(1, 20, 1):
    if(i >= 10): break
    if(i%2 != 0):
        continue
    sum += i 
print(sum)      
'''

'''
# 5. 신호등
while(1):
    color = input("신호등 색 입력(R, G) : ")
    if(color == "R"):
        print("stop!")       
    elif(color == "G"):
        print("Go!")
    else: break
'''

'''
# 6. 1~10 사이 난수 발생하여 덧셈 문제 맞춰보시오
import random
num1 = 0
num2 = 0
while(True):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    print(num1," + ", num2, " =", end = " ")
    val = int(input(""))
    if(val != (num1+num2)): break
'''

'''
# 7. 리스트 학생별 점수 합/불합격 출력
score = [100, 56, 80, 40, 77]
index=0
for i in score:
    index += 1
    if(i >= 75):
        print(index,"번 째 학생은 합격입니다")
    else:
        print(index, "번째 학생은 불합격입니다")
'''

'''
# 8. 과일들 저장된 리스트 중 입력된 과일이 있는지
fruit = ["peach", "pear", "watermelon", "grape", "orange"]
input_fruit = input("과일을 입력하세요 : ")
if (input_fruit in fruit):
    print(input_fruit, "는 리스트 내에 있습니다")
else:
    print(input_fruit, "는 리스트 내에 없습니다") 
'''

# 9. 2-9 구구단 출력
for i in range(2, 10, 1):
    print("----",i,"단----")
    for j in range(1, 10, 1):
        print(i, "*", j, "=", i*j)
    print("\n")