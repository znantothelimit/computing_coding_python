#20190954 반복문 231123lecture

'''
# for문
for i in [1,2,3,4,5]:
    print(i, "hello")
'''

'''
for i in range(1, 6):
    print("hello", i, end = " ")
'''

'''
# 홀수 출력 
for i in range(0, 10, 2):
    print(i, end = " ")

print("\n")

# 짝수 출력
for i in range(0, 10):
    if(i%2== 0):
        print(i, end = " ")

print("\n")

for i in reversed(range(0, 10, 2)):
    print(i, end = " ")
'''

'''
# while문
i=1
while(i<=10):
    print(i, end = " ")
    i += 1
print("반복 종료")

j=10
while(j>=0):
    print(j, end = " ")
    j -= 1
print("반복 종료")
'''

'''
# 홀수값을 입력하다가 짝수 값이 입력되면 반복 종료
while(1):
    a = int(input("숫자 입력(짝수 입력 시 반복 종료) : "))
    print(a)
    if(a % 2 == 0): break
'''

# 난수 발생, 컴퓨터가 발생한 난수 맞추기 updown game
import random
ran = random.randint(1, 100)
i = 0
while(1):
    scan = int(input("숫자 입력(updown game ; 0-100) : "))
    i += 1
    if(scan>ran):
        print(scan, "down\n")
    elif(scan<ran):
        print(scan, "up\n")
    else:
        print(ran, scan, "correct\n")
        print("시도횟수 : ", i, end = "\n")
        break

